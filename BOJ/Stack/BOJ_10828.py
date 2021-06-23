import sys

n = int(sys.stdin.readline().strip())
list = []
for i in range(n):
    command = sys.stdin.readline().strip().split(' ')
    if command[0] == 'push':
        list.insert(len(list),command[1])
    elif command[0] == 'pop':
        if list:
            print(list[len(list)-1])
            del list[len(list)-1]
        else:
            print('-1')
    elif command[0] == 'size':
        print(len(list))
    elif command[0] == 'empty':
        if len(list)==0:
            print('1')
        else:
            print('0')
    else:
        if list:
            print(list[len(list)-1])
        else:
            print('-1')

