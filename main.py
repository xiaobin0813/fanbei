#!/usr/bin/python
# coding: utf-8


"""This script parse stock info"""

import tushare as ts
import math
from pandas import Series,DataFrame
import pandas as pd
import time

def get_name(code):
    df = ts.get_stock_basics()
    name = df.ix[code,'name']
    return name
def get_pb(code):
    df1 = ts.get_stock_basics()
    pb = df1.ix[code,'pb']
    return pb
def get_roe_time():
    date_year = int(time.strftime('%Y', time.localtime(time.time())))
    date_month = int(time.strftime('%m', time.localtime(time.time())))

    if date_month in (1, 2, 3):
        roe_year = date_year - 1
        roe_month = 4
    elif date_month in (4, 5, 6):
        roe_year = date_year
        roe_month = 1
    elif date_month in (7, 8, 9):
        roe_year = date_year
        roe_month = 2
    else:
        roe_year = date_year
        roe_month = 3
    return roe_year, roe_month

def get_roe(code):
    '测试发现roe1获取的结果为nan'
    get_roe_time()
    date = get_roe_time()
    df1 = ts.get_report_data(date[0], date[1])
    roe = df1.ix[code, 'roe']
    if 'nan'in roe and date[1]!=1:
        df2 = ts.get_report_data(date[0], date[1]-1)
        roe = df2.ix[code, 'roe']
    elif 'nan'in roe and date[1]==1:
        df3 = ts.get_report_data(date[0]-1, 4)
        roe = df3.ix[code, 'roe']
    return roe

def get_roe2(code):
    '测试发现roe2获取的结果也为nan'
    get_roe_time()
    date = get_roe_time()
    df2 = ts.get_profit_data(date[0], date[1])
    roe = df2.ix[code, 'roe']
    return roe

def get_fb1(code):
    'LOG(市净率两倍，资产收益率+1) ,pb;市净率 roe,净资产收益率(%)roe的来源：1业绩报告（主表）2，盈利能力数据'
    name=get_name(code)
    pb=get_pb(code)
    roe=get_roe(code)
    i = 0
    fbx=[]
    namex=[]
    print("\n")
    print "i\tcode\tname\tpb\tfb"
    for i in range(len(pb.values)):
        pbv = pb.values[i]
        roev = pb.values[i]
        bankrov=[]
        #由于拿不到正常的roe值，原因是roe这个指标缺失，取的结果是nan；这里暂时使用pb的值代替
        #fb1 = math.log(pbv*2,(roev/100) + 1)
        fb1 = math.log(pbv*2,(10.89/100) + 1)
        #print i + 1, pb.index[i],pb.values[i],float('%.2f' % fb1)
        print i + 1, pb.index[i],name[i],pb.values[i],float('%.2f' % fb1)
        fbx.append(round(fb1,2))
        namex.append(name[i])
        i += 1
    print "The following is FB："
    #return fbx
    return  dict(zip(STOCK,fbx))

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
    TEST  = ['600219',  ##南山铝业
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
    bankroe=['600016',
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

    print get_fb1(STOCK)

