import socket
import subprocess

SERVER_PORT = 8000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', SERVER_PORT))
server_socket.listen()
print('Listening on port %s ...' % SERVER_PORT)

while True:    
    client_connection, client_address = server_socket.accept()  # 클라이언트 접속할때까지 대기
    request = client_connection.recv(1024).decode()    # 브라우져가 보낸 데이터 1024 byte읽기
    
    headers = request.split('\n')     # GET /svr?query=34  HTTP/1.1       <-- headers[0]  
    data = headers[0].split()[1][1:]  # /svr?query=34  
    service = data.split("?")[0]      # /svr 
    if len(data.split("?")) == 1 :    # 파라미터가 명시되지 않았으면
        parameter = ""      
    else :
        parameter = data.split("?")[1]   # query=34 
    
    client_connection.send('HTTP/1.0 200 OK\n\n'.encode())    # 헤더를 브라우져로 보냄
    html = "<h1> Hello Server Programming</h1>";              # 본문 출력 
    html += "<h3> service : " +  service + "</h3>"
    html += "<h3> input paramter : " +  parameter + "</h3>"
    
    client_connection.send(html.encode())                     # 데이터를 브라우져로 보냄 
    client_connection.close()                                 # 브라우져 접속 끊기

server_socket.close()