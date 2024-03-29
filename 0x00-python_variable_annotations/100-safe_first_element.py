#!/usr/bin/env python3
"""
10. Duck typing - first element of a sequence
"""
from typing import List, Tuple, Sequence, Iterable, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function
    """
    if lst:
        return lst[0]
    else:
        return None
