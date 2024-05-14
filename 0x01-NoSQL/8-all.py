#!/usr/bin/env python3
"""Defines a function that lists all documents in collection"""


# if __name__ == '__main__':
def list_all(mongo_collection):
    all_documents = mongo_collection.find()
    if all_documents is None:
        return []
    return all_documents
