"""Manage bike-share stations with validated records and safe SQL queries."""

import secrets
import sqlite3
from contextlib import closing


class BikeShareManager:
    """Keep station data in an independent, in-memory SQLite database."""

    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.execute(
            "CREATE TABLE stations ("
            "id INTEGER PRIMARY KEY, "
            "name TEXT NOT NULL CHECK (length(trim(name)) > 0), "
            "capacity INTEGER NOT NULL "
            "CHECK (typeof(capacity) = 'integer' AND capacity > 0), "
            "bikes INTEGER NOT NULL "
            "CHECK (typeof(bikes) = 'integer' "
            "AND bikes >= 0 AND bikes <= capacity))"
        )

    def add_station(self, name, capacity, bikes, log=None):
        """Add a valid station and return a caller-owned registration log."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Station name must be a non-empty string.")
        if (
            isinstance(capacity, bool)
            or not isinstance(capacity, int)
            or capacity <= 0
        ):
            raise ValueError("Capacity must be a positive integer.")
        if (
            isinstance(bikes, bool)
            or not isinstance(bikes, int)
            or not 0 <= bikes <= capacity
        ):
            raise ValueError("Bikes must be an integer from zero to capacity.")
        if log is None:
            log = []
        name = name.strip()
        with self.connection:
            self.connection.execute(
                "INSERT INTO stations (name, capacity, bikes) "
                "VALUES (?, ?, ?)",
                (name, capacity, bikes),
            )
        log.append(name)
        return log

    def rent_bike(self, station_id):
        """Rent one bike; return False for empty or missing stations."""
        with self.connection:
            result = self.connection.execute(
                "UPDATE stations SET bikes = bikes - 1 "
                "WHERE id = ? AND bikes > 0",
                (station_id,),
            )
        return result.rowcount == 1

    @staticmethod
    def unlock_pin():
        """Generate a four-digit unlock PIN using a secure random source."""
        return secrets.randbelow(9000) + 1000

    def full_stations(self):
        """Return names of full stations in registration order."""
        rows = self.connection.execute(
            "SELECT name FROM stations WHERE bikes = capacity ORDER BY id"
        ).fetchall()
        return [row[0] for row in rows]

    def reset_station(self, station_id):
        """Empty a station; return whether it exists, propagating DB errors."""
        with self.connection:
            result = self.connection.execute(
                "UPDATE stations SET bikes = 0 WHERE id = ?", (station_id,)
            )
        return result.rowcount == 1

    def has_bikes(self, station_id):
        """Return whether a station exists and has any bikes available."""
        row = self.connection.execute(
            "SELECT bikes FROM stations WHERE id = ?", (station_id,)
        ).fetchone()
        return row is not None and row[0] > 0

    def close(self):
        """Close the underlying database connection."""
        self.connection.close()


def main():
    """Demonstrate registration, rentals, PINs, full stations and resets."""
    with closing(BikeShareManager()) as manager:
        manager.add_station("Central Park", 10, 10)
        manager.add_station("Metro Gate", 8, 2)
        print("Rent at station 2:", manager.rent_bike(2))
        print("Rent at missing station 9:", manager.rent_bike(9))
        print("Unlock PIN:", manager.unlock_pin())
        print("Full stations:", manager.full_stations())
        print("Station 2 has bikes:", manager.has_bikes(2))
        print("Reset station 1:", manager.reset_station(1))
        print("Station 1 has bikes after reset:", manager.has_bikes(1))


if __name__ == "__main__":
    main()
