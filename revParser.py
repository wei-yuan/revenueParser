import numpy as np
import pandas as pd
import requests
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import seaborn as sns
from enum import Enum
from io import StringIO


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
        r = requests.get(url=url)
        # Big-5 or Big5 is a Chinese character encoding method used in Taiwan, Hong Kong, and Macau
        # for traditional Chinese characters.
        r.encoding = 'big5'
        df_html = pd.read_html(StringIO(r.text), encoding='big5')
        # get revenue information from dataframe
        # 2021/5/3 to extract the data we want, do something brutally here...
        df = pd.concat([df.iloc[:-1, :] for df in df_html[0:] if df.shape[1] == 11])
        # get rid of the header that I don't need
        df = df.droplevel(0, axis=1)

        return df
