import random
import math
from collections import defaultdict
import copy

# Dataset
data_points = [(2, 3), (5, 8), (1, 2), (8, 8), (1, 0), (9, 11), (8, 2), (10, 2)]
k = 2  # Number of clusters
iterations = 3
centroids = random.sample(data_points, k)

for _ in range(iterations):
    # Mapper phase: assign points to nearest centroid
    mapped = [(min(range(k), key=lambda i: math.dist(p, centroids[i])), p) for p in data_points]

    # Shuffle & reduce: group points by centroid and calculate new centroids
    grouped = defaultdict(list)
    for idx, p in mapped:
        grouped[idx].append(p)
    centroids = [tuple(map(lambda x: sum(x)/len(x), zip(*grouped[i]))) if grouped[i] else centroids[i] for i in range(k)]

# Output final centroids
for i, c in enumerate(centroids, 1):
    print(f"Centroid {i}: {c}")
