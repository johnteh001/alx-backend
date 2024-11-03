#!/usr/bin/env python3
"""0-simple_helper_function.py"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Function determines start and end index
    Args:
        page(int): page number
        page_size(int): the number of list per page
    Returns:
        (int, int): start and end index for the page
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
