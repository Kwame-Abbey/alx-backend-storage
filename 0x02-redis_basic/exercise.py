#!/usr/bin/env python3
"""Write strings to redis"""
import redis
import uuid
from typing import Union


class Cache:
    """Creates a class"""
    def __init__(self) -> None:
        """Initializes once an instance is created"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Returns the key"""
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key
