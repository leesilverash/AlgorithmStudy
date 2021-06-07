import sys

n = int(sys.stdin.readline().strip())
que = []
while(n):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push':
        que.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if que:
            print(que[0])
            del que[0]
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)
    n-=1





