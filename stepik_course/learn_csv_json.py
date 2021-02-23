import csv
import json

with open("example.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#with open("example1.csv") as f:
    #writer = csv.writer(f, quoting = csv.QUOTE_NONNUMERIC)
    #writer.writerows([['student', ' best', ' 100', ' 100', '100', ' Excellent score'], ['student', ' good', ' 90', ' "90.2"', ' 100', 'Good score\nbut could do better']])

student1 = {
    "first name" : "Greg",
    "last name" : "Dean",
    "scores" : [70, 80, 90],
    "description" : "Good job, Greg",
    "certificate" : True
}

student2 = {
    "first name" : "Wirt",
    "last name" : "Wood",
    "scores" : [80, 80.2, 80],
    "description" : "Nicely done",
    "certificate" : True
}

data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True)) # принимает первый объект в формате пайтон, а возвращает в формате json
# indent - количество отступов, sort_keys - сортировка ключей 
with open("students.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)

with open("students.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"]))