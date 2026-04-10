# Crea un gioco dove il computer sceglie un numero da 1 a 20 e io devo indovinarlo.
# Dimmi se il numero è troppo alto o troppo basso e conta i tentativi.
import random
def indovina_numero():
    numero_segreto = random.randint(1, 20)
    tentativi = 0
    indovinato = False

    print("Benvenuto al gioco Indovina il Numero!")
    print("Il computer ha scelto un numero tra 1 e 20. Prova a indovinarlo!")

    while not indovinato:
        try:
            guess = int(input("Inserisci il tuo tentativo: "))
            tentativi += 1

            if guess < numero_segreto:
                print("Troppo basso! Riprova.")
            elif guess > numero_segreto:
                print("Troppo alto! Riprova.")
            else:
                indovinato = True
                print(f"Congratulazioni! Hai indovinato il numero {numero_segreto} in {tentativi} tentativi.")
        except ValueError:
            print("Per favore, inserisci un numero valido.")
if __name__ == "__main__":    indovina_numero() 
