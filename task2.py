# Şagirdlərin siyahısı və onların qiymətləri
sinif = [
    {"ad": "Əli", "qiymət": 85},
    {"ad": "Leyla", "qiymət": 92},
    {"ad": "Məmməd", "qiymət": 78},
    {"ad": "Aygün", "qiymət": 90},
    {"ad": "Rəşad", "qiymət": 88}
]

# Selection Sort alqoritmi ilə şagirdləri qiymətə görə sıralamaq
for i in range(len(sinif)):
    # Hal-hazırda ən aşağı qiyməti tapmaq üçün başlanğıc indeksi
    min_index = i
    # Qalan şagirdlər arasında ən aşağı qiyməti tapmaq
    for j in range(i + 1, len(sinif)):
        if sinif[j]["qiymət"] < sinif[min_index]["qiymət"]:
            min_index = j
    # Ən aşağı qiymətə sahib şagirdi mövcud mövqe ilə dəyişdirmək
    sinif[i], sinif[min_index] = sinif[min_index], sinif[i]

# Sıralanmış şagirdlərin siyahısını çap etmək
print("Şagirdlərin qiymətlərə görə sıralanması:")
for shagird in sinif:
    print(f"{shagird['ad']}: {shagird['qiymət']}")
