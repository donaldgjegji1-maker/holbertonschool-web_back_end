#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import MongoClient


def log_stats():
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs  # Use the 'logs' database
    collection = db.nginx  # Use the 'nginx' collection

    # Total number of documents in the collection
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # HTTP Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # GET method with path = /status
    status_check = collection.count_documents({
        "method": "GET", "path": "/status"
        })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
