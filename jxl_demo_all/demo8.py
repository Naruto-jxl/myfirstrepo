
alist = []
item_list = {')':'(',']':'[','}':'{','>':'<'}
item = ['(','[','{','<']
astr = 'wqeq({}>'

i = 0
while i < len(astr):
    if alist == []:
        if astr[i] in item_list:
            print('不成对--1',alist)           #未出现右括号，先出现左括号
            break
        else:
            if astr[i] in item:             #属于右括号
                if i != len(astr)-1:
                    alist.append(astr[i])
                    i += 1
                    continue
                else:                       #最后一位，属于右括号
                    print('不成对--2',alist)
                    break
            else:
                if i == len(astr)-1:
                    print('成对',alist)
                    break
                else:
                    i += 1
                    continue
    else:                           #alist不为空
        if i == len(astr)-1:            #最后一位
            if astr[i] not in item_list:
                print('不成对--3',alist)
                break
            else:
                if item_list[astr[i]] == alist[-1]:   #item_list最后一位是alist最后一位
                    alist.pop()
                    if alist == []:
                        print('成对--1',alist)
                        break
                    else:
                        print('不成对--4',alist)
                        break
                else:
                    print('不成对--5',alist)
                    break
        else:               #非最后一位
            if astr[i] not in item_list and astr[i] not in item:
                i += 1
                continue
            elif astr[i] in item:
                alist.append(astr[i])
                i += 1
                continue
            else:               #不是最后一位而且属于左括号
                if item_list[astr[i]] == alist[-1]:
                    alist.pop()
                    i += 1
                    continue
                else:
                    print('不成对--6',alist)
                    break














