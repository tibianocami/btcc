import hashlib
import time

def open_file(nome_file):
    with open(nome_file, "r", encoding="utf-8") as f:
        return f.read()

def op(contenuto, difficolta):
    nonce = 0
    tentativi = 0

    start_time = time.time()

    while True:
        stringa_da_minare = contenuto + str(nonce)
        hashh = hashlib.sha256(stringa_da_minare.encode()).hexdigest()

        tentativi += 1

        # controllo difficoltà
        if hashh.startswith("0" * difficolta):
            end_time = time.time()
            tempo_totale = end_time - start_time

            hash_rate = tentativi / tempo_totale if tempo_totale > 0 else 0

            return nonce, hashh, tentativi, tempo_totale, hash_rate

        nonce += 1

def main():
    nome_file = input("nome file: ")
    contenuto = open_file(nome_file)

    while True:
        try:
            difficolta = int(input("scegli una difficolta compresa tra 1 e 10: "))

            if 1 <= difficolta <= 10:
                break
            else:
                print("fuori range")

        except ValueError:
            print("errore: devi inserire un numero intero")

    nonce, hashh, tentativi, tempo_totale, hash_rate = op(contenuto, difficolta)

    print("\n--- RISULTATI MINING ---")
    print("Nonce trovato:", nonce)
    print("Hash:", hashh)
    print("Tentativi:", tentativi)
    print(f"Tempo totale: {tempo_totale:.4f} secondi")
    print(f"Hash al secondo: {hash_rate:,.2f}")

main()
