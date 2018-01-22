def trim(s):
    if s == '':
        return s
    if s[0] == ' ':
        return trim(s[1:len(s)-1])
    if s[len(s)-1] == ' ':
        return trim(s[0:len(s)-2])
    return s
    
print(trim('      e      '))
