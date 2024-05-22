import socket

mapping = {
    "GORGE": "STOP",
    "PHREAK": "DROP",
    "FIRE": "ROLL"
}

def netcat(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.send(b'y\n')
        data = s.recv(1024)
        print('Received', data.decode('utf-8'))
        dat = data.decode('utf-8').split('\n')
        for i in range(1000):
            try: 
                dat_i = dat.index("What do you do? ") - 1 
            except: 
               print(":0")
            
            split_txt = dat[dat_i].split(", ")
            print(split_txt)
            text = ""

            for i in range(0,len(split_txt)):
                 if split_txt[i] in mapping.keys():
                     text += mapping.get(split_txt[i]) + "-"

            text = text[:-1]
            text += "\n"
            print(text)
            s.send(text.encode())
            data = s.recv(1024).decode("utf-8")
            dat = data.split("\n")
            print(data)
            
        s.shutdown(socket.SHUT_WR)

netcat('83.136.253.3',32713)

