def quick_sort_worst_case(arr, depth=0):
    if len(arr) <= 1:
        return arr

    # Pivot olaraq ən son elementi seç (ən pis halda)
    pivot = arr[-1]
    print(f"{'  '*depth}Pivot seçildi: {pivot}")

    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]

    print(f"{'  '*depth}Sol hissə: {left}")
    print(f"{'  '*depth}Sağ hissə: {right}")

    # Rekursiv olaraq sıralama
    sorted_left = quick_sort_worst_case(left, depth + 1)
    sorted_right = quick_sort_worst_case(right, depth + 1)

    return sorted_left + [pivot] + sorted_right

# Ən pis halda Quick Sort-u göstərmək üçün sıralanmış siyahı
arr = list(range(1, 11))  # [1, 2, 3, ..., 10]
sorted_arr = quick_sort_worst_case(arr)

print("Sıralanmış Siyahı:", sorted_arr)
