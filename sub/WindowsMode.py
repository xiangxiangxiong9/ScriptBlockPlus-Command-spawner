import pyperclip
import subprocess
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox
from tkinter import *


def windows(name_value='', name='', ActionType='', getscript='', ListOfActionType=''):
    for a in range(len(name)):
        if 'novalid' in name[a]:
            start = a
    for i in name[start:]:
        #print(i)
        #print(name_value[i])
        globals()[i] = name_value[i]
    try:
        window = tk.Tk()
    except:
        CommandMode = True
        return 1
    window.geometry('1000x600')
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
            for i in getscript:
                if var2.get() == i:
                    for j in range(len(ActionType)):
                        try:
                            if globals()[ActionType[j]] == var2.get():
                                var1.set(ListOfActionType[j] + ' ')
                                choosed.set(True)
                                break
                        except KeyError as err:
                            # print('找不到 %s' % err)
                            pass
        else:
            choosed.set(False)

        if choosed.get():
            print(Information05)
            var.set(var.get() + '[' + var1.get() +
                    t.get("1.0", "end")[:-1] + ']')
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
    var2.set(novalid)
    MENU1 = OptionMenu(window, var2, *getscript).place(x=0, y=0)
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
            pyperclip.copy('/sbp ' + var4.get() + ' ' + \
                           'add' +  ' ' + var.get())
        else:
            pyperclip.copy('/sbp ' + var4.get() + ' ' + 'remove')
        # tk.messagebox.showinfo(title=Information02, message=Information03)'''
        # 先询问再复制到剪切板[20201002]
        if var6.get() != 'remove':
            if tk.messagebox.askyesno(title=Information01, message='/sbp ' + var4.get() + ' ' + var6.get() + ' ' + var.get()):
                pyperclip.copy('/sbp ' + var4.get() + ' ' +
                               var6.get() + ' ' + var.get())
                tk.messagebox.showinfo(
                    title=Information02, message=Information03)
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
