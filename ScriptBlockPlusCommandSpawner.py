# coding:utf-8
# 基础导入
import os
import time
import sys
import re
import subprocess
import codecs
import pyperclip
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import *
import colorama
from colorama import init, Fore, Back, Style
init(autoreset=True)
# 语言文件获取
Config = os.getcwd() + '\\config.txt'
# 判断文件是否存在
try:
    f = open(Config, 'r', encoding='utf-8')
    f.close()
except IOError:
    print("\033[1;31;40mConfig file does not exise!Creating!")
    with open(Config, 'w+', encoding='utf-8') as file:
        file.write(
            'please make sure that /language/language_[Language].txt exist\nLanguage:en')
Configfile = open(Config, 'r', encoding='utf-8')
print('\033[1;32mConfig File: \033[1;33m' + Config)
for configfound in Configfile.readlines():
    key = "Language:"
    if key in configfound:
        s = re.findall('"TimeSpan":"([\d.]+)"', configfound)
    Configfile.close()


def WtireTranslateFile(Language):
    if Language == 'en':
        with open('languages/language_en.txt', 'w+', encoding='utf-8') as file:
            file.write(r'''#ActionType
novalid:Please choose
$cost:Need and cost money
$item:Need and cost item[<item's id> [Many]]
@actionbar:Send actionbar information[contect time]
@amount:Total number of allowed executions
@blocktype:Interactive block type [block id]
@bypass:Execute as OP
@calc:Calculate [papi variable> = <value failure_return_information]
@command:Execute as player himself
@console:Execute as Console
@cooldown:cooldown this script block for the player
@delay:delay
@execute:Execute the script block of the specified type and coordinates [type / x y z]
@group:Execute request permission group
@groupADD:Add the player to a permission group
@groupREMOVE:Remove the player to a permission group
@hand:Check item in hand[<item's id> [Many]]
@oldcooldown:cooldown this script block for all players
@perm:Execute request permission
@permADD:Add a permission to the player
@permREMOVE:REMOVE a permission to the player
@player:Send a message to the player
@say:Send Message as the player
@scriptaction:Executive interaction
@server:Unknown role [Cross service?]
@sound:Play a sound for the player
@title:Display title [main_title / subtitle]

#ScriptType
interact:interact
walk:walk
break:break

#Todo
create:create
add:add
remove:remove

#Button
CheckToAdd:Check To Add
ClearTextInput:CLear Text Input
ClearTemp:Clear Temp
OutPut:Output
Restart:Restart

#Information
OutputTitle1:Copy to ClipBoard?
OutputTitle2:Success
OutputMessage:The instructions have been copied to the clipboard\nNote: If the command length is longer than 256, please use the command block and essentials's sudo
TempText:Temp
AddSuccess:Added successfully
AddFailed:Added failed
WindowTitle:ScriptBlockPlus Command Spawmer
RestartMessageboxTitle:Restart?
RestartMessageboxMessage:Do you want to restart this process?Unsaved data will be lost
Restarting:Restarting!
''')
    elif Language == 'zh':
        with open('languages/language_zh.txt', 'w+', encoding='utf-8') as file:
            file.write(r'''#ActionType
novalid:请选择
$cost:需要且消耗钱
$item:需要且消耗物品[<物品id> [数量]]
@actionbar:发送快捷栏信息[内容 时间]
@amount:允许执行的总次数
@blocktype:互动方块类型[方块id]
@bypass:以OP身份执行
@calc:计算[papi变量 >=< 值 失败返回信息]
@command:以玩家自身身份执行
@console:以控制台身份执行
@cooldown:冷却
@delay:延迟
@execute:执行指定类型、坐标的脚本方块[类型/x y z]
@group:执行需要权限组
@groupADD:追加权限组
@groupREMOVE:去除权限组
@hand:检查手里的物品[<方块id> [数量]]
@oldcooldown:全服冷却
@perm:执行需要权限
@permADD:追加权限
@permREMOVE:去除权限
@player:给玩家自己发信息
@say:玩家说话
@scriptaction:执行互动方式
@server:作用不明[跨服?]
@sound:给玩家播放声音
@title:显示标题[主标题/副标题]

#ScriptType
interact:互动
walk:走过
break:破坏

#Todo
create:创建
add:添加
remove:移除

#Button
CheckToAdd:点击添加
ClearTextInput:清空文本输入区
ClearTemp:清空缓冲区
OutPut:输出
Restart:重启

#Information
OutputTitle1:复制到剪切板?
OutputTitle2:成功
OutputMessage:已将指令复制到剪切板\n注意: 如果命令长度长于256，请使用命令块以及essentials的sudo
TempText:缓冲区
AddSuccess:添加成功
AddFailed:添加失败
WindowTitle:ScriptBlockPlus指令生成器
RestartMessageboxTitle:重启？
RestartMessageboxMessage:你想要重启这个程序吗？未保存的数据将会丢失
Restarting:重启中!
''')


# 检查是否有languages文件夹[20201002]
if not os.path.exists('languages'):
    print("\033[1;31;40mLanguages folder does not exise!Creating!")
    os.mkdir('languages')
    print("\033[1;31;40mWtiring language files...")
    print("\033[1;31;40mWtiring English file...[0/2]")
    WtireTranslateFile('en')
    print("\033[1;31;40mWtiring Chinese file...[1/2]")
    WtireTranslateFile('zh')
    print("\033[1;31;40mWrote language files[2/2]")
    print("\033[1;31;40mIf there is no translation for your language, you can create a new file called language_[language]. txt, and then edit \"language\" in config")
Language = os.getcwd() + '\\languages\\language_' + configfound[9:] + '.txt'
try:
    file = open(Language, encoding='utf-8')
    file.close()
except IOError:
    if configfound[9:] == 'en' or configfound[9:] == 'zh':
        print('\033[1;31;40mThe translate for language: ' + configfound[9:] +
              ' may have been deleted...Re creating...')
        WtireTranslateFile(configfound[9:])
    else:
        print('\033[1;31;40mThe translate for language: ' + configfound[9:] +
              ' may not exise...The default language will be used')
        with open(Config, 'w+', encoding='utf-8') as file:
            file.write(
                'please make sure that /language/language_[Language].txt exist\nLanguage:en')
        Language = os.getcwd() + '\\languages\\language_en.txt'
print('\033[1;32mUsing Language File: \033[1;33m' + Language)
# 窗口
try:
    window = tk.Tk()
except:
    print("This program needs a graphical interface")
    sys.exit(0)
window.geometry('1000x600')
# 语言文件读取
#语言文件var设置[更换方式 [20201002]]
with open(Language, encoding='utf-8') as LanguageFile:
    LanguageText = LanguageFile.readlines()
ListOfActionType = ["novalid", "$cost", "$item", "@actionbar", "@amount", "@blocktype", "@bypass", "@calc", "@command", "@console", "@cooldown", "@delay", "@execute",
                    "@group", "@groupADD", "@groupREMOVE", "@hand", "@oldcooldown", "@perm", "@permADD", "@permREMOVE", "@player", "@say", "@scriptaction", "@server", "@sound", "@title"]
ListOfScriptType = ["interact", "walk", "break"]
ListOfTodo = ["create", "add", "remove"]
ListOfButton = ["CheckToAdd", "ClearTextInput",
                "ClearTemp", "OutPut", "Restart"]
ListOfInformation = ["OutputTitle1", "OutputTitle2", "OutputMessage",
                     "TempText", "AddSuccess", "AddFailed", "WindowTitle", "RestartMessageboxTitle", "RestartMessageboxMessage", "Restarting"]
for tmp in LanguageText:
    for i in range(0, len(ListOfActionType)):
        if ListOfActionType[i] == tmp.split(':')[0]:
            temp = ''
            for j in range(1, len(tmp.split(':'))):
                temp = temp + tmp.split(':')[j]
            temp = temp[:-1]
            print(ListOfActionType[i], '=', temp)
            no = str(i + 1)
            if len(no) == 1:
                no = '0' + no
            globals()["ActionType" + no] = temp
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
choosed = tk.StringVar()
choosed.set('0')
# 缓冲区文本
a = tk.Text(window, width=50, height=20)
a.place(x=250, y=310)
# 按钮事件
# 确认按钮


def Confirm():
    # if套娃函数 换 elif [20201002]
    if var2.get() == ActionType02:
        var1.set('$cost:')
        choosed.set('1')
    elif var2.get() == ActionType03:
        var1.set('$item:')
        choosed.set('1')
    elif var2.get() == ActionType04:
        var1.set('@actionbar:')
        choosed.set('1')
    elif var2.get() == ActionType05:
        var1.set('@amount:')
        choosed.set('1')
    elif var2.get() == ActionType06:
        var1.set('@blocktype:')
        choosed.set('1')
    elif var2.get() == ActionType07:
        var1.set('@bypass:')
        choosed.set('1')
    elif var2.get() == ActionType08:
        var1.set('@calc:')
        choosed.set('1')
    elif var2.get() == ActionType09:
        var1.set('@command:')
        choosed.set('1')
    elif var2.get() == ActionType10:
        var1.set('@console:')
        choosed.set('1')
    elif var2.get() == ActionType11:
        var1.set('@cooldown:')
        choosed.set('1')
    elif var2.get() == ActionType12:
        var1.set('@delay:')
        choosed.set('1')
    elif var2.get() == ActionType13:
        var1.set('@execute:')
        choosed.set('1')
    elif var2.get() == ActionType14:
        var1.set('@group:')
        choosed.set('1')
    elif var2.get() == ActionType15:
        var1.set('@groupADD:')
        choosed.set('1')
    elif var2.get() == ActionType16:
        var1.set('@groupREMOVE:')
        choosed.set('1')
    elif var2.get() == ActionType17:
        var1.set('@hand:')
        choosed.set('1')
    elif var2.get() == ActionType18:
        var1.set('@oldcooldown:')
        choosed.set('1')
    elif var2.get() == ActionType19:
        var1.set('@perm:')
        choosed.set('1')
    elif var2.get() == ActionType20:
        var1.set('@permADD:')
        choosed.set('1')
    elif var2.get() == ActionType21:
        var1.set('@permREMOVE:')
        choosed.set('1')
    elif var2.get() == ActionType22:
        var1.set('@player:')
        choosed.set('1')
    elif var2.get() == ActionType23:
        var1.set('@say:')
        choosed.set('1')
    elif var2.get() == ActionType24:
        var1.set('@scriptaction:')
        choosed.set('1')
    elif var2.get() == ActionType25:
        var1.set('@server:')
        choosed.set('1')
    elif var2.get() == ActionType26:
        var1.set('@sound:')
        choosed.set('1')
    elif var2.get() == ActionType27:
        var1.set('@title:')
        choosed.set('1')
    else:
        choosed.set('0')

    if choosed.get() == ('1'):
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
var2.set(ActionType01)
MENU1 = OptionMenu(window, var2, ActionType01, ActionType02, ActionType03, ActionType04, ActionType05, ActionType06, ActionType07, ActionType08, ActionType09, ActionType10, ActionType11, ActionType12, ActionType13,
                   ActionType14, ActionType15, ActionType16, ActionType17, ActionType18, ActionType19, ActionType20, ActionType21, ActionType22, ActionType23, ActionType24, ActionType25, ActionType26, ActionType27).place(x=0, y=0)
# 执行方式
var3 = StringVar()
var3.set(ScriptType01)
var4 = StringVar()
MENU2 = OptionMenu(window, var3, ScriptType01, ScriptType02,
                   ScriptType03).place(x=610, y=0)
# 添加方式
var5 = StringVar()
var5.set(Todo01)
MENU3 = OptionMenu(window, var5, Todo01, Todo02, Todo03).place(x=700, y=0)
# 输出


def output():
    if var3.get() == ScriptType01:
        var4.set('interact')
    else:
        if var3.get() == ScriptType02:
            var4.set('walk')
        else:
            var4.set('break')
    # 将else if 替换为 elif [20201002]
    '''if var5.get() == Todo01:
        pyperclip.copy('/sbp ' + var4.get() + ' ' + 'create' +  ' ' + var.get())
    elif var5.get() == Todo02:
        pyperclip.copy('/sbp ' + var4.get() + ' ' + 'add' +  ' ' + var.get())
    else:
        pyperclip.copy('/sbp ' + var4.get() + ' ' + 'remove')
    #tk.messagebox.showinfo(title=Information02, message=Information03)'''
    # 先询问再复制到剪切板[20201002]
    if tk.messagebox.askyesno(title=Information01, message='/sbp ' + var4.get() + ' ' + 'create' + ' ' + var.get()):
        if var5.get() == Todo01:
            pyperclip.copy('/sbp ' + var4.get() + ' ' +
                           'create' + ' ' + var.get())
        elif var5.get() == Todo02:
            pyperclip.copy('/sbp ' + var4.get() + ' ' +
                           'add' + ' ' + var.get())
        else:
            pyperclip.copy('/sbp ' + var4.get() + ' ' + 'remove')
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
