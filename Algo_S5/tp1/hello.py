s: str = 'Bonjour'
t: str = ''
if s == 'Bonjour':
    t = '0o7'
    s += t
else:
    s += ' World!'
print(s)

print(f'Dissection de la chaîne de caractères {s!r} :')
for i in range(len(s)):
    print(i, s[i])