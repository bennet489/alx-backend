#!/usr/bin/env python3
""" Implement a method named get_page that takes two integer
arguments page with defautl value 1 and page_size with default
value 10 """

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """two args are passed and returns tuple size of two
    containing the start and end indices relating to the range
    of indices to return in a list for the said pagination params
    Args:
        page(int): number of page to return
        page_size(int): items per page number
    Return: tuple(start, end) """
    start = 0
    end = 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)


class Server:
    """ A server class to paginate database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__data = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """function will take two int args page = 1 and page_size = 10
        and return the requested page of the dataset
        Args:
            page(int): requested page (must be positive value greater than 0)
            page_size(int): number of items per page(must be positive value
            greater than 0)
        Return:
            list of list containing required data """
        assert type(page) == int and typ(page_size) == int and\
            page > 0 and page_size > 0
        data = self.dataset()
        try:
            index = index_range(page, page_size)
            return data[index[0]: index[1]]
        except IndexError:
            return []
