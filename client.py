import requests
import threading
import time

server_url = "http://localhost:5001"


def send_io_request(content):
    start_time = time.time()
    response = requests.post(f'{server_url}/io', data={'content': content})
    end_time = time.time()
    print(response.json())
    print(f"Request time for IO request: {end_time - start_time} seconds")


def send_calculation_request(n):
    start_time = time.time()
    response = requests.get(f'{server_url}/calculation?n={n}')
    end_time = time.time()
    print(response.json())
    print(f"Request time for calculation request: {end_time - start_time} seconds")


def send_requests():
    threading.Thread(target=send_io_request, args=("Hello, World!",)).start()
    threading.Thread(target=send_calculation_request, args=(10,)).start()


if __name__ == '__main__':
    num_requests = 50
    for _ in range(num_requests):
        send_requests()
        time.sleep(0.01)
