import itertools
import string

# Шынайы пароль (тек тест үшін)
CORRECT_PASSWORD = "abc123"

# Қолданылатын таңбалар (кіші әріптер мен сандар)
CHARSET = string.ascii_lowercase + string.digits

def brute_force_attack():
    attempts = 0
    for length in range(1, len(CORRECT_PASSWORD) + 1):
        for guess in itertools.product(CHARSET, repeat=length):
            attempts += 1
            guess_password = "".join(guess)
            print(f"Тексеру: {guess_password}")
            if guess_password == CORRECT_PASSWORD:
                print(f"Пароль бұзылды: {guess_password}, {attempts} әрекеттен кейін!")
                return

if __name__ == "__main__":
    brute_force_attack()
