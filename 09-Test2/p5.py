def f(first_letter, last_letter):
    count = 0
    with open("data.txt", 'r', encoding="utf-8", errors="ignore") as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if word.startswith(first_letter) and word.endswith(last_letter):
                    count+=1
    return count
