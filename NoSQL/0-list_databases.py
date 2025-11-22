#!/usr/bin/env python3
"""
Script that lists all databases in MongoDB
"""

from pymongo import MongoClient


def list_databases():
    """
    List all databases.
    """
    # Connect to local MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # Get list of database names
    dbs = client.list_database_names()

    # Print each database name
    for db in dbs:
        print(db)


if __name__ == "__main__":
    list_databases()
