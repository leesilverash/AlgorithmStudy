from queue import PriorityQueue
import sys

input = sys.stdin.readline
n = int(input().rstrip())
que = PriorityQueue(maxsize=n)

for i in range(n):
    que.put(int(input().rstrip()))

for i in range(que.qsize()):
    print(que.get())
