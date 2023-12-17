import socket
import ssl
import json


class Client:
    def __init__(
        self,
        target_ip: str,
        target_port: int = 80,
        verbose: bool = False,
        method: str = "GET",
        jptheader: str = "Content-Type: application/json",
        data: str = ""
    ) -> None :
        """Initialize parameters."""
        self.target_ip = target_ip
        self.target_port = target_port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.verbose = verbose
        self.method = method
        self.json_content_type = jptheader
        self.data = data

    def send_data(self, sock: socket, data: str, verbose: bool) -> str:
        sock.send(data)
        response = sock.recv(4056)
        # print(response.decode('utf-8'))
        if not self.verbose:
            return response.decode("utf-8")[230:]
        else:
            return response.decode("utf-8")

    def connect(self) -> None:
        try:
            self.client.connect((self.target_ip, self.target_port))

            if self.method == "GET":
                print("\n")
                data = "GET /get HTTP/1.1\r\nHost: {}\r\n\r\n".format(
                    self.target_ip
                ).encode("utf-8")

                response = self.send_data(self.client, data, self.verbose)
                print(response)

            if self.method == "DELETE":
                print("\n")
                data = "DELETE /delete HTTP/1.1\r\nHost: {}\r\n\r\n".format(
                    self.target_ip
                ).encode("utf-8")

                response = self.send_data(self.client, data, self.verbose)
                print(response)

            if self.method == "POST":
                if self.target_port == 443:
                    context = ssl.create_default_context()
                    with context.wrap_socket(
                        self.client, server_hostname="eu.httpbin.org"
                    ) as ssock:
                        data = (
                            (
                                "POST /post HTTP/1.1\r\n"
                                "host: eu.httpbin.org\r\n"
                                "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0\r\n"
                                "accept: application/json\r\n"
                                "connection: close\r\n"
                                "content-type:{jct}\r\n"
                                "content-length: {len}\r\n"
                                "\r\n"
                                "{data}"
                            )
                            .format(
                                jct=self.json_content_type.split(":", 1)[1],
                                len=len(self.data),
                                data=self.data,
                            )
                            .encode("utf-8")
                        )
                        response = self.send_data(ssock, data, self.verbose)
                        print(response)
                else:
                    print("Hey man! Use a secure port for POST requests")
        except socket.error as e:
            print("Failed to connect: ", e)
