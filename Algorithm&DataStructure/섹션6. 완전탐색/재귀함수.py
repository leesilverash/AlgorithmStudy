# n 이 입력되면 1부터 n까지 출력되는 재귀함수
def DFS(x):
    if x > 0:
        DFS(x-1)
        print(x, end=" ")

if __name__ == "__main__":
    n = int(input())
    DFS(n)