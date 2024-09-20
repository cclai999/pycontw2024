import socketserver
import threading
from time import sleep


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    request_queue_size = 40


def func1(index):
    print("func1 pass")
    return 1, "OK"


def func_cause_exception(index):
    a = 1
    b = 0
    print(a/b) # ZeroDivisionError


def func_not_implement(index):
    print("func_not_implement pass")
    return -1, "func not found!"


func_mapper = {
    "func1": func1,
    "func_cause_exception": func_cause_exception,
}


def parser_data(data):
    parts = data.decode().split(",")
    if len(parts) == 2:
        ifx_index = int(parts[0])
        function_name = parts[1].strip()
        return ifx_index, function_name
    else:
        raise ValueError("socket data format error")


class PaymentTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        cur_thread = threading.current_thread()
        data = self.request.recv(1024).strip()
        print(f"{cur_thread.name}; {self.client_address[0]} wrote: {data}")
        sleep(3)
        # just send back the same data, but upper-cased
        ifx_result = -1
        try:
            ifx_index, function_name = parser_data(data)
            ifx_result, msg = func_mapper.get(function_name, func_not_implement)(ifx_index)
            result = f"{ifx_result},{msg}"
            self.request.sendall(result.encode())
        except Exception as e:
            # capture_exception(e)
            result = f"-1, Something wrong"
            self.request.sendall(result.encode("utf-8"))
        finally:
            self.request.close()
            print(f"{cur_thread.name}; {self.client_address[0]} wrote: {data} done")
            sleep(1)


if __name__ == "__main__":
    # Set the server's host and port
    host, port = "localhost", 9999

    # Create the server
    server = ThreadedTCPServer((host, port), PaymentTCPHandler)

    # Activate the server; this will keep running until you interrupt the program with Ctrl+C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

    # Clean up (close the server)
    server.server_close()
