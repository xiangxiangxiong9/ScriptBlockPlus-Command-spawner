#coding:utf-8
#基础导入
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
import pyperclip
#窗口
window = tk.Tk()
window.title('ScriptBlockPlus指令生成器')
window.geometry('1000x600')
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
    if var2.get() == '需要且消耗钱':
        var1.set('$cost:')
        choosed.set('1')
    else:
        if var2.get() == '需要且消耗物品[<方块id> [数量]]':
            var1.set('$item:')
            choosed.set('1')
        else:
            if var2.get() == '发送快捷栏信息[内容 时间]':
                var1.set('@actionbar:')
                choosed.set('1')
            else:
                if var2.get() == '允许执行的总次数':
                    var1.set('@amount:')
                    choosed.set('1')
                else:
                    if var2.get() == '交互方块类型[方块id]':
                        var1.set('@blocktype:')
                        choosed.set('1')
                    else:
                        if var2.get() == '以管理员身份执行':
                            var1.set('@bypass:')
                            choosed.set('1')
                        else:
                            if var2.get() == '计算[papi变量 >=< 值 失败返回信息]':
                                var1.set('@calc:')
                                choosed.set('1')
                            else:
                                if var2.get() == '以玩家自身身份执行':
                                    var1.set('@command:')
                                    choosed.set('1')
                                else:
                                    if var2.get() == '以管理员身份执行':
                                        var1.set('@console:')
                                        choosed.set('1')
                                    else:
                                        if var2.get() == '冷却':
                                            var1.set('@cooldown:')
                                            choosed.set('1')
                                        else:
                                            if var2.get() == '延迟':
                                                var1.set('@delay:')
                                                choosed.set('1')
                                            else:
                                                if var2.get() == '执行指定类型、坐标的脚本方块[类型/world x y z]':
                                                    var1.set('@execute:')
                                                    choosed.set('1')
                                                else:
                                                    if var2.get() == '执行需要权限组':
                                                        var1.set('@group:')
                                                        choosed.set('1')
                                                    else:
                                                        if var2.get() == '追加权限组':
                                                            var1.set('@groupADD:')
                                                            choosed.set('1')
                                                        else:
                                                            if var2.get() == '去除权限组':
                                                                var1.set('@groupREMOVE:')
                                                                choosed.set('1')
                                                            else:
                                                                if var2.get() == '检查手里的物品[<方块id> [数量]]':
                                                                    var1.set('@hand:')
                                                                    choosed.set('1')
                                                                else:
                                                                    if var2.get() == '全服冷却':
                                                                        var1.set('@oldcooldown:')
                                                                        choosed.set('1')
                                                                    else:
                                                                        if var2.get() == '执行需要权限':
                                                                            var1.set('@perm:')
                                                                            choosed.set('1')
                                                                        else:
                                                                            if var2.get() == '追加权限':
                                                                                var1.set('@permADD:')
                                                                                choosed.set('1')
                                                                            else:
                                                                                if var2.get() == '去除权限':
                                                                                    var1.set('@permREMOVE:')
                                                                                    choosed.set('1')
                                                                                else:
                                                                                    if var2.get() == '给玩家自己发送信息':
                                                                                        var1.set('@player:')
                                                                                        choosed.set('1')
                                                                                    else:
                                                                                        if var2.get() == '玩家说话':
                                                                                            var1.set('@say:')
                                                                                            choosed.set('1')
                                                                                        else:
                                                                                            if var2.get() == '执行互动方式':
                                                                                                var1.set('@scriptaction:')
                                                                                                choosed.set('1')
                                                                                            else:
                                                                                                if var2.get() == '作用不明':
                                                                                                    var1.set('@server:')
                                                                                                    choosed.set('1')
                                                                                                else:
                                                                                                    if var2.get() == '给玩家播放声音':
                                                                                                        var1.set('@sound:')
                                                                                                        choosed.set('1')
                                                                                                    else:
                                                                                                        if var2.get() == '显示标题[主标题/副标题]':
                                                                                                            var1.set('@title:')
                                                                                                            choosed.set('1')
                                                                                                        else:
                                                                                                            choosed.set('0')
    if choosed.get() == ('1'):
        print("添加成功")
        var.set(var.get() + '[' + var1.get() + t.get("1.0","end")[:-1] + ']')
    else:
        print('添加失败')
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
ttk.Button(window,text='点击添加',command=Confirm).place(x=300,y=265)
#label文本
tk.Label(window,text='缓冲区').place(x=400,y=289)
#缓冲区清除按钮
ttk.Button(window,text='清除缓冲区',command=Cleartemp).place(x=500,y=285)
#文本输入框
t = tk.Text(window,width=50,height=20)
t.place(x=250,y=0)
#清除文本输入框
ttk.Button(window,text='清除文本输入区',command=Clearinput).place(x=400,y=265)
#添加类型
var2=StringVar()
var2.set('请选择')
MENU1 = OptionMenu(window,var2,'请选择', '需要且消耗钱','需要且消耗物品[<方块id> [数量]]','发送快捷栏信息[内容 时间]','允许执行的总次数','交互方块类型[方块id]','以管理员身份执行','计算[papi变量 >=< 值 失败返回信息]','以玩家自身身份执行','以控制台身份执行','冷却','延迟','执行指定类型、坐标的脚本方块[类型/world x y z]','执行需要权限组','追加权限组','去除权限组','检查手里的物品[<方块id> [数量]]','全服冷却','执行需要权限','追加权限','去除权限','给玩家自己发送信息','玩家说话','执行互动方式','作用不明','给玩家播放声音','显示标题[主标题/副标题]').place(x=0,y=0)
#执行方式
var3=StringVar()
var3.set('互动')
var4=StringVar()
MENU2 = OptionMenu(window,var3, '互动','走过','挖掘').place(x=610,y=0)
#添加方式
var5=StringVar()
var5.set('新建')
var6=StringVar()
MENU2 = OptionMenu(window,var5, '新建','添加').place(x=700,y=0)
#输出
def output():
    if var3.get() == '互动':
        var4.set('interact')
    else:
        if var3.get() == '走过':
            var4.set('walk')
        else:
           var4.set('break')
    if var5.get() == '新建':
        var6.set('create')
    else:
        var6.set('add')
    pyperclip.copy('/sbp ' + var4.get() + ' ' + var6.get() +  ' ' + var.get())
    tk.messagebox.showinfo(title='成功' , message='已将指令复制到剪切板\n注意: 如果长度高于256，请使用命令块以及essentials的sudo')
ttk.Button(window,text='输出',command=output).place(x=610,y=300)
window.mainloop()