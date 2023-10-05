#!/usr/bin/env python3
"""Safely return the first element of a sequence or None if the sequence is empty."""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Args:
        lst (Sequence[Any]): The input sequence of any type.

    Returns:
        Union[Any, None]: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
