import random

def quick_sort_random_pivot(arr):
    if len(arr) <= 1:
        return arr

    # Pivotu təsadüfi seç
    pivot = random.choice(arr)
    print(f"Pivot seçildi (Random): {pivot}")

    # Pivot ətrafında bölmə
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Rekursiv olaraq bölmələri sort et
    return quick_sort_random_pivot(less) + equal + quick_sort_random_pivot(greater)

# Nümunə siyahı
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort_random_pivot(arr)

print("Sıralanmış Siyahı (Random Pivot):", sorted_arr)
