def trasformata_bwt(parola):
    text = parola + "$"
    print(text)

    rotazioni = []

    print("Rotazioni: ")
    for i in range(len(text)):
        text = text[1:] + text[0]
        rotazioni.append(text)
        print(text)

    print("Ordinamento: ")
    rotazioni.sort()
    for riga in rotazioni:
        print(riga)

    print("L'ultima colonna della BWT è: ")
    bwt = ""
    for riga in rotazioni:
        last_lettera = riga[-1]
        bwt = bwt + last_lettera
        print(bwt)

    return bwt

if __name__ == "__main__":
    parola = input("Inserisci la parola che vuoi trasformare: ")
    trasformata_bwt(parola)


    