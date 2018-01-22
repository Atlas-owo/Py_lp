def trim(s):
    if s == '':
        return s
    for i in range(len(s)) :
        if s[i] != ' ':
            s = s[i:len(s)]
            break
    if i == len(s)-1:
        return ''

    s1 = list(range(len(s)))
    s1.reverse()
    for j in s1:
        if s[j] != ' ':
            s = s[0:j+1]
            break

    return s

print(trim('        w '))
print(trim('    '))
