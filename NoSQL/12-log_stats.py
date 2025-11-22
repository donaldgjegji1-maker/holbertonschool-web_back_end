#!/usr/bin/env python3
""" 12-log_stats.py """

from pymongo import MongoClient


def get_nginx_stats():
    """Retrieve and display Nginx log statistics"""

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    # Get total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    # Count all methods in one query using aggregation
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]

    method_counts = {}
    for doc in collection.aggregate(pipeline):
        method_counts[doc["_id"]] = doc["count"]

    # Print methods in the required order
    for method in methods:
        count = method_counts.get(method, 0)
        print(f"    method {method}: {count}")

    # Count status check
    status_check = collection.count_documents({
        "method": "GET", 
        "path": "/status"
    })
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
