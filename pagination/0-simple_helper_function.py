#!/usr/bin/env python3
"""
This module provides a helper function to calculate start and end indexes
for pagination based on page number and page size.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start index and end index for pagination.

    The page parameter is 1-indexed, meaning the first page is page 1.
    """
    start_index: int = (page - 1) * page_size
    end_index: int = page * page_size
    return start_index, end_index

