# coding:utf-8
# 基础导入
import os
import time
import sys
import re
import gc
from urllib.request import urlopen as get
# import socket
# socket.setdefaulttimeout(20)
#import retrying
# import codecs
import locale
import json
import platform
import socket
nogetlocale = False
Windows = False
if platform.system() == 'Windows':
    Windows = True
    import colorama
    from colorama import init, Fore, Back, Style
    init(autoreset=True)

from urllib.request import urlopen
import json
import os
China = False
ip = json.loads(str(urlopen('http://jsonip.com').read(), 'utf-8'))['ip']
print('Your ip: ' + ip)


def base_path(path):
    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)
    return basedir


from geoip2.database import Reader
#print(os.path.join(base_path(''), 'GeoLite2-Country.mmdb'))
country = Reader(os.path.join(
    base_path(''), 'GeoLite2-Country.mmdb')).country(ip).country.iso_code
if country == 'CN':
    print('Maybe you are chinese or you are gone to China...')
    China = True


class Language():
    # 更改txt为json[20200130]
    def GetLanguageFile(Language):
        print('\033[1;32mTry to get Language: ' + Language + ' file...\033[0m')
        try:
            if China:
                a = urlopen(
                    'https://gitee.com/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Language-' + Language + '.json')
                if a.status == 404:
                    a.close()
                    return 404
                elif a.status == 200:
                    with open('languages/language-' + Language + '.json', 'w+', encoding='utf-8') as file:
                        file.write(a.read().decode('utf-8'))
                    a.close()
                else:
                    a.close()
                    return 1
            else:
                a = urlopen(
                    'https://github.com/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Language-' + Language + '.json')
                if a.status == 404:
                    a.close()
                    return 404
                elif a.status == 200:
                    with open('languages/language-' + Language + '.json', 'w+', encoding='utf-8') as file:
                        file.write(a.read().decode('utf-8'))
                    a.close()
                else:
                    a.close()
                    return 1
        except:
            return 2

    def CheckVersion(Language, localversion):
        print('\033[1;32mChecking the language ' +
              Language + ' version...\033[0m')
        try:
            if China:
                a = urlopen(
                    'https://gitee.com/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Languages-versions.json')
                if a.status == 404:
                    a.close()
                    return 404
                elif a.status == 200:
                    remoteversions = json.loads(a.read().decode('utf-8'))
                    a.close()
                else:
                    a.close()
                    return 1
            else:
                a = urlopen(
                    'https://github.com/xiangxiangxiong9/ScriptBlockPlus-Command-spawner/raw/master/languages/Languages-versions.json')
                if a.status == 404:
                    a.close()
                    return 404
                elif a.status == 200:
                    remoteversions = json.loads(a.read().decode('utf-8'))
                    a.close()
                else:
                    a.close()
                    return 1
        except:
            return 2
        if localversion < remoteversions[Language]:
            print('\033[1;31mYour local version has expired. Updating the language file version for you.\033[0m')
            self.GetLanguageFile(Language)


def main():
    global nogetlocale
    CommandMode = False
    for i in sys.argv:
        if i == '-nogui':
            CommandMode = True
        elif '-language=' in i:
            nogetlocale = True
            _Language = i[10:]
    if nogetlocale:
        if not os.path.isfile(os.getcwd() + os.sep + 'languages' + os.sep + 'Language-' + _Language + '.json'):
            if not os.path.exists('languages'):
                print(
                    "\033[1;31mLanguages folder does not exise!Creating!\033[0m")
                os.mkdir('languages')
            languagewtire = Language.GetLanguageFile(_Language)
            if languagewtire == 0:
                pass
            elif languagewtire == 2:
                print(
                    '\033[1;31mThere may be something wrong with your network,we cannot get files on the server.Please try again.\033[0m')
                sys.exit(0)
            elif languagewtire == 404:
                print('\033[1;31mThe translate for language: ' + _Language +
                      ' may not exise...Ignore -language option\033[0m')
                nogetlocale = False
        # 更改txt为json[20200130]
        _Language = os.getcwd() + os.sep + 'languages' + os.sep + \
            'Language-' + _Language + '.json'

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
                    'Please make sure that /language/Language-[Language].json exist\nDefault Language is: en_US\nSuppose Locales: en_US,ja[ja_JP],zh_CN\nLanguage:%s' % locale)
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
        _Language = os.getcwd() + os.sep + 'languages' + os.sep + 'Language-' + \
            configfound.split(':')[1].replace(' ', '') + '.json'
        if not os.path.isfile(_Language):
            if not os.path.exists('languages'):
                print(
                    "\033[1;31mLanguages folder does not exise!Creating!\033[0m")
                os.mkdir('languages')
            languagewtire = Language.GetLanguageFile(
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
                Language.GetLanguageFile('en_US')
                with open(Config, 'w+', encoding='utf-8') as file:
                    file.write(
                        'Please make sure that /language/Language-[Language].json exist\nDefault Language is: en_US\nSuppose Locales: en_US,ja[ja_JP],zh_CN\nLanguage:en_US')

        #@retrying.retry(stop_max_attempt_number=3)

    print('\033[1;32mUsing Language File: \033[1;33m' + _Language + '\033[0m')

    # 语言文件读取
    # 语言文件var设置[更换方式 [20201002]
    # 更改txt为json[20200130]
    with open(_Language, encoding='utf-8') as LanguageFile:
        LanguageText = json.loads(LanguageFile.read())
    Language.CheckVersion(_Language.split(
        os.sep)[-1].replace('Language-', '').replace('.json', ''), LanguageText['version'])

    import Mode
    if (Windows and not CommandMode) or (not Windows and not CommandMode):
        if Mode.WindowsMode(LanguageText) == 1:
            CommandMode = True
    if CommandMode:
        Mode.CommandMode(LanguageText)


main()
