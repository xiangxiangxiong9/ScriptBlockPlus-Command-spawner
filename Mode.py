def WindowsMode(LanguageText):
    ActionType = list(LanguageText['ActionType'].keys())
    ActionTypeValues = list(LanguageText['ActionType'].values())
    ScriptType = list(LanguageText['ScriptType'].keys())
    ScriptTypeValues = list(LanguageText['ScriptType'].values())
    Todo = list(LanguageText['Todo'].keys())
    TodoValues = list(LanguageText['Todo'].values())
    Button = list(LanguageText['Button'].values())
    Information = list(LanguageText['Information'].values())
    
    
    import pyperclip
    import subprocess
    import tkinter as tk
    import tkinter.ttk as ttk
    import tkinter.messagebox
    import sys
    #from tkinter import *
    
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
        if var2.get() != ActionTypeValues[0]:
            print(var2.get())
            for i in range(len(ActionTypeValues)):
                if var2.get() == ActionTypeValues[i]:
                    var1.set(ActionType[i])
                    choosed.set(True)
        else:
            choosed.set(False)

        if choosed.get():
            print(Information[4])
            var.set(var.get() + '[' + var1.get() + ' ' + t.get("1.0", "end")[:-1] + ']')
        else:
            print(Information[3])
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
    ttk.Button(window, text=Button[0], command=Confirm).place(x=300, y=265)
    # label文本
    tk.Label(window, text=Information[3]).place(x=400, y=289)
    # 缓冲区清除按钮
    ttk.Button(window, text=Button[2],
               command=Cleartemp).place(x=500, y=285)
    # 文本输入框
    t = tk.Text(window, width=50, height=20)
    t.place(x=250, y=0)
    # 清除文本输入框
    ttk.Button(window, text=Button[1],
               command=Clearinput).place(x=400, y=265)
    # 添加类型
    var2 = tk.StringVar()
    var2.set(ActionTypeValues[0])
    MENU1 = tk.OptionMenu(window, var2, *ActionTypeValues).place(x=0, y=0)
    # 执行方式
    var3 = tk.StringVar()
    var3.set(ScriptTypeValues[0])
    var4 = tk.StringVar()
    MENU2 = tk.OptionMenu(window, var3, *ScriptTypeValues).place(x=610, y=0)
    # 添加方式
    var5 = tk.StringVar()
    var5.set(TodoValues[0])
    var6 = tk.StringVar()
    MENU3 = tk.OptionMenu(window, var5, *TodoValues).place(x=700, y=0)
    # 输出

    def output():
        for i in range(len(ScriptTypeValues)):
            if var3.get() == ScriptTypeValues[i]:
               var4.set(ScriptType[i]) 

        for i in range(len(TodoValues)):
            if var5.get() == TodoValues[i]:
               var6.set(Todo[i]) 
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
            if tk.messagebox.askyesno(title=Information[0], message='/sbp ' + var4.get() + ' ' + var6.get() + ' ' + var.get()):
                pyperclip.copy('/sbp ' + var4.get() + ' ' +
                               var6.get() + ' ' + var.get())
                tk.messagebox.showinfo(
                    title=Information[1], message=Information[2])
        elif tk.messagebox.askyesno(title=Information[0], message='/sbp ' + var4.get() + ' ' + var6.get()):
            pyperclip.copy('/sbp ' + var4.get() + ' ' + var6.get())
            tk.messagebox.showinfo(
                title=Information[1], message=Information[2])

    #
    ttk.Button(window, text=Button[3], command=output).place(x=610, y=300)
    # 重启

    def restart():
        if tk.messagebox.askyesno(title=Information[7], message=Information[8]):
            print(Information[9])
            commandline = sys.executable
            if ' ' in commandline:
                commandline = '"' + commandline + '"'
            for temp in sys.argv:
                commandline = commandline + ' ' + temp
            print(commandline)
            subprocess.Popen(commandline)
            sys.exit()

    ttk.Button(window, text=Button[4], command=restart).place(x=610, y=500)
    window.title(Information[6])
    window.mainloop()

def CommandMode(name_value='', name='', ActionType='', getscript='', ListOfActionType=''):
    import pyperclip
    import sys
    import os
    ActionType = list(LanguageText['ActionType'].keys())
    ActionTypeValues = list(LanguageText['ActionType'].values())
    ScriptType = list(LanguageText['ScriptType'].keys())
    ScriptTypeValues = list(LanguageText['ScriptType'].values())
    Todo = list(LanguageText['Todo'].keys())
    TodoValues = list(LanguageText['Todo'].values())
    Button = list(LanguageText['Button'].values())
    Information = list(LanguageText['Information'].values())

    data = ''
    while True:
        for i in range(len(ActionType[1:])):
            try:
                print(str(i) + ': ' + ActionTypeValues[i])
            except KeyError:
                pass
        if len(data) == 0:
            print("Please enter action code or exit for close this process")
        else:
            print(
                "Please enter action code or output to output command or clear for clear cache or exit for close this process")
        inputcode = input()
        print('Your input:' + inputcode)
        if inputcode == 'exit':
            import sys
            break
            sys.exit(0)
        elif inputcode == 'clear':
            data = ''
            continue
        elif inputcode == 'output':
            if not len(data) == 0:
                while True:
                    print(
                        'Please input how to trigger the script\n1: interact\n2: walk\n3: break\n4: hit')
                    tmp2 = input()
                    print('Your input:' + inputcode)
                    if tmp2 != '1' or tmp2 != '2' or tmp2 != '3' or tmp2 != '4':
                        break
                while True:
                    print(
                        'Please input what do you want to do\n1: create\n2: add\n3: remove')
                    tmp3 = input()
                    print('Your input:' + inputcode)
                    if tmp2 != '1' or tmp2 != '2' or tmp2 != '3':
                        break
                print(
                    'The command has been copied to the clipboard. Thanks for using it')
                if not tmp3 == '3':
                    if tmp2 == '1':
                        tmp2 = 'interact'
                    elif tmp2 == '2':
                        tmp2 = 'walk'
                    elif tmp2 == '3':
                        tmp2 = 'break'
                    else:
                        tmp2 = 'hit'
                    if tmp3 == '1':
                        tmp3 = 'create'
                    else:
                        tmp3 = 'add'
                    print('Command: ' + '/sbp ' +
                          tmp2 + ' ' + tmp3 + ' ' + data)
                    pyperclip.copy('/sbp ' + tmp2 + ' ' +
                                   tmp3 + ' ' + data)
                    os.system('pause')
                else:
                    if tmp2 == '1':
                        tmp2 = 'interact'
                    elif tmp2 == '2':
                        tmp2 = 'walk'
                    elif tmp2 == '3':
                        tmp2 = 'break'
                    else:
                        tmp2 = 'hit'
                    tmp3 = 'remove'
                    print('Command: ' + '/sbp ' +
                          tmp2 + ' ' + tmp3 + ' ' + data)
                    pyperclip.copy('/sbp ' + tmp2 + ' ' + tmp3)
                    os.system('pause')
        else:
            try:
                int(inputcode)
            except:
                print('You input an unknown vaule')
                continue
            i = 0
            for i in range(len(ActionType)):
                if inputcode == i:
                    tmp1 = ActionType[i]
                    break
            print(ActionTypeValues[i])
            print('Please input script\'s value,or cancel to back')
            inputcode = input()
            print('Your input:' + inputcode)
            if inputcode == 'cancel':
                continue
            else:
                data += '[' + tmp1 + ' ' + inputcode + ']'
                continue
