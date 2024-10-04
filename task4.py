# Oyun kartlarının siyahısı və onların rəqəmləri
el = [
    {"ad": "Kart 5", "rəqəm": 5},
    {"ad": "Kart 3", "rəqəm": 3},
    {"ad": "Kart 8", "rəqəm": 8},
    {"ad": "Kart 1", "rəqəm": 1},
    {"ad": "Kart 4", "rəqəm": 4}
]

# Insertion Sort alqoritmi ilə kartları rəqəmə görə sıralamaq
for i in range(1, len(el)):
    current_card = el[i]
    position = i

    # Sıralanmış hissədə uyğun mövqeni tapmaq üçün hərəkət et
    while position > 0 and el[position - 1]["rəqəm"] > current_card["rəqəm"]:
        el[position] = el[position - 1]
        position -= 1

    # Kartı uyğun mövqeyə yerləşdir
    el[position] = current_card

# Sıralanmış kartların siyahısını çap etmək
print("Kartların rəqəmlərə görə sıralanması:")
for kart in el:
    print(f"{kart['ad']}: {kart['rəqəm']}")
