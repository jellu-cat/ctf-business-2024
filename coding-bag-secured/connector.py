from pwn import *

def answer(data):
    script = './sol.py'

    result = subprocess.run(
        ['python', script, data],
        capture_output=True,
        text=True)
    print("-->", result.stderr)
    print("-->", result.args)
    print("-->", result.stdout)
    return result.stdout

p = remote('83.136.251.226', 41262)

while True:
    data = p.recv().decode('utf-8')
    for i in range(100):
        data = p.recv().decode('utf-8')
        # print(data)

        index = data.find("/100")
        result = data[index + len("/100"):]
        # print(result)
        message = answer(result)
        print("--->", message)
        p.send(message.encode())
        # print(f"Sended: {message}")
