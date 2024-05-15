#!/usr/bin/env python3
"""Write strings to redis"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self,
            key: str, fn: Optional[Callable] = None) -> str:
        """takes a key string argument and an optional
        Callable argument named fn
        """
        data = self._redis.get(key)
        return fn(data) if fn is not None else data

    def get_str(self, data: str) -> str:
        """returns str value of decoded byte """
        return data.decode('utf-8', 'strict')

    def get_int(self, data: str) -> int:
        """returns int value of decoded byte """
        return int(data)
