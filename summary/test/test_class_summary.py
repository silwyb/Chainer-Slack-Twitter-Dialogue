#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))
import pyximport
pyximport.install()
from class_summary import ClassSummary
from split_data.input_file_cython import InputFileCython
from os import path
APP_ROOT = path.dirname(path.abspath(__file__))
import re


class Test_ClassSummary(unittest.TestCase):
    """Test Class Summary class.

    """
    def setUp(self):
        """
        setting initial paramater
        Args:
            data: test file name
            split_module: setting the split_module instance
        """
        wiki_vector_file_name = APP_ROOT + '/../../Data/jawiki_vector/jawiki_vector.txt'
        self.input_module = InputFileCython(wiki_vector_file_name)

    def test_summary_class(self):
        """
        test make summary dict
        """
        self.input_module.input_fast_large_file()
        wiki_vector = self.input_module.get_vector()
        read_file = '13996061-n.txt'
        class_summary = ClassSummary(read_file, wiki_vector)
        class_summary.summary_class()


if __name__ == '__main__':
    unittest.main()
