#!/usr/bin/env python3
"""8-all.py"""


def list_all(mongo_collection):
    """
    List of all documents. Empty list if no documents.
    """

    if mongo_collection is None:
        return []

    return list(mongo_collection.find())
