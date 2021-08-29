import sys
K, N = map(int, sys.stdin.readline().strip().split())
word_list = {}
first_letters = []
for i in range(K):
    word_list[sys.stdin.readline().rstrip()] = 0
for i in range(N):
    first_letters.append(sys.stdin.readline().rstrip())

def findWords(letter):
    tmp_list = list(zip(word_list.keys(), word_list.values()))
    cnt = 0
    answer = []
    for word in tmp_list:
        if not answer:
            if word[0][0] == letter:
                answer.append(word[0])
                cnt = word[1]
        elif word[0][0] == letter:
            if word[1] <= cnt:
                answer.append(word[0])
    answer.sort()
    word_list[answer[0]] = cnt+1
    return answer[0]

for letter in first_letters:
    print(findWords(letter))


