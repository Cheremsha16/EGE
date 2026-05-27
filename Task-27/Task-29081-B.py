from math import dist

def center(cluster):
    ans =[]
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_B_29081.txt') as file:
    dots =[]
    stars =[]
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data != 'VII' and int(data[1]) >= 8:
            stars.append([float(x), float(y)])

cluster_1 = [d for d in dots if d[1] < 15]
cluster_2 = [ d for d in dots if 15 < d[1] < 22]
cluster_3 = [ d for d in dots if 22 < d[1]]

stars_1 = [s for s in stars if s in cluster_1]
stars_2 = [s for s in stars if s in cluster_2]
stars_3 = [s for s in stars if s in cluster_3]

B1 = []
for s1 in stars_1:
    for s2 in stars_2:
        B1.append(dist(s1, s2))
for s2 in stars_2:
    for s3 in stars_3:
        B1.append(dist(s2, s3))
for s1 in stars_1:
    for s3 in stars_3:
        B1.append(dist(s1, s3))
print(min(B1) * 10000)

B2 =[]
for s1 in stars_1:
    for s2 in stars_1:
        if s1 != s2:
            B2.append(dist(s1, s2))
for s1 in stars_2:
    for s2 in stars_2:
        if s1 != s2:
            B2.append(dist(s1, s2))
for s1 in stars_3:
    for s2 in stars_3:
        if s1 != s2:
            B2.append(dist(s1, s2))
B2= sum(B2) / len(B2)
print(B2 *10000)