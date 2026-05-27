from math import dist

def center(cluster):
    ans=[]
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_A_29081 (1).txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data == 'VII':
            stars.append([float(x), float(y)])

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

stars_1 = [s for s in stars if s in cluster_1]
stars_2 = [ s for s in stars if s in cluster_2]

A =[]
for s in stars_1:
    A.append(dist(s, center_1))
for s in stars_2:
    A.append(dist(s, center_2))

print(min(A) * 10000, max(A) * 10000)

#B2 = [dist(s1, s2) for s in stars for s1, s2 in combinations(s, 2)]