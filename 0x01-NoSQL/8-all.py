#!/usr/bin/env python3
"""Defines a function that lists all documents in collection"""
import pymongo


# if __name__ == '__main__':
def list_all(mongo_collection):
    """Returns a list of document"""
    return [] if not mongo_collection else list(mongo_collection.find())
