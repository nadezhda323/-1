cifra = int(input())
nameoper = input()
if nameoper == "+":
    cifradva = int(input())
    itog = cifra + cifradva
if nameoper == "*":
    cifradva = int(input())
    itog = cifra * cifradva
if nameoper == "-":
    cifradva = int(input())
    itog = cifra - cifradva
if nameoper == "/":
    cifradva = int(input())
    if cifradva == 0:
        print("oshibka")
    itog = cifra / cifradva
print(itog)
print("hello")