def merge_sort(book_chapters):
    """
    Böyük kitabı fəsillərə bölüb, hər fəsili ayrı-ayrılıqda sortlayır və sonra birləşdirir.
    
    Args:
        book_chapters (list): Sortlanacaq fəsillərin siyahısı.
        
    Returns:
        list: Sortlanmış fəsillərin birləşdirilmiş siyahısı.
    """
    
    # 1. **Kitabın Fəsillərə Bölünməsi**
    if len(book_chapters) <= 1:
        return book_chapters

    mid = len(book_chapters) // 2
    left_half = book_chapters[:mid]
    right_half = book_chapters[mid:]

    print(f"Kitab fəsillərə bölündü: {left_half} | {right_half}")

    # 2. **Hər Fəsilin Ayrı-ayrılıqda Yazılması (Sortlanması)**
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # 3. **Fəsillərin Birləşdirilməsi və Yekun Kitabın Yaradılması**
    merged = merge(sorted_left, sorted_right)
    print(f"Fəsillər birləşdirilir: {merged}")
    return merged

def merge(left, right):
    """
    İki sortlanmış siyahını birləşdirərək yeni sortlanmış siyahı yaradır.
    
    Args:
        left (list): Sortlanmış sol hissə.
        right (list): Sortlanmış sağ hissə.
        
    Returns:
        list: Birləşdirilmiş və sortlanmış siyahı.
    """
    merged = []
    i = j = 0

    # Birləşdirmə prosesi
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Sol hissədə qalan elementləri əlavə et
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Sağ hissədə qalan elementləri əlavə et
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

# **Yekun Kitabın Yaradılması:**
# Aşağıdakı nümunədə, kitabın fəsilləri (sıralanması lazım olan ədədlər) merge sort ilə sortlanır.

if __name__ == "__main__":
    # Kitabın fəsilləri (sıralanması lazım olan ədədlər)
    book = [38, 27, 43, 3, 9, 82, 10]
    print("Yekun kitabın yaradılması başlanır.")
    sorted_book = merge_sort(book)
    print(f"Yekun kitab sortlandı: {sorted_book}")
