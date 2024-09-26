# 1. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus (Jonas Jonaitis).
# Atspausdinti trumpesnį stringą.
# vardas = "Dwayne"
# pavarde = "Johnson"
# strings = [vardas, pavarde]
# print(min(strings, key=len))
import re

# 2. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Vardą atspausdinti tik didžiosiom raidėm, o pavardę tik mažosioms. (LEONARDO dicaprio)
# vardas = "Dwayne"
# pavarde = "Johnson"
# print(vardas.upper())
# print(pavarde.lower())

# 3. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš pirmų vardo ir pavardės kintamųjų raidžių. Jį atspausdinti.
# vardas = "Dwayne"
# pavarde = "Johnson"
# varpav = vardas[0] + pavarde[0]
# print(varpav)

# 4. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus.
# Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo ir pavardės kintamųjų raidžių. Jį atspausdinti.
# vardas = "Dwayne"
# pavarde = "Johnson"
# sujungtukas = vardas[-3:] + pavarde[-3:]
# print(sujungtukas)

# 5. Sukurti kintamąjį su stringu: "An American in Paris".
# Jame visas “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.
# kint = "An American in Paris"
# kint2 = kint.replace("A", "*").replace("a", "*")
# print(kint2)

# 6. Sukurti kintamąjį su stringu: "An American in Paris".
# Jame ištrinti visas balses. Rezultatą atspausdinti. Kodą pakartoti su stringais:
# "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".
a1 = "An American in Paris"
b1 = "Breakfast at Tiffany's"
c1 = "2001: A Space Odyssey"
d1 = "It's a Wonderful Life"

keitimas = ""
balses = ("a", "A", "e", "E", "i", "I", "u", "U", "o", "O")
def rem_balses(a1):
    return(re.sub("[aeiouAEIOU]","", a1))
print(rem_balses(a1))

