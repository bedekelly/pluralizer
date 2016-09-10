class LambdaException(Exception):
    """
    Stub class to wrap all exceptions to be caught only by AWS Lambda
    infrastructure.
    """


class BadRequest(LambdaException):
    """
    Represent a Bad Request error (i.e. an HTTP 400).
    """


def bad_request(message):
    """Utility to return a BadRequest error with the given message."""
    return BadRequest("Bad Request: {}".format(message))

