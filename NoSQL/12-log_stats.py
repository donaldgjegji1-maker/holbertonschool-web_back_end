#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""

import subprocess
import json


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
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        return "0"


def get_nginx_stats():
    """Retrieve and display Nginx log statistics"""

    # Get total number of logs
    total_logs = run_mongo_command("db.nginx.countDocuments()")
    print(f"{total_logs} logs")

    # Methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    # Count each method
    for method in methods:
        cmd = f'db.nginx.countDocuments({{"method": "{method}"}})'
        count = run_mongo_command(cmd)
        print(f"    method {method}: {count}")

    # Count status check (method=GET and path=/status)
    sts_cmd = 'db.nginx.countDocuments({"method": "GET", "path": "/status"})'
    status_check = run_mongo_command(sts_cmd)
    print(f"{status_check} status check")


if __name__ == "__main__":
    get_nginx_stats()
