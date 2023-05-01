#!/usr/bin/env python3
"""simple pagination"""
from typing import Dict, Tuple
import csv
import math
from typing import List


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
        """returns a list of rows based on page and page_size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        pages = self.dataset()[start:end]
        return pages

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """return a dict containing data and metadata for pages requested"""
        len_dataset = len(self.dataset())
        page_data = self.get_page(page=page, page_size=page_size)
        total_pages = math.ceil(len_dataset / page_size)
        prev_page = page - 1 if page - 1 >= 1 else None
        next_page = page + 1 if page + 1 < total_pages else None

        return {
            'page_size': page_size,
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of index range to be returned
    from a list based on page and page_size
    """
    return (page - 1) * page_size, page * page_size
