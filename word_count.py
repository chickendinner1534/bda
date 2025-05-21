import os
from collections import defaultdict

with open("input.txt", "w") as f:
    f.write("hello world\nhello mapreduce\nhello hadoop world\n")

intermediate = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        for word in line.split():
            intermediate.append((word, 1))

shuffle = defaultdict(list)
for word, count in intermediate:
    shuffle[word].append(count)

results = []
for word in sorted(shuffle.keys()):
    total = sum(shuffle[word])
    results.append((word, total)) 
with open("wordcount_output.txt", "w") as f:
    for word, count in results:
        f.write(f"{word}\t{count}\n")
print(hadoop_log.strip())
with open("wordcount_output.txt") as f:
    print("\nWord Count Output:\n" + f.read())
