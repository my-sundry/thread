#!/usr/bin/ python3
# -*- coding:utf-8 -*-
'''
   Author:zyf
   功能：利用tushare库下载可交易日，并保存为csv文件。
'''
import tushare as ts
start = '20190101'
end   = '20191231'

ts.set_token('89b4c72135b4dd4deb39b689a2c640aacf09fe44be16e51f341693ce')
pro = ts.pro_api()

df = pro.trade_cal(exchange='',start_date=start,end_date=end)
#print(df)
df.to_csv('./trade_cal.csv')

#print(df.cal_date[0])

