import os
import time
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

delay = 0.05

def clear_screen(lines_before=5):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

    for _ in range(lines_before):
        print()

def type_like_chatgpt(text, delay):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def zoek_woorden():
    clear_screen()
    woorden_lijst = []

    try:
        with open('inventaris.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                woorden_lijst.append(parts[0].strip())
    except FileNotFoundError as e:
        print('Hier kun je het niet vinden')
        return

    completer = WordCompleter(woorden_lijst, ignore_case=True)
    zoek = prompt('Waar ben je naar op zoek?\n', completer=completer)
    clear_screen()
    gevonden = False
    try:
        with open('inventaris.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(' - ')
                if zoek.lower() in parts[0].strip().lower():
                    text = line
                    type_like_chatgpt(text, delay)
                    gevonden = True
                    break
    except FileNotFoundError as e:
        print('Hier kun je het niet vinden')
        return

    if not gevonden:
        print('Dit zit niet in je bureau lades')

def woorden_toevoegen():
    clear_screen()
    afkortingen_begrippen = input('Wat wil je opbergen?\n')
    betekenis = input('Geef hier aan in welke lade je het doet en evt. een beschrijving: (L1 = Linkerkast lade 1)\n')

    gevonden = False
    try:
        with open('inventaris.txt', 'r') as file:
            for line in file:
                if afkortingen_begrippen in line:
                    print('Dit zit al in deze lade.')
                    gevonden = True
                    break
    except FileNotFoundError as e:
        print('Ik kan de inhoud niet vinden')
        return

    if not gevonden:
        clear_screen()
        with open('inventaris.txt', 'a') as file:
            file.write(afkortingen_begrippen + ' - ' + betekenis + '\n')

def main():
    while True:
        print()
        print()
        keuze = input('Wil je iets zoeken(Z), toevoegen(T), of hou je er mee op(Q)?\n').lower()
        if keuze == 'z':
            zoek_woorden()
        elif keuze == 't':
            woorden_toevoegen()
        elif keuze == 'q':
            break
        else:
            print('Ongeldige invoer, probeer opnieuw.')

if __name__ == '__main__':
    main()
