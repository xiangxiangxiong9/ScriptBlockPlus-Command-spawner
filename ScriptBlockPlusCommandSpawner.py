#coding:utf-8
#基础导入
import os
import time
import sys
import re
import codecs
import pyperclip
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import *
import colorama
from colorama import init,Fore,Back,Style
init(autoreset=True)
#语言文件获取
print(sys.executable)
Config = os.getcwd()+'\\config.txt'
#判断文件是否存在
try:
    f =open(Config)
    f.close()
except IOError:
    print("\033[1;31;40mThe File\033[1;32;40m " + Config + ' \033[1;31;40mcannot read')
    print("\033[1;31;40mIs it exist?")
    time.sleep(5)
    sys.exit()
Configfile = open(Config)
print('\033[1;32mConfig File: \033[1;33m' + Config)
for configfound in Configfile.readlines():
    key = "Language:"
    if key in configfound:
        s = re.findall('"TimeSpan":"([\d.]+)"',configfound)
    Configfile.close()
Language = os.getcwd()+'\\languages\\language_'+configfound[9:]+'.txt'
print('\033[1;32mUsing Language File: \033[1;33m' + Language)
#窗口   
window = tk.Tk()
window.geometry('1000x600')
#判断文件是否存在
try:
    f =open(Language)
    f.close()
except IOError:
    print("\033[1;31;40mThe File\033[1;32;40m " + Language + ' \033[1;31;40mcannot read')
    print("\033[1;31;40mIs it exist?")
    print("\033[1;31;40mEdit 'Language:' in file \033[1;32;40m"+Config)
    time.sleep(5)
    sys.exit()
#语言文件读取
#语言文件var设置
actiontype01 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "novalid:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype01.set(LanguageInfo[8:-1])
    LanguageFile.close()

actiontype02 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "$cost:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype02.set(LanguageInfo[6:-1])
    LanguageFile.close()

actiontype03 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "$item:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype03.set(LanguageInfo[6:-1])
    LanguageFile.close()

actiontype04 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@actionbar:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype04.set(LanguageInfo[11:-1])
    LanguageFile.close()

actiontype05 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@amount:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype05.set(LanguageInfo[8:-1])
    LanguageFile.close()

actiontype06 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@blocktype:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype06.set(LanguageInfo[11:-1])
    LanguageFile.close()

actiontype07 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@bypass:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype07.set(LanguageInfo[8:-1])
    LanguageFile.close()

actiontype08 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@calc:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype08.set(LanguageInfo[6:-1])
    LanguageFile.close()

actiontype09 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@command:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype09.set(LanguageInfo[9:-1])
    LanguageFile.close()

actiontype10 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@console:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype10.set(LanguageInfo[9:-1])
    LanguageFile.close()

actiontype11 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@cooldown:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype11.set(LanguageInfo[10:-1])
    LanguageFile.close()

actiontype12 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@delay:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype12.set(LanguageInfo[7:-1])
    LanguageFile.close()

actiontype13 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@execute:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype13.set(LanguageInfo[9:-1])
    LanguageFile.close()

actiontype14 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@group:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype14.set(LanguageInfo[7:-1])
    LanguageFile.close()

actiontype15 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@groupADD:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype15.set(LanguageInfo[10:-1])
    LanguageFile.close()

actiontype16 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@groupREMOVE:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype16.set(LanguageInfo[13:-1])
    LanguageFile.close()

actiontype17 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@hand:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype17.set(LanguageInfo[6:-1])
    LanguageFile.close()

actiontype18 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@oldcooldown:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype18.set(LanguageInfo[13:-1])
    LanguageFile.close()

actiontype19 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@perm:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype19.set(LanguageInfo[6:-1])
    LanguageFile.close()

actiontype20 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@permADD:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype20.set(LanguageInfo[9:-1])
    LanguageFile.close()

actiontype21 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@permREMOVE:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype21.set(LanguageInfo[12:-1])
    LanguageFile.close()

actiontype22 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@player:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype22.set(LanguageInfo[8:-1])
    LanguageFile.close()

actiontype23 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@say:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype23.set(LanguageInfo[5:-1])
    LanguageFile.close()

actiontype24 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@scriptaction:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype24.set(LanguageInfo[14:-1])
    LanguageFile.close()

actiontype25 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@server:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype25.set(LanguageInfo[8:-1])
    LanguageFile.close()

actiontype26 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@sound:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype26.set(LanguageInfo[7:-1])
    LanguageFile.close()

actiontype27 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "@title:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        actiontype27.set(LanguageInfo[7:-1])
    LanguageFile.close()

scripttype01 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "interact:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        scripttype01.set(LanguageInfo[9:-1])
    LanguageFile.close()

scripttype02 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "walk:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        scripttype02.set(LanguageInfo[5:-1])
    LanguageFile.close()

scripttype03 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "break:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        scripttype03.set(LanguageInfo[6:-1])
    LanguageFile.close()

Todo01 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "create:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Todo01.set(LanguageInfo[7:-1])
    LanguageFile.close()

Todo02 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "add:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Todo02.set(LanguageInfo[4:-1])
    LanguageFile.close()

Todo03 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "remove:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Todo03.set(LanguageInfo[7:-1])
    LanguageFile.close()

Button01 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "CheckToAdd:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Button01.set(LanguageInfo[11:-1])
    LanguageFile.close()

Button02 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "ClearTextInput:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Button02.set(LanguageInfo[15:-1])
    LanguageFile.close()

Button03 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "ClearTemp:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Button03.set(LanguageInfo[10:-1])
    LanguageFile.close()

Button04 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "OutPut:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Button04.set(LanguageInfo[7:-1])
    LanguageFile.close()

Information01 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "OutputTitle:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Information01.set(LanguageInfo[12:-1])
    LanguageFile.close()

Information02 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "outputMessage:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Information02.set(LanguageInfo[14:-1])
    LanguageFile.close()

Information03 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "TempText:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Information03.set(LanguageInfo[9:-1])
    LanguageFile.close()

Information04 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "AddSuccess:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Information04.set(LanguageInfo[11:-1])
    LanguageFile.close()
    
Information05 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "AddFailed:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Information05.set(LanguageInfo[10:-1])
    LanguageFile.close()

Information06 = tk.StringVar()
LanguageFile = open(Language,encoding='utf-8')
for LanguageInfo in LanguageFile.readlines():
    key = "WindowTitle:"
    if key in LanguageInfo:
        s = re.findall('"TimeSpan":"([\d.]+)"',LanguageInfo)
        Information06.set(LanguageInfo[12:-1])
    LanguageFile.close()
#部分var设置
var = tk.StringVar()
var1 = tk.StringVar()
var.set('')
choosed = tk.StringVar()
choosed.set('0')
#缓冲区文本
a = tk.Text(window,width=50,height=20)
a.place(x=250,y=310)
#按钮事件
#确认按钮
def Confirm():
    #if套娃函数...
    if var2.get() == actiontype02.get():
        var1.set('$cost:')
        choosed.set('1')
    else:
        if var2.get() == actiontype03.get():
            var1.set('$item:')
            choosed.set('1')
        else:
            if var2.get() == actiontype04.get():
                var1.set('@actionbar:')
                choosed.set('1')
            else:
                if var2.get() == actiontype05.get():
                    var1.set('@amount:')
                    choosed.set('1')
                else:
                    if var2.get() == actiontype06.get():
                        var1.set('@blocktype:')
                        choosed.set('1')
                    else:
                        if var2.get() == actiontype07.get():
                            var1.set('@bypass:')
                            choosed.set('1')
                        else:
                            if var2.get() == actiontype08.get():
                                var1.set('@calc:')
                                choosed.set('1')
                            else:
                                if var2.get() == actiontype09.get():
                                    var1.set('@command:')
                                    choosed.set('1')
                                else:
                                    if var2.get() == actiontype10.get():
                                        var1.set('@console:')
                                        choosed.set('1')
                                    else:
                                        if var2.get() == actiontype11.get():
                                            var1.set('@cooldown:')
                                            choosed.set('1')
                                        else:
                                            if var2.get() == actiontype12.get():
                                                var1.set('@delay:')
                                                choosed.set('1')
                                            else:
                                                if var2.get() == actiontype13.get():
                                                    var1.set('@execute:')
                                                    choosed.set('1')
                                                else:
                                                    if var2.get() == actiontype14.get():
                                                        var1.set('@group:')
                                                        choosed.set('1')
                                                    else:
                                                        if var2.get() == actiontype15.get():
                                                            var1.set('@groupADD:')
                                                            choosed.set('1')
                                                        else:
                                                            if var2.get() == actiontype16.get():
                                                                var1.set('@groupREMOVE:')
                                                                choosed.set('1')
                                                            else:
                                                                if var2.get() == actiontype17.get():
                                                                    var1.set('@hand:')
                                                                    choosed.set('1')
                                                                else:
                                                                    if var2.get() == actiontype18.get():
                                                                        var1.set('@oldcooldown:')
                                                                        choosed.set('1')
                                                                    else:
                                                                        if var2.get() == actiontype19.get():
                                                                            var1.set('@perm:')
                                                                            choosed.set('1')
                                                                        else:
                                                                            if var2.get() == actiontype20.get():
                                                                                var1.set('@permADD:')
                                                                                choosed.set('1')
                                                                            else:
                                                                                if var2.get() == actiontype21.get():
                                                                                    var1.set('@permREMOVE:')
                                                                                    choosed.set('1')
                                                                                else:
                                                                                    if var2.get() == actiontype22.get():
                                                                                        var1.set('@player:')
                                                                                        choosed.set('1')
                                                                                    else:
                                                                                        if var2.get() == actiontype23.get():
                                                                                            var1.set('@say:')
                                                                                            choosed.set('1')
                                                                                        else:
                                                                                            if var2.get() == actiontype24.get():
                                                                                                var1.set('@scriptaction:')
                                                                                                choosed.set('1')
                                                                                            else:
                                                                                                if var2.get() == actiontype25.get():
                                                                                                    var1.set('@server:')
                                                                                                    choosed.set('1')
                                                                                                else:
                                                                                                    if var2.get() == actiontype26.get():
                                                                                                        var1.set('@sound:')
                                                                                                        choosed.set('1')
                                                                                                    else:
                                                                                                        if var2.get() == actiontype27.get():
                                                                                                            var1.set('@title:')
                                                                                                            choosed.set('1')
                                                                                                        else:
                                                                                                            choosed.set('0')
    if choosed.get() == ('1'):
        print(Information04.get())
        var.set(var.get() + '[' + var1.get() + t.get("1.0","end")[:-1] + ']')
    else:
        print(Information05.get())
    a.delete(0.0,"end")
    a.insert("insert", var.get())
#清除缓冲区
def Cleartemp():
    var.set('')
    a.delete(0.0,"end")
#清除输入框
def Clearinput():
    t.delete(0.0,"end")
#添加按钮
ttk.Button(window,text=Button01.get(),command=Confirm).place(x=300,y=265)
#label文本
tk.Label(window,text=Information03.get()).place(x=400,y=289)
#缓冲区清除按钮
ttk.Button(window,text=Button03.get(),command=Cleartemp).place(x=500,y=285)
#文本输入框
t = tk.Text(window,width=50,height=20)
t.place(x=250,y=0)
#清除文本输入框
ttk.Button(window,text=Button02.get(),command=Clearinput).place(x=400,y=265)
#添加类型
var2=StringVar()
var2.set(actiontype01.get())
MENU1 = OptionMenu(window,var2,actiontype01.get(), actiontype02.get(),actiontype03.get(),actiontype04.get(),actiontype05.get(),actiontype06.get(),actiontype07.get(),actiontype08.get(),actiontype09.get(),actiontype10.get(),actiontype11.get(),actiontype12.get(),actiontype13.get(),actiontype14.get(),actiontype15.get(),actiontype16.get(),actiontype17.get(),actiontype18.get(),actiontype19.get(),actiontype20.get(),actiontype21.get(),actiontype22.get(),actiontype23.get(),actiontype24.get(),actiontype25.get(),actiontype26.get(),actiontype27.get()).place(x=0,y=0)
#执行方式
var3=StringVar()
var3.set(scripttype01.get())
var4=StringVar()
MENU2 = OptionMenu(window,var3, scripttype01.get(),scripttype02.get(),scripttype03.get()).place(x=610,y=0)
#添加方式
var5=StringVar()
var5.set(Todo01.get())
MENU2 = OptionMenu(window,var5, Todo01.get(),Todo02.get(),Todo03.get()).place(x=700,y=0)
#输出
def output():
    if var3.get() == scripttype01.get():
        var4.set('interact')
    else:
        if var3.get() == scripttype02.get():
            var4.set('walk')
        else:
           var4.set('break')
    if var5.get() == Todo01.get():
        pyperclip.copy('/sbp ' + var4.get() + ' ' + 'create' +  ' ' + var.get())
    else:
        if var5.get() == Todo02.get():
            pyperclip.copy('/sbp ' + var4.get() + ' ' + 'add' +  ' ' + var.get())
        else:
            pyperclip.copy('/sbp ' + var4.get() + ' ' + 'remove')
    tk.messagebox.showinfo(title=Information01.get(), message=Information02.get())
ttk.Button(window,text=Button04.get(),command=output).place(x=610,y=300)
window.title(Information06.get())
window.mainloop()