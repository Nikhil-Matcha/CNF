import socket, requests

s = socket.socket()
ip= "127.0.0.1"

port=80
s.bind((ip,port))
print("Server is running with ip: ",ip, " and port ",port)
#listening for client to connect
s.listen(3)
print("Server is listening....")

while True:
    #establishing connection with client
    conn,addr=s.accept()
    #Receiving data from client
    data=conn.recv(1024).decode()
    #decoding to string format
    print(data)

    # Get the content of htdocs/index.html
    file = open("I:\\desktop\\msit\\NewFolder\\CNF\\Project\\index.html",encoding='utf-8')
    content = file.read()


    response="HTTP/1.1 200 Ok\n\n"+content
    headers=data.split('\n')
    print(headers[0])
    filename=headers[0].split()[1]
    print(filename)

    try:
        fin=open('I:\\desktop\\msit\\NewFolder\\CNF\\Project\\'+filename,encoding='utf-8')
        content=fin.read()
        fin.close()
        response="HTTP/1.1 200 Ok\n\n"+content
        conn.send(response.encode())
        
    except FileNotFoundError:
        if filename.split(".")[1] != 'html':
            response = 'HTTP/1.0 415 Unsupported Media Type:\n\n 415 Unsupported Media Type The server will not accept the request, because the media type is not supported'

        elif filename != '/index.html':
            response = 'HTTP/1.0 403 Forbidden Pages\n\n 403 Forbidden Pages You are not being allowed access, for whatever reason'

        else:
            response = 'HTTP/1.0 400 bad Request\n\n 400 bad Request Server does not recognize the URL'

    conn.sendall(response.encode())
    conn.close()
s.close()