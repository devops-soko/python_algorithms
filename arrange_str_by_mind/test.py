def solution(strings, n):
    for i in range(0, len(strings)) :
        strings[i] = strings[i][n]+ strings[i]
    
    strings.sort()
    return [word[1:] for word in strings]

print(solution (["abce", "abcd", "cdx"],2))