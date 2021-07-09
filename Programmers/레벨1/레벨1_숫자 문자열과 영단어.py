def solution(s):
    answer = ''
    dic = {'zero':0, 'one':1, 'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    word= []
    for i in range(len(s)):
        num = ''.join(word)
        if num in dic:
            answer+=str(dic[num])
            word = []
        if s[i].isdigit():
            answer+=s[i]
        else:
            word.append(s[i])
    if word:
        answer+=str(dic[''.join(word)])
    return int(answer)