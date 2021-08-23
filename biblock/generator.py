import random

rnd = random.Random(0)
nodes = 600
groups = [list(range(300)), list(range(300, nodes))]
pairs = list()
for i in range(nodes):
    for j in range(nodes):
        prob = 0.1 if (i < 300)==(j < 300) else 0.05
        if rnd.uniform(0, 1) < prob:
            pairs.append((i, j))

with open("pairs.txt", "w") as file:
    for i, j in pairs:
        file.write(str(i)+" "+str(j)+"\n")
with open("groups.txt", "w") as file:
    for group in groups:
        file.write(" ".join([str(i) for i in group])+"\n")
