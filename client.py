import requests
import threading
import time


def send_io_request(content):
    response = requests.post('http://localhost:5000/io',
                             data={'content': content})
    print(response.json())


def send_calculation_request(n):
    response = requests.get(f'http://localhost:5000/calculation?n={n}')
    print(response.json())


def send_requests():
    threading.Thread(target=send_io_request, args=("Hello, World!",)).start()
    threading.Thread(target=send_calculation_request, args=(10,)).start()


if __name__ == '__main__':
    num_requests = 50
    for _ in range(num_requests):
        send_requests()
        time.sleep(0.01)
