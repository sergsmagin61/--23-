import math

def find_min_distance(A, B):
    min_distance = float('inf')
    min_points = None

    for point_a in A:
        for point_b in B:
            distance = math.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)
            if distance < min_distance:
                min_distance = distance
                min_points = (point_a, point_b)

    return min_distance, min_points


set_A = [(1, 4), (2, 5), (3, 6)]
set_B = [(7, 10), (8, 11), (9, 12)]

min_distance, min_points = find_min_distance(set_A, set_B)

print(f"Минимальное расстояние: {min_distance}")
print(f"Точки на минимальном расстоянии: {min_points}")
