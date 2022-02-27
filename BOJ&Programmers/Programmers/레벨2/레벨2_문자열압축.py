# def solution(s):
#     answer = len(s)
#
#     for i in range(1, int(len(s) / 2) + 1):
#         pos = 0
#         length = len(s)
#
#         while pos + i <= len(s):
#             unit = s[pos:pos + i]
#             pos += i
#
#             cnt = 0
#             while pos + i <= len(s):
#                 if unit == s[pos:pos + i]:
#                     cnt += 1
#                     pos += i
#                 else:
#                     break
#             if cnt > 0:
#                 length -= i * cnt
#
#                 if cnt < 9:
#                     length += 1
#                 elif cnt < 99:
#                     length += 2
#                 elif cnt < 999:
#                     length += 3
#                 else:
#                     length += 4
#         answer = min(answer, length)
#
#     return answer


def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        length = 1     # 압축한 문자열의 길이
        curr = ''     # 현재 압축한 문자열
        ans = ''        # 압축 결과
        for j in range(0,len(s),i):
            tmp = s[j:j+i]
            if curr == tmp:
                length += 1
            else:
                if length > 1:
                    ans += str(length)+tmp
                else:
                    ans += tmp
                length = 1
                curr = tmp
        if length > 1:
            ans += str(length)
        if len(ans) < answer:
            answer = len(ans)

    return answer