
# splní se více podmínek, pokud je jich v if-elif-else chain více?
a = 3
if a <= 3: # True -> provede se podmínka
    print("a je menší nebo rovno třem") # tedy se vypíše toto a program skončí, nikam dál nepokračuje, už má splněno (elif se neprovede)
elif a == 3:
    print("a je 3")
else:
    print("Else blok je prázdný a právě byl executed.")