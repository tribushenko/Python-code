from collections import Counter
import collections
import csv
import json

with open("Crimes.csv") as f:
    reader = csv.reader(f)
    types = []
    for row in reader:
        types.append(row[5])
    counter = collections.Counter(types)
maxi = 0
max_crime = ""
for k, v in counter.items():
    if v > maxi:
        maxi = v
        max_crime = k
print("crime - " + max_crime + ".\nQuantity of happening = " + str(maxi))




js = json.loads(input())
graph = {}
classes = []
for i in js:
    classes.append(i["name"])
    graph[i["name"]] = set(i["parents"])
classes.sort()

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

inherit = []
for i in classes:
    inherit.append(dfs(graph, i))

for j in classes:
    count = 0
    for i in inherit:
        if j in i:
            count += 1
    print(j + " : " + str(count))


