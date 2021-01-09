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
# import retrying
# import codecs
import locale
import platform
import sub
nogetlocale = False
Windows = False
if platform == 'Windows':
    Windows = True
    import colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)


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
                c = urllib.request.urlopen(
                    'https://gitee.com/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Language-' + Language + '.txt')
                if c.status == 404:
                    c.close()
                    return 404
                elif c.status == 200:
                    with open('languages/language-' + Language + '.txt', 'w+', encoding='utf-8') as file:
                        file.write(c.read().decode('utf-8'))
                        c.close()
                    return 0
                else:
                    c.close()
                    return 1
            except:
                return 2


def main():
    global nogetlocale
    for i in sys.argv:
        if i == '-nogui':
            CommandMode = True
        elif '-language=' in i:
            nogetlocale = True
            Language = i[10:]
    if nogetlocale:
        if not os.path.isfile(os.getcwd() + os.sep + 'languages' + os.sep + 'Language-' + Language + '.txt'):
            if not os.path.exists('languages'):
                print(
                    "\033[1;31mLanguages folder does not exise!Creating!\033[0m")
                os.mkdir('languages')
            languagewtire = getLanguageFile(Language)
            if languagewtire == 0:
                pass
            elif languagewtire == 2:
                print(
                    '\033[1;31mThere may be something wrong with your network,we cannot get files on the server.Please try again.\033[0m')
                sys.exit(0)
            elif languagewtire == 404:
                print('\033[1;31mThe translate for language: ' + Language +
                      ' may not exise...Ignore -language option\033[0m')
                nogetlocale = False
        Language = os.getcwd() + os.sep + 'languages' + os.sep + \
            'Language-' + Language + '.txt'

    if not nogetlocale:
        global locale
        tmp = locale.getdefaultlocale()[0]
        del locale
        locale = tmp
        del tmp
        gc.collect()
        # 语言文件获取
        Config = os.getcwd() + os.sep + 'config.txt'
        # 判断文件是否存在
        try:
            f = open(Config, 'r', encoding='utf-8')
            f.close()
        except IOError:
            print("\033[1;31mConfig file does not exise!Creating!\033[0m")
            with open(Config, 'w+', encoding='utf-8') as file:
                file.write(
                    'Please make sure that /language/Language-[Language].txt exist\nDefault Language is: en_US\nSuppose Locales: en_US,ja[ja_JP],zh_CN\nLanguage:en_US')
        Configfile = open(Config, 'r', encoding='utf-8')
        print('\033[1;32mConfig File: \033[1;33m' + Config + '\033[0m')
        for configfound in Configfile.readlines():
            key = "Language:"
            if key in configfound:
                s = re.findall('"TimeSpan":"([\d.]+)"', configfound)
            Configfile.close()
        Configfile = open(Config, 'r', encoding='utf-8')
        for configfound in Configfile.readlines():
            key = "Language:"
            if key in configfound:
                s = re.findall('"TimeSpan":"([\d.]+)"', configfound)
            Configfile.close()
        Language = os.getcwd() + os.sep + 'languages' + os.sep + 'Language-' + \
            configfound.split(':')[1].replace(' ', '') + '.txt'
        if not os.path.isfile(Language):
            if not os.path.exists('languages'):
                print(
                    "\033[1;31mLanguages folder does not exise!Creating!\033[0m")
                os.mkdir('languages')
            languagewtire = getLanguageFile(
                configfound.split(':')[1].replace(' ', ''))
            if languagewtire == 0:
                pass
            elif languagewtire == 2:
                print(
                    '\033[1;31mThere may be something wrong with your network,we cannot get files on the server.Please try again.\033[0m')
                sys.exit(0)
            elif languagewtire == 404:
                print('\033[1;31mThe translate for language: ' + locale +
                      ' may not exise...The default language will be used\033[0m')
                getLanguageFile('en_US')
                with open(Config, 'w+', encoding='utf-8') as file:
                    file.write(
                        'Please make sure that /language/Language-[Language].txt exist\nDefault Language is: en_US\nSuppose Locales: en_US,ja[ja_JP],zh_CN\nLanguage:en_US')

        #@retrying.retry(stop_max_attempt_number=3)

    print('\033[1;32mUsing Language File: \033[1;33m' + Language + '\033[0m')

    def getscript():
        resule = []
        for i in range(len(ActionType)):
            try:
                resule.append(globals()[ActionType[i]])
            except KeyError as err:
                pass
        return resule

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
    CommandMode = False
    # print([str(globals()), str([name for name in globals()])])
    for i in sys.argv:
        if i == '-nogui':
            CommandMode = True
    if not Windows and not CommandMode:
        sub.WindowsMode.windows(
            name_value=globals(), name=[name for name in globals()], ActionType=ActionType, getscript=getscript(), ListOfActionType=ListOfActionType)
    if CommandMode:
        sub.CommandMode.cmd(name_value=globals(), name=[name for name in globals(
        )], ActionType=ActionType, getscript=getscript(), ListOfActionType=ListOfActionType)


main()
