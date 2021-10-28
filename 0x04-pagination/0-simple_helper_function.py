#!/usr/bin/env python3
""" This module contain the function named index_range that
takes two integer arguments page and page_size """


def index_range(page: int, page_size: int):
    """ The function should return a tuple of size
    two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters """

    size = page * page_size
    return (size - page_size, size) 
