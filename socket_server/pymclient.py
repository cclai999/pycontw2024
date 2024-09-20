import socket
import threading

message = [
    ",func_cause_exception",
    ",func1",
    ",func2",
    ",too, many, params"
]


def client_thread(host, port, msg_index):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(f"{msg_index}{message[msg_index % 4]}".encode("utf-8"))
        data = s.recv(1024)
        print(f"Received {data.decode()}")


if __name__ == '__main__':
    num_clients = 35
    threads = []
    for i in range(num_clients):
        t = threading.Thread(target=client_thread, args=('localhost', 9999, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()