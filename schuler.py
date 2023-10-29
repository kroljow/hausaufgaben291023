# Durchschnittberechnen und Wert in einer neunen Liste speichern
# Beste und Schlechteste Note in jedem Fach auch in einer Liste speichern
# Gesamtdurchschnitt 
# Notenstatistik neue Liste die anzahl der schüler enthält die in jedem fach min 90 prozent erreicht haben
# wie oft kommen die prozentzahlen vor
#--------------------------------------------------

#Gegeben Werte 

mathe = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

#Durchschnitt 
def avarrage(noten):
    summe = sum(noten)
    avarrage = summe /len(noten)
    return avarrage


avarrageMath = avarrage(mathe)
avarragePhysic = avarrage(physik)
avarrageChemestry = avarrage(chemie)

     
avarrageMarks =[ avarrageMath, avarragePhysic, avarrageChemestry]



print( " Die Durschnittsnote des Kurses 26374 in Mathematik ist: ", avarrageMath)
print( " Die Durchschnittsnote des Kurses 26374 in Physik ist: ", avarragePhysic)
print( " Die Durchschnittsnote des Kurses 26374 in Chemie ist: ", avarrageChemestry)

print( " Die Durchschnittsnote aller Fächer:",avarrageMarks)

def bestAndTheWorst (noten):
    bestMark = max(noten)
    worstMark = min(noten)
    return bestMark, worstMark

bestAndWorstMath = bestAndTheWorst(mathe)
bestAndWorstPhysic = bestAndTheWorst(physik)
bestAndWorstChemestry = bestAndTheWorst(chemie)

bestAndTheWorstList = [ bestAndWorstMath, bestAndWorstPhysic, bestAndWorstChemestry]

print("Beste und schlechteste Noten in Mathematik:", bestAndWorstMath)
print("Beste und schlechteste Noten in Physik:", bestAndWorstPhysic)
print("Beste und schlechteste Noten in Chemie:", bestAndWorstChemestry)

print ( "Beste und schlechteste Noten pro Fach:", bestAndTheWorstList)

allMarks = mathe + physik + chemie

def avarrageMain(noten):
    summe = sum(noten)
    durschschnitt = summe / len(noten)
    return durschschnitt

overall = avarrageMain( allMarks)

print("Gesamtdurchschnittsnote über alle Fächer des Kurses:", overall)

def streber (noten):
    anzahl = sum(1 for note in noten if note >= 90)
    return anzahl


anzahlMath = streber(mathe)
anzahlPhysic = streber(physik)
anzahlChemestry = streber (chemie)

HowMuchSmartass = [anzahlMath + anzahlPhysic + anzahlChemestry]


print("Anzahl der Schüler mit mindestens 90 Prozent in Mathematik:", anzahlMath)
print("Anzahl der Schüler mit mindestens 90 Prozent in Physik:", anzahlPhysic)
print("Anzahl der Schüler mit mindestens 90 Prozent in Chemie:", anzahlChemestry)

print("Anzahl der Schüler  mindestens 90 Prozent im Kurs:", HowMuchSmartass)

def frequency (faecher):
    frequencyMarks = {}
    for  fach in faecher: 
        for note in fach:
         if note in frequencyMarks:
            frequencyMarks[note] += 1
         else:
            frequencyMarks[note] = 1
    return frequencyMarks

alleFaecher = [ mathe, physik, chemie]

frequencyOverall = frequency(alleFaecher)

print(" Häufigkeit der Noten in allen Fächern:")
for note, anzahl in frequencyOverall.items():
    print(f"Note {note}: {anzahl} Mal")







