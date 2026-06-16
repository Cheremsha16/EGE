with open(r'.\files\7548.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt=0
for line in data:
    if len(set(line)) == len(line):
        if max(line) + min(line) > sum(line) - max(line) - min(line):
            cnt+=1
print(cnt)
