def caesar_verschluesseln(text, schluessel): #Funktion verschlüsseln 
    verschluesselter_text = "" # erzeugt Leerzeichenkette die dann den zu verschlüßelten Text enthält
    for zeichen in text:
        if zeichen.isalpha(): # gibt true zurück wenn Zeichen ein Buchstabe ist
            if zeichen.islower(): # gibt true zurück wenn alle Zeichen kleingeschreiben sind 
                verschluesselter_text += chr(((ord(zeichen) - ord('a') + schluessel) % 26) + ord('a'))
            else:
                verschluesselter_text += chr(((ord(zeichen) - ord('A') + schluessel) % 26) + ord('A'))
        else:
            verschluesselter_text += zeichen
    return verschluesselter_text

def caesar_entschluesseln(verschluesselter_text, schluessel): # Funktion zum Entschlüsseln
    return caesar_verschluesseln(verschluesselter_text, -schluessel)

def main(): # hauptfunktion
    while True:
        print("Willkommen zur Caesar-Verschlüsselung und -Entschlüsselung!")
        text = input("Bitte gib einen Text ein: ")
        
        try:
            schluessel = int(input("Gib eine Zahl zwischen -25 bis 25 ein: ")) # Schlüßelabfrage
            if -25 <= schluessel <= 25:
                operation = input("Möchtest du  den Text verschlüsseln (V) oder entschlüsseln (E)? ").lower()
                if operation == 'v':
                    verschluesselter_text = caesar_verschluesseln(text, schluessel)
                    print("Verschlüsselter Text:", verschluesselter_text)
                elif operation == 'e':
                    entschluesselter_text = caesar_entschluesseln(text, schluessel)
                    print("Entschlüsselter Text:", entschluesselter_text)
                else:
                    print("Et tu brute? Ungültige Operation. Bitte 'V' für Verschlüsselung oder 'E' für Entschlüsselung eingeben.") # Fehler
            else:
                print("Et tu brute? Der Verschlüsselungsschlüssel muss im Bereich von -25 bis 25 liegen.")
        except ValueError:
            print(" Et tu brute? Ungültiger Verschlüsselungsschlüssel. Bitte eine ganze Zahl eingeben.")
        
        wiederholen = input("Möchtest du eine weitere Nachricht verschlüsseln oder entschlüsseln? (Ja/Nein): ").lower()
        if wiederholen != 'ja':
            break

if __name__ == "__main__":
    main()

