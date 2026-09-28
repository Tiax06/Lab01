import random

# Costanti del gioco
CODICE_MIN = 1
CODICE_MAX = 50
TENTATIVI_BASE = 6
TENTATIVI_MIN = 3
MAX_LIVELLO = 3


def dai_indizio(tentativo, codice):
    """Restituisce un indizio confrontando il tentativo con il codice segreto"""
    # TODO
    if (tentativo < codice):
        print("più alto")
    else:
        print("più basso")


def stampa_tentativi(n, usati):
    """Stampa la riga dei tentativi: O = disponibile, X = già usato"""
    # TODO
    simboli = []
    for i in range(6): # da 0 a 5
        if i < usati :
            simboli.append("X")
        else:
            simboli.append("O")

        for s in simboli:
            print(s, end = " ")


def gestisci_livello(livello):
    """ Gestisce un singolo livello del gioco.
    Ritorna:
    * True se il giocatore indovina il codice
    * False se il giocatore esaurisce i tentativi.

    NB: Le funzioni dai_indizio() e stampa_tentativi() vanno chiamate dentro questa funzione
    """

    # Inizializzazioni
    n = TENTATIVI_BASE - livello
    if n < TENTATIVI_MIN:
        n = TENTATIVI_MIN

    codice = random.randint(CODICE_MIN, CODICE_MAX)
    usati = 0

    # TODO

    print()
    print(f"Livello {livello}) {n} tentativi")

    stampa_tentativi(n, usati)


    while usati < n:
        stringa = input("Tentativo: ")
        numero = int(stringa)
        if numero < CODICE_MIN or numero > CODICE_MAX:
            print(f"il codice deve essere tra {CODICE_MIN} e {CODICE_MAX}")
            usati += 1
        elif numero == codice:
            print("Accesso consentito")
            return True
        else: #nell'intervallo ma non corretto
            usati += 1
            dai_indizio(numero, codice)

    print("GAME OVER, tentativi esauriti")
    return False


def main():
    print("=== Benvenuto in Vault Code ===")
    livello = 0

    while livello <= MAX_LIVELLO:
        completato = gestisci_livello(livello)
        if completato:
            livello += 1
        else:
            break


if __name__ == "__main__":
    main()
