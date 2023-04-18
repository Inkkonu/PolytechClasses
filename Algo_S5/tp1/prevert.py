data: str
with open('data_inventaire_prevert.txt', 'r') as infile:
    data = infile.read().replace(';', '\n')

i = 1
output: str = ''
for line in data.split('\n'):
    if line == '':
        output += '\n'
    else:
        output += f'{i:02d}. {line}\n'
        i += 1

with open('inventaire_prevert.txt', 'w') as outfile:
    outfile.write(output)
