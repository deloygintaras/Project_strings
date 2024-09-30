# 1. Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus (Jonas Jonaitis).
# Atspausdinti trumpesnį stringą.
# vardas = "Dwayne"
# pavarde = "Johnson"
# strings = [vardas, pavarde]
# print(min(strings, key=len))
import random
import re
import string

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
# a1 = "An American in Paris"
# b1 = "Breakfast at Tiffany's"
# c1 = "2001: A Space Odyssey"
# d1 = "It's a Wonderful Life"
#
# keitimas = ""
# balses = ("a", "A", "e", "E", "i", "I", "u", "U", "o", "O")
# def rem_balses(a1):
#     return(re.sub("[aeiouAEIOU]","", a1))
# print(rem_balses(a1))
#
# def rem_balses(b1):
#     return(re.sub("[aeiouAEIOU]","", b1))
# print(rem_balses(b1))
#
# def rem_balses(c1):
#     return(re.sub("[aeiouAEIOU]","", c1))
# print(rem_balses(c1))
#
# def rem_balses(d1):
#     return(re.sub("[aeiouAEIOU]","", d1))
# print(rem_balses(d1))

# 7. Stringe, kurį generuoja toks kodas:
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + "
# - A New Hope" Surasti ir atspausdinti epizodo numerį.	su


# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# epizodonr = starWars.split()[3]
# print("Episode number", epizodonr)

# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
# EpizodoNr = re.search('[1-9]',starWars)
# if EpizodoNr:
#     nr = EpizodoNr.group()
#     print("Epizodo numeris: ", EpizodoNr)

# 8. Suskaičiuoti kiek stringe “Don('t Be a Menace to South Central While Drinking Your Juice in the Hood”
# yra žodžių trumpesnių arba lygių nei 5 raidės. Pakartokite kodą su stringu “Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale”.)

# kint1 = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
# kint2 = "Tik nereikia gasdinti Pietu Centro, geriant sultis pas save kvartale"
#
# words = kint1.split()
# words1 = kint2.split()
# short_words = [word for word in words if len(word) <= 5]
# short_words1 = [word for word in words1 if len(word) <= 5]
# print(kint1)
# print(kint2)
# print("Trumpesni arba lygus penkiem raidem zodziai Angliskame tekste:", len(short_words))
# print("Trumpesni arba lygus penkiem raidem zodziai Lietuviskame tekste:", len(short_words1))

# 9.Parašyti kodą, kuris generuotų atsitiktinį stringą iš lotyniškų mažųjų raidžių. Stringo ilgis 3 simboliai.
# n = 3
# res = ''.join(random.choices(string.ascii_lowercase, k = n))
# print("Generuojamas stringas:" + str(res))

# 10. Parašykite kodą, kuris generuotų atsitiktinį stringą su 10 atsitiktine tvarka išdėliotų žodžių,
# o žodžius generavimui imtų iš 8-me uždavinyje pateiktų dviejų stringų. Žodžiai neturi kartotis. (reikės masyvo)


# kint1 = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
# kint2 = "Tik nereikia gasdinti Pietu Centro, geriant sultis pas save kvartale"
#
# zodziai1 = kint1.split()
# zodziai2 = kint2.split()
# visi = zodziai1 + zodziai2
# if len(visi) >= 10:
#     random.shuffle(visi)
# atsitiktinis_zodziai = visi[:10]
# atsitiktinis_stringas= ' '.join(atsitiktinis_zodziai)
# print(atsitiktinis_stringas)
