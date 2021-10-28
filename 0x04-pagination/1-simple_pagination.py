#!/usr/bin/env python3
""" This module contain the function named index_range that
takes two integer arguments page and page_size """
import csv
import math
from typing import List


def index_range(page: int, page_size: int):
    """ The function should return a tuple of size
    two containing a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters """

    size = page * page_size
    return (size - page_size, size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert(type(page) == int)
        assert(type(page_size) == int)
        assert page > 0
        assert page_size > 0

        pages, page_sizes = index_range(page, page_size)
        csv = []
        if pages >= len(self.dataset()):
            return csv
        csv = self.dataset()
        return csv[pages:page_sizes]
