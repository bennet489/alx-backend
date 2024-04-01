#!/usr/bin/env python3
"""A function named index_range that takes two integer arguments page
and page_size """
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    returns a tuple of size two consisting a start
    index and end index that relates to the range
    of indexes to return in a list for those
    particular pagination params
    :param page:
    :param page_size:
    :return:
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
