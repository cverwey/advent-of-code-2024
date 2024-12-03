list1 = []
list2 = []

with open(r".\day-01\input.txt", "r") as file:
    content = file.read()

for line in content.splitlines():
    item1, item2 = line.split("   ")
    list1.append(int(item1))
    list2.append(int(item2))

list1.sort()
list2.sort()

distances = [abs(a - b) for a, b in zip(list1, list2)]
sum_dist = sum(distances)

# print(distances)
print(sum_dist)
