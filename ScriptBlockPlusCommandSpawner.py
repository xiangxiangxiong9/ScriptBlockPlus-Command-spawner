# coding:utf-8
# 基础导入
import os
import time
import sys
import re
import gc
import urllib.request
# import socket
# socket.setdefaulttimeout(20)
#import retrying
import subprocess
import codecs
import locale
import pyperclip
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import *
import colorama
from colorama import init, Fore, Back, Style


init(autoreset=True)
tmp = locale.getdefaultlocale()[0]
del locale
locale = tmp
del tmp
gc.collect()
# 语言文件获取
Config = os.getcwd() + '\\config.txt'
# 判断文件是否存在
try:
    f = open(Config, 'r', encoding='utf-8')
    f.close()
except IOError:
    print("\033[1;31mConfig file does not exise!Creating!")
    with open(Config, 'w+', encoding='utf-8') as file:
        file.write(
            'Please make sure that /language/Language-[Language].txt exist\nDefault Language is: en_US\nSuppose Locales: en_US,ja[ja_JP],zh_CN\nLanguage:en_US')
Configfile = open(Config, 'r', encoding='utf-8')
print('\033[1;32mConfig File: \033[1;33m' + Config)
for configfound in Configfile.readlines():
    key = "Language:"
    if key in configfound:
        s = re.findall('"TimeSpan":"([\d.]+)"', configfound)
    Configfile.close()


#@retrying.retry(stop_max_attempt_number=3)
def getLanguageFile(Language):
    print('\033[1;32mTry to get Language: ' +
          Language + ' on GitHub...\033[0m')
    try:
        a = urllib.request.urlopen(
            'https://github.com/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Language-' + Language + '.txt')
        if a.status == 404:
            a.close()
            return 404
        elif a.status == 200:
            with open('languages/language-' + Language + '.txt', 'w+', encoding='utf-8') as file:
                file.write(a.read().decode('utf-8'))
                a.close()
            return 0
        else:
            a.close()
            return 1
    except:
        print('\033[1;31mGet file on GitHub failed...\n\033[1;32mTry to get Language: ' +
              Language + ' on FastGit...\033[0m')
        try:
            b = urllib.request.urlopen(
                'https://hub.fastgit.org/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Language-' + Language + '.txt')
            if b.status == 404:
                b.close()
                return 404
            elif b.status == 200:
                with open('languages/language-' + Language + '.txt', 'w+', encoding='utf-8') as file:
                    file.write(b.read().decode('utf-8'))
                    b.close()
                return 0
            else:
                b.close()
                return 1
        except:
            print('\033[1;31mGet file on FastGit failed...\n\033[1;32mTry to get Language: ' +
                  Language + ' on Gitee...\033[0m')
            try:
                b = urllib.request.urlopen(
                    'https://gitee.com/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Language-' + Language + '.txt')
                if b.status == 404:
                    b.close()
                    return 404
                elif b.status == 200:
                    with open('languages/language-' + Language + '.txt', 'w+', encoding='utf-8') as file:
                        file.write(b.read().decode('utf-8'))
                        b.close()
                    return 0
                else:
                    b.close()
                    return 1
            except:
                return 2


Configfile = open(Config, 'r', encoding='utf-8')
for configfound in Configfile.readlines():
    key = "Language:"
    if key in configfound:
        s = re.findall('"TimeSpan":"([\d.]+)"', configfound)
    Configfile.close()
Language = os.getcwd() + '\\languages\\Language-' + \
    configfound.split(':')[1].replace(' ', '') + '.txt'
if not os.path.isfile(Language):
    if not os.path.exists('languages'):
        print("\033[1;31mLanguages folder does not exise!Creating!")
        os.mkdir('languages')
    languagewtire = getLanguageFile(configfound.split(':')[1].replace(' ', ''))
    if languagewtire == 0:
        pass
    elif languagewtire == 1:
        print('\033[1;31mThere may be something wrong with your network,we cannot get files on the server.Please try again.\033[0m')
        sys.exit(1)
    elif languagewtire == 404:
        print('\033[1;31mThe translate for language: ' + locale +
              ' may not exise...The default language will be used\033[0m')
        getLanguageFile('en_US')
        with open(Config, 'w+', encoding='utf-8') as file:
            file.write(
                'Please make sure that /language/Language-[Language].txt exist\nDefault Language is: en_US\nSuppose Locales: en_US,ja[ja_JP],zh_CN\nLanguage:en_US')

print('\033[1;32mUsing Language File: \033[1;33m' + Language)
# 窗口
try:
    window = tk.Tk()
except:
    print("This program needs a graphical interface")
    sys.exit(0)
window.geometry('1000x600')
# 语言文件读取
# 语言文件var设置[更换方式 [20201002]]
with open(Language, encoding='utf-8') as LanguageFile:
    LanguageText = LanguageFile.readlines()
ListOfActionType = ["!novalid", "$cost", "$item", "@actionbar", "@amount", "@blocktype", "@bypass", "@bypassGROUP", "@bypassPERM", "@calc", "@command", "@console", "@cooldown", "@delay", "@execute",
                    "@group", "@groupADD", "@groupREMOVE", "@hand", "@oldcooldown", "@perm", "@permADD", "@permREMOVE", "@player", "@say", "@scriptaction", "@server", "@sound", "@title"]
ListOfScriptType = ["interact", "walk", "break"]
ListOfTodo = ["create", "add", "remove"]
ListOfButton = ["CheckToAdd", "ClearTextInput",
                "ClearTemp", "OutPut", "Restart"]
ListOfInformation = ["OutputTitle1", "OutputTitle2", "OutputMessage",
                     "TempText", "AddSuccess", "AddFailed", "WindowTitle", "RestartMessageboxTitle", "RestartMessageboxMessage", "Restarting"]

ActionType = []
for i in ListOfActionType:
    ActionType.append(i[1:])

for tmp in LanguageText:
    for i in range(0, len(ListOfActionType)):
        if ListOfActionType[i] == tmp.split(':')[0]:
            temp = ''
            for j in range(1, len(tmp.split(':'))):
                temp = temp + tmp.split(':')[j]
            temp = temp[:-1]
            print(ListOfActionType[i][1:], '=', temp)
            # no = str(i + 1)
            # if len(no) == 1:
            #     no = '0' + no
            globals()[ActionType[i]] = temp
    for i in range(0, len(ListOfScriptType)):
        if ListOfScriptType[i] == tmp.split(':')[0]:
            temp = ''
            for j in range(1, len(tmp.split(':'))):
                temp = temp + tmp.split(':')[j]
            temp = temp[:-1]
            print(ListOfScriptType[i], '=', temp)
            no = str(i + 1)
            if len(no) == 1:
                no = '0' + no
            globals()["ScriptType" + no] = temp
    for i in range(0, len(ListOfTodo)):
        if ListOfTodo[i] == tmp.split(':')[0]:
            temp = ''
            for j in range(1, len(tmp.split(':'))):
                temp = temp + tmp.split(':')[j]
            temp = temp[:-1]
            print(ListOfTodo[i], '=', temp)
            no = str(i + 1)
            if len(no) == 1:
                no = '0' + no
            globals()["Todo" + no] = temp
    for i in range(0, len(ListOfButton)):
        if ListOfButton[i] == tmp.split(':')[0]:
            temp = ''
            for j in range(1, len(tmp.split(':'))):
                temp = temp + tmp.split(':')[j]
            temp = temp[:-1]
            print(ListOfButton[i], '=', temp)
            no = str(i + 1)
            if len(no) == 1:
                no = '0' + no
            globals()["Button" + no] = temp
    for i in range(0, len(ListOfInformation)):
        if ListOfInformation[i] == tmp.split(':')[0]:
            temp = ''
            for j in range(1, len(tmp.split(':'))):
                temp = temp + tmp.split(':')[j]
            temp = temp[:-1]
            print(ListOfInformation[i], '=', temp)
            no = str(i + 1)
            if len(no) == 1:
                no = '0' + no
            globals()["Information" + no] = temp


# 部分var设置
var = tk.StringVar()
var1 = tk.StringVar()
var.set('')
choosed = tk.BooleanVar()
choosed.set(False)
# 缓冲区文本
a = tk.Text(window, width=50, height=20)
a.place(x=250, y=310)
# 按钮事件
# 确认按钮


def Confirm():
    # if套娃函数 换 elif [20201002]
    # if var2.get() == ActionType02:
    #     var1.set('$cost:')
    #     choosed.set('1')
    # elif var2.get() == ActionType03:
    #     var1.set('$item:')
    #     choosed.set('1')
    # elif var2.get() == ActionType04:
    #     var1.set('@actionbar:')
    #     choosed.set('1')
    # elif var2.get() == ActionType05:
    #     var1.set('@amount:')
    #     choosed.set('1')
    # elif var2.get() == ActionType06:
    #     var1.set('@blocktype:')
    #     choosed.set('1')
    # elif var2.get() == ActionType07:
    #     var1.set('@bypass:')
    #     choosed.set('1')
    # elif var2.get() == ActionType08:
    #     var1.set('@calc:')
    #     choosed.set('1')
    # elif var2.get() == ActionType09:
    #     var1.set('@command:')
    #     choosed.set('1')
    # elif var2.get() == ActionType10:
    #     var1.set('@console:')
    #     choosed.set('1')
    # elif var2.get() == ActionType11:
    #     var1.set('@cooldown:')
    #     choosed.set('1')
    # elif var2.get() == ActionType12:
    #     var1.set('@delay:')
    #     choosed.set('1')
    # elif var2.get() == ActionType13:
    #     var1.set('@execute:')
    #     choosed.set('1')
    # elif var2.get() == ActionType14:
    #     var1.set('@group:')
    #     choosed.set('1')
    # elif var2.get() == ActionType15:
    #     var1.set('@groupADD:')
    #     choosed.set('1')
    # elif var2.get() == ActionType16:
    #     var1.set('@groupREMOVE:')
    #     choosed.set('1')
    # elif var2.get() == ActionType17:
    #     var1.set('@hand:')
    #     choosed.set('1')
    # elif var2.get() == ActionType18:
    #     var1.set('@oldcooldown:')
    #     choosed.set('1')
    # elif var2.get() == ActionType19:
    #     var1.set('@perm:')
    #     choosed.set('1')
    # elif var2.get() == ActionType20:
    #     var1.set('@permADD:')
    #     choosed.set('1')
    # elif var2.get() == ActionType21:
    #     var1.set('@permREMOVE:')
    #     choosed.set('1')
    # elif var2.get() == ActionType22:
    #     var1.set('@player:')
    #     choosed.set('1')
    # elif var2.get() == ActionType23:
    #     var1.set('@say:')
    #     choosed.set('1')
    # elif var2.get() == ActionType24:
    #     var1.set('@scriptaction:')
    #     choosed.set('1')
    # elif var2.get() == ActionType25:
    #     var1.set('@server:')
    #     choosed.set('1')
    # elif var2.get() == ActionType26:
    #     var1.set('@sound:')
    #     choosed.set('1')
    # elif var2.get() == ActionType27:
    #     var1.set('@title:')
    #     choosed.set('1')
    # else:
    #     choosed.set('0')
    if var2.get() != globals()[ActionType[0]]:
        print(var2.get())
        for i in getscript():
            if var2.get() == i:
                for j in range(len(ActionType)):
                    try:
                        if globals()[ActionType[j]] == var2.get():
                            var1.set(ListOfActionType[j] + ' ')
                            choosed.set(True)
                            break
                    except KeyError as err:
                        print('找不到 %s' % err)
    else:
        choosed.set(False)

    if choosed.get():
        print(Information05)
        var.set(var.get() + '[' + var1.get() + t.get("1.0", "end")[:-1] + ']')
    else:
        print(Information06)
    a.delete(0.0, "end")
    a.insert("insert", var.get())
# 清除缓冲区


def Cleartemp():
    var.set('')
    a.delete(0.0, "end")
# 清除输入框


def Clearinput():
    t.delete(0.0, "end")


def getscript():
    resule = []
    for i in range(len(ActionType)):
        try:
            resule.append(globals()[ActionType[i]])
        except KeyError as err:
            pass
    return resule


# 添加按钮
ttk.Button(window, text=Button01, command=Confirm).place(x=300, y=265)
# label文本
tk.Label(window, text=Information04).place(x=400, y=289)
# 缓冲区清除按钮
ttk.Button(window, text=Button03, command=Cleartemp).place(x=500, y=285)
# 文本输入框
t = tk.Text(window, width=50, height=20)
t.place(x=250, y=0)
# 清除文本输入框
ttk.Button(window, text=Button02, command=Clearinput).place(x=400, y=265)
# 添加类型
var2 = StringVar()
var2.set(novalid)
MENU1 = OptionMenu(window, var2, *getscript()).place(x=0, y=0)
# 执行方式
var3 = StringVar()
var3.set(ScriptType01)
var4 = StringVar()
MENU2 = OptionMenu(window, var3, ScriptType01, ScriptType02,
                   ScriptType03).place(x=610, y=0)
# 添加方式
var5 = StringVar()
var5.set(Todo01)
var6 = StringVar()
MENU3 = OptionMenu(window, var5, Todo01, Todo02, Todo03).place(x=700, y=0)
# 输出


def output():
    if var3.get() == ScriptType01:
        var4.set('interact')
    elif var3.get() == ScriptType02:
        var4.set('walk')
    else:
        var4.set('break')
    if var5.get() == Todo01:
        var6.set('create')
    elif var5.get() == Todo02:
        var6.set('add')
    else:
        var6.set('remove')
    # 将else if 替换为 elif [20201002]
    '''if var5.get() == Todo01:
        pyperclip.copy('/sbp ' + var4.get() + ' ' + \
                       'create' +  ' ' + var.get())
    elif var5.get() == Todo02:
        pyperclip.copy('/sbp ' + var4.get() + ' ' + 'add' +  ' ' + var.get())
    else:
        pyperclip.copy('/sbp ' + var4.get() + ' ' + 'remove')
    # tk.messagebox.showinfo(title=Information02, message=Information03)'''
    # 先询问再复制到剪切板[20201002]
    if var6.get() != 'remove':
        if tk.messagebox.askyesno(title=Information01, message='/sbp ' + var4.get() + ' ' + var6.get() + ' ' + var.get()):
            pyperclip.copy('/sbp ' + var4.get() + ' ' +
                           var6.get() + ' ' + var.get())
            tk.messagebox.showinfo(title=Information02, message=Information03)
    elif tk.messagebox.askyesno(title=Information01, message='/sbp ' + var4.get() + ' ' + var6.get()):
        pyperclip.copy('/sbp ' + var4.get() + ' ' + var6.get())
        tk.messagebox.showinfo(title=Information02, message=Information03)


#
ttk.Button(window, text=Button04, command=output).place(x=610, y=300)
# 重启


def restart():
    if tk.messagebox.askyesno(title=Information08, message=Information09):
        print(Information10)
        commandline = sys.executable
        if ' ' in commandline:
            commandline = '"' + commandline + '"'
        for temp in sys.argv:
            commandline = commandline + ' ' + temp
        print(commandline)
        subprocess.Popen(commandline)
        sys.exit()


ttk.Button(window, text=Button05, command=restart).place(x=610, y=500)
window.title(Information07)
window.mainloop()
