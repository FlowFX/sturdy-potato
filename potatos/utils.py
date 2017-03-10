"""Utility functions for the potatoes projet."""

import string

try:
    from secrets import choice       # Python3.6+ only
except ImportError:                  # pragma: no cover
    from random import choice


def random_key(length):
    """Return a random alphanumeric string of length 'length'."""
    alphabet = string.ascii_letters + string.digits
    while True:
        key = ''.join(choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in key) and
                any(c.isupper() for c in key) and
                    sum(c.isdigit() for c in key) >= 3):
            break
    return key

