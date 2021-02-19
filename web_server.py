import socket
import os

rootPath = "I:\\desktop\\msit\\NewFolder\\CNF\\Project\\CNF"

def geturl(request_data):
	temp = request_data.split(" ")[1]
	if(temp == "/") or temp == "/favicon.ico":
		return temp
	try:
		os.path.isdir(temp)
	except:
		return ""
	return temp

def get_files(path):
	files = []
	for file in os.listdir(path):
		files.append("<a href = \""+os.path.join(path, file) + "\"  > " + os.path.join(path, file).split("\\")[-1] +"</a> <br>")
	return ''.join(files)

HOST = ''
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)
print("Server started on port %s" %PORT)
print("Listening...")

while True:
    conn, addr = s.accept()
    reqData = conn.recv(1024).decode("UTF-8")
    # print(reqData)
    url = geturl(reqData)
    print(url)
    httpResponse = b""""""
    badRequest = b"""\
HTTP/1.1 400 BAD REQUEST
Content-Type: html;


<b><center><font color="red">BAD REQUEST</font></center></b>"""
    goodRequest = b"""\
HTTP/1.1 200 OK
Content-Type: html;


"""
    if reqData.split(" ")[0] != "GET" or url == "":
        httpResponse = badRequest
    else:
        if url == "/favicon.ico":
            pass
        elif url == "/":
            httpResponse = goodRequest + bytes(get_files(rootPath), 'UTF-8')
        elif os.path.isdir(url):
            httpResponse = goodRequest + bytes(get_files(url), 'UTF-8')
        else:
            httpResponse = goodRequest + bytes("""<b><center><font color="red">GOOD REQUEST</font></center></b>""", 'UTF-8')
    conn.sendall(httpResponse)