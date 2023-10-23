#!/usr/bin/env python3
"""
This module contains the function index_range that takes two integer arguments
and returns a tuple containing a start index and an end index for a particular
pagination page.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
            Returns a tuple containing a start index and an end index for a particular
                pagination page.

                    Args:
                            page (int): page number
                                    page_size (int): number of items per page

                                        Returns:
                                                Tuple[int, int]: tuple containing a start index and an end index
                                                    """
                                                        if page <= 0 or page_size < 0:
                                                                    return (-1, -1)

                                                                    return (page_size * (page - 1), page_size * page)
