#!/usr/bin/env python3
"""simple pagination"""
from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of index range to be returned
    from a list based on page and page_size
    """
    return (page - 1) * page_size, page * page_size
