#!/usr/bin/env python3
"""
Adds `get_page` method to `Server` class
"""
from typing import List, Tuple
import csv


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """dataset Cached
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """start and end index range for a `page`, with `page_size`
        """
        StartIndex = page * page_size
        return StartIndex - page_size, StartIndex

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """finds the correct indexes to paginate the dataset
        correctly and return the appropriate page of the dataset
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        indexStart, endIndex = self.index_range(page, page_size)
        return self.dataset()[indexStart:endIndex]

    def get_hyper(self, page: int,
                  page_size: int) -> Dict[str, Union[int, List[List], None]]:
        """
        method that takes the same arguments
        (and defaults) as get_page and returns a dictionary
        containing the following key-value pairs:
        """
        data = self.get_page(page, page_size)
        rowsTotal = len(self.dataset())
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1
        if self.index_range(page, page_size)[1] >= rowsTotal:
            next_page = None
        total_pages = rowsTotal / page_size
        if total_pages % 1 != 0:
            total_pages += 1
        return {'page_size': len(data), 'page': page,
                'data': data, 'next_page': next_page,
                'prev_page': prev_page, 'total_pages': int(total_pages)}
