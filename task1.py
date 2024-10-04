import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

sorted_array = list(range(1, 1001))  # 1-dən 1000-ə qədər sıralanmış massiv

start_time = time.time()
result = bubble_sort(sorted_array.copy())
end_time = time.time()

print("Sıralanmış massiv:", result[:10], "...")  # İlk 10 elementi göstərmək kifayətdir
print(f"İşləmə vaxtı: {end_time - start_time} saniyə")
