#!/usr/bin/python
# coding: UTF-8

"""This script parse stock info"""

import tushare as ts
import math
from pandas import Series,DataFrame
import pandas as pd
import time

def get_roe_time():
    date_year = int(time.strftime('%Y', time.localtime(time.time())))
    date_month = int(time.strftime('%m', time.localtime(time.time())))
    if date_month in (1, 2, 3):
        roe_year = date_year - 1
        roe_month = 4
        print 1, roe_year, roe_month
    elif date_month in (4, 5, 6):
        roe_year = date_year
        roe_month = 1
        print 2, roe_year, roe_month
    elif date_month in (7, 8, 9):
        roe_year = date_year
        roe_month = 2
        print 3, roe_year, roe_month
    else:
        roe_year = date_year
        roe_month = 3
        print 4, roe_year, roe_month
    print roe_year, roe_month


def get_roe(code):
    get_roe_time()
    df2 = ts.get_profit_data(roe_year, roe_month)
    # roe1 = df2[u'code'][u'roe']
    roe = df2[u'roe']
    df3 = ts.get_hist_data(roe_year, roe_month)
    roe = df3[u'roe']
    idx=0
    for idx in range(len(roe)):
        roe_val = roe[idx]
        idx+=1
        print roe_val



def get_pb(code):
    df1 = ts.get_stock_basics()
    # pb = df[['pb']]
    pb = df1.ix[code]['pb']
def get_fb2(code):
    get_pb(code)
    get_roe()
    i=0
    for i in range(len(pb.values)):
        pbv=pb.values[i]
        roev=roe.values[i]
        fb=math.log(pbv*2,(roev/100)+1)
        print i+1,pb.index[i],pb.values[i],roe.index[i],roe.values[i],fb
        i+=1
    ##


if __name__ == '__main__':
    STOCK1  = ['600219',  ##南山铝业
             '000002',  ##万  科Ａ
             '000623',  ##吉林敖东
             '000725',  ##京东方Ａ
             '600036',  ##招商银行
             '601166',  ##兴业银行
             '600298',  ##安琪酵母
             '600881',  ##亚泰集团
             '002582',  ##好想你
             '600750',  ##江中药业
             '601088',  ##中国神华
             '000338',  ##潍柴动力
             '000895',  ##双汇发展
             '000792']  ##盐湖股份
    STOCK2=['HK001988','HK000998','HK006818','HK003328','HK001963','HK003618','HK003988','SH600016','SH600015','SH601328','HK001288','SH601166','SH601818','HK001398','HK000939','SH601288','SH600000','SH600919','SH601988','SH601997','HK003968','SH601998','SZ000001','SH601398','SH601939','SH600036','SZ002142','SH601169','SH601009']        #get_all_price(STOCK)
    STOCK3=['001988','000998','006818','003328','001963','003618','003988','600016','600015','601328','001288','601166','601818','001398','000939','601288','600000','600919','601988','601997','003968','601998','000001','601398','601939','600036','002142','601169','601009']
    code = ['600016','600015','601328','601166','601818','601288','600000','600919','601988','601997','601998','000001','601398','601939','600036','002142','601169','601009']
    #timeToMarket(STOCK)
    print get_pb(code)


