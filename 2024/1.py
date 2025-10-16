import sys

# read input file line by line
with open(sys.argv[1]) as input:
    lines = input.readlines()
    list1 = []
    list2 = []

# split lines and store values in two separate lists
    for line in lines:
        line = line.split()
        list1.append(int(line[0]))
        list2.append(int(line[1]))

# sort lists from lowest to highest values
list1.sort()
list2.sort()

# calculate total distances as sum of distances between each value pair
total_distance = 0
for i in range(len(list1)):
    total_distance += abs(list1[i] - list2[i])

part_1_result = total_distance
print(f"Part 1: {part_1_result}")

# calculate similarity score
similarity_score = sum([x * len([y for y in list2 if y == x]) for x in list1])

part_2_result = similarity_score
print(f"Part 2: {part_2_result}")