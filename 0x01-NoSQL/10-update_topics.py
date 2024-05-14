#!/usr/bin/env python3
"""Changes all topics of school document"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a document"""
    return mongo_collection.update_many(
        {"name": name},
        {'$set': {"topics": topics}}
    )
