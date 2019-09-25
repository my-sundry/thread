#!/usr/bin/python
# -*- coding:utf-8 -*-

import threading
import datetime
import sys
import inspect
import ctypes

class A:
    count = 0
    shutdown_signal = True
    def fun2(self):
        global count
        global shutdown_signal
        if self.shutdown_signal:
            if self.count < 5:
                print('线程2执行!')
                global timer1
                timer1 = threading.Timer(5,self.fun2)
                timer1.start()
                self.count += 1
            else:
                self.shutdown_signal = False
                self.timer1.cancel()
        else:
            self.timer1.cancel()

    def fun_timer(self):
        now = datetime.datetime.now().strftime('%H:%M')
        global shutdown_signal
        if self.shutdown_signal:
            if now < '17:01':
                print('线程1执行!')
                global timer
                timer = threading.Timer(10,self.fun_timer)
                timer.start()
                #print(timer.isAlive())
            else:
                #self.terminator(self.timer1)
                self.shutdown_signal = False
                self.timer.cancel()
        else:
            self.timer.cancel()
    
    def __async_raise(self,thread_Id,exctype):
        thread_Id = ctypes.c_long(thread_Id)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_Id,ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_Id,None)
            raise SystemError("PyThreadState_SEtAsyncExc failed")

    def terminator(self,thread):
        self.__async_raise(thread.ident, SystemExit)

if __name__ == '__main__'
    a = A()
    a.timer = threading.Timer(1,a.fun_timer)
    a.timer.start()
    a.timer1 = threading.Timer(2,a.fun2)
    a.timer1.start()
