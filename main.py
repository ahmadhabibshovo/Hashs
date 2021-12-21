lines = []
with open('hashs.txt') as f:
    lines = f.readlines()
for x in lines:
    print(f'git cherry-pick {x}',end='')
    if lines.index(x) == len(lines)-1:
        print()
    s = input()