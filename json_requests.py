import functools
import requests


class JsonRequests(object):
    def __init__(self, **kwargs):
        self._kwargs = kwargs

    def __getattr__(self, attr_name):
        attr = getattr(requests, attr_name)
        if not callable(attr):
            return attr
        @functools.wraps(attr)
        def attrwrapper(*args, **kwargs):
            result = attr(*args, **{ **self._kwargs, **kwargs })
            if not isinstance(result, requests.models.Response):
                return result
            result.raise_for_status()
            return result.json()
        return attrwrapper
