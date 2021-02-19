import socket
import os
import filetype

from _thread import *
import threading

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
    newPath = rootPath + "\\" + path[1:]
    files = []
    for file in os.listdir(newPath):
        files.append("<a href = \"" + path + "/" + file + "\"  > " + file + "</a> <br>")
    return ''.join(files)

def myThread(connection):
    handleRequest(connection)

def handleRequest(conn):
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
            httpResponse = goodRequest + bytes(get_files(""), 'UTF-8')
        elif os.path.isdir(rootPath + url):
            httpResponse = goodRequest + bytes(get_files(url), 'UTF-8')
        elif os.path.isfile(rootPath + url):
            x = filetype.guess(rootPath + url)
            contentType = ""
            if x is None:
                contentType = "/text"
            else:
                contentType = x.mime
            f = open(rootPath + url, encoding="UTF-8", errors='ignore')
            s1 = f.read()
            httpResponse = goodRequest + bytes(contentType, "UTF-8")+b""";


""" + bytes(s1, "UTF-8")
        else:
            httpResponse = badRequest
    conn.sendall(httpResponse)

HOST = ''
PORT = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(5)
print("Server started on port %s" %PORT)
print("Listening...")

while True:
    conn, addr = s.accept()
    start_new_thread(myThread, (conn, ))