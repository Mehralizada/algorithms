def distribute_tickets(tickets, groups=None, depth=0):
    if groups is None:
        groups = []

    if not tickets:
        return groups

    # Hər dəfə ən yüksək nömrəli bileti seç (pivot)
    pivot = max(tickets)
    groups.append([pivot])  # Yeni qrup yaradılır

    # Pivotdan böyük və ya kiçik bilet olmadığı üçün qalan biletlər
    remaining_tickets = [ticket for ticket in tickets if ticket != pivot]

    # Rekursiv olaraq qalan biletləri bölüşdür
    distribute_tickets(remaining_tickets, groups, depth + 1)

    return groups

# Bilet siyahısını yarat (1-dən 10-a qədər nümunə)
tickets = list(range(1, 11))

# Sıralanmış və balanssız bölməni göstər
groups = distribute_tickets(tickets)

print("Biletlərin Balanssız Bölünməsi:")
for i, group in enumerate(groups, 1):
    print(f"Qrup {i}: {group}")
