'''
Use fluent API here
For more information about assertpy, see: https://assertpy.github.io/docs.html
'''
import os
import sys
import pytest
from assertpy import assert_that

rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(rootDir)
from revParser import Parser, CompanyType


class TestParser:

    def test_join(self):
        assert_that('_'.join(['A', 'A'])).is_equal_to('A_A')

    def test_parse_single_month(self):
        assert_that(Parser.parse_single_month_revenue('110', '3', '6150', CompanyType.otc.name)).is_equal_to(695679)


if __name__ == '__main__':
    pass
