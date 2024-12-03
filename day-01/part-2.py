# list1 = [3, 4, 2, 1, 3, 3]
# list2 = [4, 3, 5, 3, 9, 3]

list1 = []
list2 = []

with open(r".\day-01\input.txt", "r") as file:
    content = file.read()

for line in content.splitlines():
    item1, item2 = line.split("   ")
    list1.append(int(item1))
    list2.append(int(item2))

similarity_scores = [x * list2.count(x) for x in list1]
score = sum(similarity_scores)

print(score)
