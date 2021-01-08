import pyperclip
import sys
import os
def cmd(name_value='', name='', ActionType='', getscript='', ListOfActionType=''):
    for a in range(len(name)):
        if 'cost' in name[a]:
            start = a
    for i in name[start:]:
        #print(i)
        #print(name_value[i])
        globals()[i] = name_value[i]
    data = ''
    while True:
        for i in range(len(ActionType[1:])):
            try:
                print(str(i) + ': ' + globals()[ActionType[i]])
            except KeyError:
                pass
        if len(data)==0:
                print("Please enter action code or exit for close this process")
        else:
                print("Please enter action code or output to output command or clear for clear cache or exit for close this process")
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
                    print('Please input how to trigger the script\n1: interact\n2: walk\n3: break\n4: hit')
                    tmp2 = input()
                    print('Your input:' + inputcode)
                    if tmp2 != '1' or tmp2 !='2'or tmp2 != '3' or tmp2 != '4':
                        break
                while True:
                    print('Please input what do you want to do\n1: create\n2: add\n3: remove')
                    tmp3 = input()
                    print('Your input:' + inputcode)
                    if tmp2 != '1' or tmp2 !='2'or tmp2 != '3':
                        break
                print('The command has been copied to the clipboard. Thanks for using it')
                if not tmp3 == '3':
                    if tmp2 == '1':tmp2 = 'interact'
                    elif tmp2 == '2':tmp2 = 'walk'
                    elif tmp2 == '3':tmp2 = 'break'
                    else:tmp2 = 'hit'
                    if tmp3 == '1':tmp3 = 'create'
                    else:tmp3 = 'add'
                    print('Command: ' + '/sbp ' + tmp2 + ' ' + tmp3 + ' ' + data)
                    pyperclip.copy('/sbp ' + tmp2 + ' ' + tmp3 + ' ' + data)
                    os.system('pause')
                else:
                    if tmp2 == '1':tmp2 = 'interact'
                    elif tmp2 == '2':tmp2 = 'walk'
                    elif tmp2 == '3':tmp2 = 'break'
                    else:tmp2 = 'hit'
                    tmp3 = 'remove'
                    print('Command: ' + '/sbp ' + tmp2 + ' ' + tmp3 + ' ' + data)
                    pyperclip.copy('/sbp ' + tmp2 + ' ' + tmp3)
                    os.system('pause')
        else:
            try:
                int(inputcode)
            except:
                print('You input an unknown vaule')
                continue
            i = 0
            while i <= len(getscript):
                if int(inputcode) == i:
                    tmp1 = (ListOfActionType[i])
                    break
                i = i+1
            print(globals()[ActionType[i]])
            print('Please input script\'s value,or cancel to back')
            inputcode = input()
            print('Your input:' + inputcode)
            if inputcode == 'cancel':
                continue
            else:
                data += '[' + tmp1 + ' ' + inputcode + ']'
                continue