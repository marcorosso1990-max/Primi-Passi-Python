# Funzione per chiedere il nome, l'anno di nascita e salutare l'utente
def saluto():
    nome = input("Ciao! Come ti chiami? ")
    anno_nascita = input("In che anno sei nato? ")
    try:
        anno_nascita = int(anno_nascita)
        eta_2030 = 2030 - anno_nascita
        print(f"Piacere di conoscerti, {nome}!")
        print(f"Nel 2030 avrai {eta_2030} anni.")
    except ValueError:
        print(f"Piacere di conoscerti, {nome}!")
        print("Non ho capito l'anno di nascita. Per favore inserisci un numero valido.")

# Chiamata alla funzione
saluto()



