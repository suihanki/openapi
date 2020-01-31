"""
Public API.
"""
from openapi.model import OpenAPI


def load(fileobj):
    """
    Load OpenAPI model objects (from json).

    """
    return OpenAPI.load(fileobj)


def loads(s):
    """
    Load OpenAPI model objects (from json).

    """
    return OpenAPI.loads(s)


def dump(obj, fileobj):
    """
    Dump OpenAPI model objects (to json).

    """
    return obj.dump(fileobj)


def dumps(obj):
    """
    Dump OpenAPI model objects (to json).

    """
    return obj.dumps()
