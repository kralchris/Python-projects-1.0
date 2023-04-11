"""
I wrote the previous code to show off. This one is the optimized version of it --- with time complexity
of O(nm). It is much better than the previous one, though its "cool factor" is smaller.
"""

import re

def algo(zpravy, min_length, max_length, negativni):
    if not isinstance(zpravy, list):
        raise ValueError("zpravy must be a list")
    if not isinstance(min_length, int):
        raise ValueError("min_length must be an integer")
    if not isinstance(max_length, int):
        raise ValueError("max_length must be an integer")
    if min_length < 0 or max_length < 0:
        raise ValueError("min_length and max_length must be non-negative")
    if min_length > max_length:
        raise ValueError("min_length cannot be greater than max_length")

    filtrovane = (
        x for x in zpravy
        if isinstance(x, (int, float))
        or (isinstance(x, str) and min_length <= len(x) <= max_length
            and not any(y.lower() in x.lower() for y in negativni)
            and not re.match(r"(?:https?://)?(?:www\.)?([a-z0-9]+(?:-[a-z0-9]+)*\.(?:com|org|net|gov|edu|biz|info|io|uk|us|ca|au|nz|in|co|eu|cz|be))", x))
    )
    return list(set(filtrovane))
