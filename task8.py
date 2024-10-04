def median_of_three(arr):
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]
    median = sorted([first, middle, last])[1]
    return median

def quick_sort_median_of_three(arr):
    if len(arr) <= 1:
        return arr

    # Pivotu median-of-three ilə seç
    pivot = median_of_three(arr)
    print(f"Pivot seçildi (Median-of-Three): {pivot}")

    # Pivot ətrafında bölmə
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Rekursiv olaraq bölmələri sort et
    return quick_sort_median_of_three(less) + equal + quick_sort_median_of_three(greater)

# Nümunə siyahı
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quick_sort_median_of_three(arr)

print("Sıralanmış Siyahı (Median-of-Three Pivot):", sorted_arr)
