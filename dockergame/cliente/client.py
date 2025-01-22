import socket
import json
SERVER_HOST = "servidor"  
SERVER_PORT = 5000
def connect_to_server():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Conectado al servidor.")
        return client_socket
    except Exception as e:
        print(f"Error al conectar con el servidor: {e}")
        return None
def send_command(client_socket, command, number=None):
    request = {"command": command}
    if number is not None:
        request["number"] = number

    try:
        client_socket.sendall(json.dumps(request).encode("utf-8"))
        response = client_socket.recv(1024).decode("utf-8")
        return json.loads(response)
    except Exception as e:
        print(f"Error al enviar comando: {e}")
        return {"status": "error", "message": "Error en la comunicación con el servidor."}
def start_game(client_socket):
    response = send_command(client_socket, "start")
    print(response["message"])

    while True:
        try:
            command = input("Ingrese comando (guess [numero], quit): ").strip()
            if command.startswith("guess"):
                try:
                    _, number = command.split()
                    number = int(number)
                    response = send_command(client_socket, "guess", number)
                except ValueError:
                    print("Por favor, ingrese un número válido con el comando 'guess'.")
                    continue
            elif command == "quit":
                response = send_command(client_socket, "quit")
                print(response["message"])
                break
            else:
                print("Comando no reconocido. Use 'guess [numero]' o 'quit'.")
                continue

            print(response["message"])
            if response["status"] == "win":
                break

        except Exception as e:
            print(f"Error: {e}")
            break
if __name__ == "__main__":
    client_socket = connect_to_server()
    if client_socket:
        start_game(client_socket)
        client_socket.close()
