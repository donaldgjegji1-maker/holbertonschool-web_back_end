#!/usr/bin/env python3
"""
Provides stats about Nginx logs stored in MongoDB
"""
import subprocess


def run_mongo_command(command):
    """Run a single MongoDB command and return the result"""
    try:
        full_cmd = f'db = db.getSiblingDB("logs"); {command}'
        result = subprocess.run(
            ['mongo', '--quiet', '--eval', full_cmd],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return "0"


def main():
    # Get total logs
    total_logs = run_mongo_command("db.nginx.count()")
    print(f"{total_logs} logs")

    # Methods
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = run_mongo_command(f'db.nginx.count({{method: "{method}"}})')
        print(f"    method {method}: {count}")

    # Status check
    sts = run_mongo_command('db.nginx.count({method: "GET", path: "/status"})')
    print(f"{sts} status check")


if __name__ == "__main__":
    main()
