#!/usr/bin/env python3
"""simple pagination"""
from typing import Tuple
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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        pages = []
        start, end = index_range(page, page_size)
        print(f'start: {start}, end: {end}')

        with open('Popular_Baby_Names.csv', newline='') as names:
            csv_file = csv.reader(names)
            # num_of_rows = len(list(csv_file))
            # if end >= num_of_rows:
            #     return pages
            csv_file.__next__()  # skip titles row
            line = 0
            for row in csv_file:
                if line >= start and line < end:
                    pages.append(row)
                elif line >= end:
                    break

                line += 1
        return pages


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of index range to be returned
    from a list based on page and page_size
    """
    return (page - 1) * page_size, page * page_size
