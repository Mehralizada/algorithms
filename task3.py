# Kitabların siyahısı və onların hündürlükləri (sm)
rüf = [
    {"ad": "Kitab A", "hündürlük": 30},
    {"ad": "Kitab B", "hündürlük": 25},
    {"ad": "Kitab C", "hündürlük": 40},
    {"ad": "Kitab D", "hündürlük": 35},
    {"ad": "Kitab E", "hündürlük": 20}
]

# Bubble Sort alqoritmi ilə kitabları hündürlüyə görə sıralamaq
n = len(rüf)
for i in range(n):
    # Hər pass üçün dəyişiklik olub olmadığını izləmək üçün bayraq
    dəyişiklik = False
    for j in range(0, n - i - 1):
        # Əgər sol kitab sağ kitabdan daha uzunlüsə, dəyiş
        if rüf[j]["hündürlük"] > rüf[j + 1]["hündürlük"]:
            rüf[j], rüf[j + 1] = rüf[j + 1], rüf[j]
            dəyişiklik = True
    # Əgər bu passda heç bir dəyişiklik olmayıbsa, sıralama tamamlanıb
    if not dəyişiklik:
        break

# Sıralanmış kitabların siyahısını çap etmək
print("Kitabların hündürlüklərə görə sıralanması:")
for kitab in rüf:
    print(f"{kitab['ad']}: {kitab['hündürlük']} sm")
