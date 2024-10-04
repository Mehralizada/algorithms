def median_of_three_list(tickets):
    first = tickets[0]
    middle = tickets[len(tickets) // 2]
    last = tickets[-1]
    median = sorted([first, middle, last])[1]
    return median

def distribute_tickets_balanced_median(tickets, groups=None, depth=0):
    if groups is None:
        groups = []

    if not tickets:
        return groups

    # Pivotu median-of-three ilə seç
    pivot = median_of_three_list(tickets)
    groups.append([pivot])  # Yeni qrup yaradılır
    print(f"{'  '*depth}Pivot seçildi (Median-of-Three): {pivot}")

    # Pivot ətrafında bölmə
    less = [ticket for ticket in tickets if ticket < pivot]
    greater = [ticket for ticket in tickets if ticket > pivot]

    # Rekursiv olaraq bölmələri sort et
    distribute_tickets_balanced_median(less, groups, depth + 1)
    distribute_tickets_balanced_median(greater, groups, depth + 1)

    return groups

# Bilet siyahısını yarat (1-dən 10-a qədər nümunə)
tickets = list(range(1, 11))

# Sıralanmış və balanslı bölməni göstər
groups = distribute_tickets_balanced_median(tickets)

print("\nBiletlərin Balanslı Bölünməsi (Median-of-Three Pivot):")
for i, group in enumerate(groups, 1):
    print(f"Qrup {i}: {group}")
