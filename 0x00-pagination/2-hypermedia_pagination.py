#!/usr/bin/env python3
"""Task 1"""

import csv
import math
from typing import List, Dict
index_range = __import__('0-simple_helper_function').index_range


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
        """Returns the recommended server page list"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        rang = index_range(page, page_size)
        self.dataset()
        return self.__dataset[rang[0]:rang[1]]

    def get_hyper(self, pag: int = 1, pag_size: int = 10) -> Dict[str, object]:
        """Implements Hypermedia pagination"""
        rang = index_range(pag, pag_size)
        data = self.get_page(pag, pag_size)
        if data:
            page_size = len(data)
        else:
            page_size = 0
        page = pag
        if rang[0] + pag_size < len(self.__dataset) - 1:
            next_page = page + 1
        else:
            next_page = None
        if page == 1:
            prev_page = None
        else:
            prev_page = page - 1
        total_pages = math.ceil(len(self.__dataset) / pag_size)
        return ({
                "page_size": page_size, "page": page,
                "data": data, "next_page": next_page,
                "prev_page": prev_page, "total_pages": total_pages
                })
