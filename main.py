#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
    Author： 
    Date:    2019-09-25
'''

import threading
import datetime
import sys
import pandas as pd
import tushare as ts

today = int(datetime.date.today().strftime('%Y%m%d'))
df = pd.read_csv('./trade_cal.csv')
df = df[df['cal_date'] == today]
is_open = df['is_open'].tolist()[0]

class Thread:
    shutdown_signal = True   #退出程序信号
    def __init__(self,code,high,low):
        self.stock_code = code
        self.high_price_limit = high
        self.low_price_limit = low

    def price_monitoring(self):
        global shutdown_signal
        realtime_price = self.get_price()
        if self.shutdown_signal:
            if realtime_price > self.high_price_limit or realtime_price <self.low_price_limit:
                self.send_mail()
                self.shutdown_signal = False
                self.timer1.cancel()
            else:
                #print(realtime_price)
                global timer1
                timer1 = threading.Timer(5,self.price_monitoring)
                timer1.start()
        else:
            self.timer1.cancel()

    def time_control(self):
        now = datetime.datetime.now().strftime('%H:%M')
        global shutdown_signal
        if self.shutdown_signal:
            if now < '15:31':
                #print('线程1执行!')
                global timer
                timer = threading.Timer(10,self.time_control)
                timer.start()
            else:
                self.shutdown_signal = False
                self.timer.cancel()
        else:
            self.timer.cancel()
    
    def get_price(self):
        df = ts.get_realtime_quotes(self.stock_code)
        price = float(df['b1_p'].tolist()[0])
        return price

    def send_mail(self):
        print('sendmail')

if __name__ == '__main__':
    if is_open:
        thread = Thread('511900',100.03,99.97)
        thread.timer = threading.Timer(1,thread.time_control)
        thread.timer.start()
        thread.timer1 = threading.Timer(2,thread.price_monitoring)
        thread.timer1.start()
    else:
        exit(1)
