from math import dist

def center(cluster):
    ans = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'.\files\27_B_17882.txt') as file:
    dots = [list(map(float, i.split())) for i in file]

cluster_1 = [d for d in dots if d[1] > 7]
cluster_2 = [d for d in dots if 3 < d[1] <7]
cluster_3 = [d for d in dots if d[1] < 3]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

Px = (center_1[0] + center_2[0] + center_3[0]) /3
Py = (center_1[1] + center_2[1] + center_3[1]) /3

print(Px *10000, Py *10000)