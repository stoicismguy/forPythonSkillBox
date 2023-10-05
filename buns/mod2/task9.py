i = input()
vowels = "ауоыиэяюёе"
consonants = "бвгджзйклмнпрстфхцчшщ"
vowels_count = 0
consonants_count = 0
for n in vowels:
    vowels_count += i.count(n)
    
for n in consonants:
    consonants_count += i.count(n)

print(f"{vowels_count} {consonants_count}")
