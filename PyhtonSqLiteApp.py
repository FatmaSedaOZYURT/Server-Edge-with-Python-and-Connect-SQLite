#Author = Fatma Seda OZYURT
#Information = This project`s purpose is for take a data from the other pc as server and store the data in SQLite
import socketserver
import sqlite3

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print ("{} wrote: ".format(self.client_address[0]))
        print (self.data)
        self.request.sendall(self.data.upper())
        
        # start split the taken data
        Input = format(self.data)
        Input1 = (Input).split("'", 2)
        Input2 = (Input1[1]).split(" ", 2)

        name = Input2[0]
        surName = Input2[1]
        info = Input2[2]

        ##Database connect
        conn=sqlite3.connect('C:\\Users\Win32\Desktop\Connect_SEDA.db')
        c = conn.cursor()

        c.execute("INSERT INTO Connect (Name, SurName, Information) VALUES (?, ?, ?)", (name, surName, info))
        conn.commit()

        c.close()
        conn.close()



if __name__ == "__main__":
    HOST, PORT = "192.168.211.130", 7000 #HOST=Your Ip Address , PORT=Your Port

    server =  socketserver.TCPServer((HOST,PORT), MyTCPHandler, True) #baglanti icin ~ for connection
    server.serve_forever()