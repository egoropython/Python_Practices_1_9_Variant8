import socket, threading, json
from repository import MovieRepository
from service import MovieService
from protocol import encode_message,decode_message
HOST="127.0.0.1"; PORT=50508
service=MovieService(MovieRepository())

def handle_client(conn,address):
    buffer=b""
    with conn:
        while True:
            chunk=conn.recv(4096)
            if not chunk: break
            buffer+=chunk
            while b"\n" in buffer:
                line,buffer=buffer.split(b"\n",1)
                if not line: continue
                try:
                    request=decode_message(line)
                    result=service.execute(request["command"],request.get("data",{}))
                    response={"status":"ok","data":result}
                except (ValueError,KeyError,TypeError,json.JSONDecodeError) as exc:
                    response={"status":"error","error":str(exc)}
                try: conn.sendall(encode_message(response))
                except OSError: return

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        server.bind((HOST,PORT)); server.listen()
        print(f"Сервер кинотеатра запущен: {HOST}:{PORT}")
        try:
            while True:
                conn,address=server.accept()
                threading.Thread(target=handle_client,args=(conn,address),daemon=True).start()
        except KeyboardInterrupt: print("\nСервер остановлен.")
if __name__=="__main__": main()
