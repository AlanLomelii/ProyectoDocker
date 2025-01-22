import socket
import json
import threading
import random

HOST = "0.0.0.0"  
PORT = 5000
sessions = {}
def handle_client(conn, addr):
    print(f"Nueva conexión desde {addr}")
    session_id = addr[1]  
    sessions[session_id] = {"number": random.randint(1, 100), "attempts": 0}

    try:
        while True:
            data = conn.recv(1024).decode("utf-8")
            if not data:
                break
            try:
                request = json.loads(data)
            except json.JSONDecodeError:
                response = {"status": "error", "message": "Formato JSON no válido."}
                conn.sendall(json.dumps(response).encode("utf-8"))
                continue
            response = process_request(session_id, request)
            conn.sendall(json.dumps(response).encode("utf-8"))
    except Exception as e:
        print(f"Error con cliente {addr}: {e}")
    finally:
        print(f"Conexión cerrada con {addr}")
        conn.close()
        if session_id in sessions:
            del sessions[session_id]
def process_request(session_id, request):
    command = request.get("command")
    session = sessions.get(session_id)

    if not session:
        return {"status": "error", "message": "Sesión no encontrada."}

    if command == "start":
        return {"status": "ok", "message": "Juego iniciado. Adivina un número entre 1 y 100."}

    if command == "guess":
        try:
            guess = int(request.get("number"))
        except (TypeError, ValueError):
            return {"status": "error", "message": "Número no válido."}

        session["attempts"] += 1
        if guess < session["number"]:
            return {"status": "continue", "message": "Mayor"}
        elif guess > session["number"]:
            return {"status": "continue", "message": "Menor"}
        else:
            attempts = session["attempts"]
            return {"status": "win", "message": f"¡Correcto! Lo lograste en {attempts} intentos."}

    if command == "quit":
        return {"status": "ok", "message": "Saliendo del juego. ¡Hasta luego!"}

    return {"status": "error", "message": "Comando no reconocido."}
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Servidor iniciado en {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
