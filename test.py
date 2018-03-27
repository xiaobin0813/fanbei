#!/usr/bin/python
# coding: UTF-8
import time
import tushare as ts


def get_roe_time():
    date_year = int(time.strftime('%Y', time.localtime(time.time())))
    date_month = int(time.strftime('%m', time.localtime(time.time())))
    if date_month in (1, 2, 3):
        roe_year = date_year - 1
        roe_month = 4
        return roe_year, roe_month
    elif date_month in (4, 5, 6):
        roe_year = date_year
        roe_month = 1
        return roe_year, roe_month

    elif date_month in (7, 8, 9):
        roe_year = date_year
        roe_month = 2
        return roe_year, roe_month

    else:
        roe_year = date_year
        roe_month = 3
        return roe_year, roe_month


if __name__ == '__main__':
    STOCK = ['600016',
             '600015',
             '601328',
             '601166',
             '601818',
             '601288',
             '600000',
             '600919',
             '601988',
             '601997',
             '601998',
             '000001',
             '601398',
             '601939',
             '600036',
             '002142',
             '601169',
             '601009']


    df1 = ts.get_stock_basics()
    # Index([u'name', u'industry', u'area', u'pe', u'outstanding', u'totals',
    #   u'totalAssets', u'liquidAssets', u'fixedAssets', u'reserved',
    #  u'reservedPerShare', u'esp', u'bvps', u'pb', u'timeToMarket', u'undp',
    # u'perundp', u'rev', u'profit', u'gpr', u'npr', u'holders'],
    # dtype='object')
    name1=df1.ix[STOCK]['name']
    pe1 = df1.ix[STOCK]['pe']
    pb1 = df1.ix[STOCK]['pb']
    # ROE = P/(E0 + NP÷2 + Ei×Mi÷M0 - Ej×Mj÷M0 ).
    df2=ts.get_today_all()
    ''''
    code：代码
    name:名称
    changepercent:涨跌幅
    trade:现价
    open:开盘价
    high:最高价
    low:最低价
    settlement:昨日收盘价
    volume:成交量
    turnoverratio:换手率
    amount:成交量
    per:市盈率
    pb:市净率
    mktcap:总市值
    nmc:流通市值
    '''''
    name2 = df2.ix[STOCK]['name']
    per2 = df2.ix[STOCK]['per']
    pb2 = df2.ix[STOCK]['pb']
    # pb2=nan？？？
    ### ！！！print df2.pb
    print pb1
    ##pb1 is OK。。。，
