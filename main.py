def main():
    dateiname = 'namen.txt'

    with open(dateiname, 'r', encoding='utf-8') as datei:
        zeilen = datei.readlines()

    formatierte_namen = []

    for zeile in zeilen:
        nachname, vorname = zeile.strip().split(',')
        formatierte_namen.append(f'{vorname.strip()} {nachname.strip()}')

    ausgabe = '\n'.join(formatierte_namen)
    print(ausgabe)

if __name__ == '__main__':
    main()
