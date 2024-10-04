import random

def distribute_tickets_balanced(tickets, groups=None, depth=0):
    if groups is None:
        groups = []

    if not tickets:
        return groups

    # Pivotu təsadüfi seç
    pivot = random.choice(tickets)
    groups.append([pivot])  # Yeni qrup yaradılır
    print(f"{'  '*depth}Pivot seçildi (Random): {pivot}")

    # Pivot ətrafında bölmə
    less = [ticket for ticket in tickets if ticket < pivot]
    greater = [ticket for ticket in tickets if ticket > pivot]

    # Rekursiv olaraq bölmələri sort et
    distribute_tickets_balanced(less, groups, depth + 1)
    distribute_tickets_balanced(greater, groups, depth + 1)

    return groups

# Bilet siyahısını yarat (1-dən 10-a qədər nümunə)
tickets = list(range(1, 11))

# Sıralanmış və balanslı bölməni göstər
groups = distribute_tickets_balanced(tickets)

print("\nBiletlərin Balanslı Bölünməsi (Random Pivot):")
for i, group in enumerate(groups, 1):
    print(f"Qrup {i}: {group}")
