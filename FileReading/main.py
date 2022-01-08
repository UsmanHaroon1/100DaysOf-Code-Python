with open('test.txt','r') as file:
    names = (file.readlines())

with open('../letter.txt','r') as l:
    content = l.read()

for name in names:
    name = name.strip()
    with open(f'{name}.txt','w') as nf:
        nc = content.replace('name',name)
        nf.write(nc)
