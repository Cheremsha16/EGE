from math import dist

def center(cluster):
    ans=[]
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_A_29080.txt') as file:
    dots=[]
    stars=[]
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[:2] == 'L3':
            stars.append([float(x), float(y)])

cluster_1 =[d for d in dots if d[1] >8]
cluster_2 =[d for d in dots if d[1] <8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

stars_1 = [s for s in stars if s in cluster_1]
stars_2 = [ s for s in stars if s in cluster_2]

A1=[]
for s in stars:
    A1.append(dist(center_1, s))
A2=[]
for s in stars:
    A2.append(dist(center_2, s))
print(max(A1)*10000, max(A2)*10000)

