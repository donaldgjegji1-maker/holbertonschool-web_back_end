#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""

import subprocess


def run_mongo_command(command):
    """Run a MongoDB command and return the result"""
    try:
        result = subprocess.run(
            ['mongo', 'logs', '--eval', command, '--quiet'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        # If command fails, return empty string
        return ""


def get_nginx_stats():
    """Retrieve and display Nginx log statistics"""

    # First, check if we can connect to the database
    test_connection = run_mongo_command("db.getCollectionNames()")
    if not test_connection:
        print("0 logs")
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            print(f"    method {method}: 0")
        print("0 status check")
        return

    # Get total number of logs
    total_logs = run_mongo_command("db.nginx.countDocuments()")
    if not total_logs:
        total_logs = "0"
    print(f"{total_logs} logs")

    # Methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    # Count each method
    for method in methods:
        cmd = f'db.nginx.countDocuments({{"method": "{method}"}})'
        count = run_mongo_command(cmd)
        if not count:
            count = "0"
        print(f"    method {method}: {count}")

    # Count status check (method=GET and path=/status)
    sts_cmd = 'db.nginx.countDocuments({"method": "GET", "path": "/status"})'
    status_check = run_mongo_command(sts_cmd)
    if not status_check:
        status_check = "0"
    print(f"{status_check} status check")


if __name__ == "__main__":
    get_nginx_stats()