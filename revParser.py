import numpy as np
import pandas as pd
import requests
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import seaborn as sns
from enum import Enum


class CompanyType(Enum):
    sii = 1
    otc = 2
    pub = 3


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def parse_single_month(year: str, month: str, tick: str, company_type: CompanyType):
        '''
        :param year: ROC calendar
        :param month: the month you that you want to query
        :param tick: the tick number of company
        :param company_type:
        :return:
        '''
        assert 1 <= int(month) <= 12, "input month string should be valid number"
        # parse information form TWSE
        date = '_'.join([year, month])
        url = 'https://mops.twse.com.tw/nas/t21/' + company_type + '/t21sc03_' + date + '_0.html'
        df_html = pd.read_html(url)
        # get revenue information from dataframe

        return df_html
