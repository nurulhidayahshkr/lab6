import socket
import sys
import math
import errno
import time
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("\nCalculator for (LOG, SQUARE ROOT, EXPONENTIAL)\n Please insert: log/sqrt/exp <number>\n Example: exp 20 \n\t\tType 'exit' to exit"))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            operation, value = data.split()
            op = str(operation)
            num = int(value)

            if op[0] == 'l':
                op = 'Log'
                answer = math.log10(num)
            elif op[0] == 's':
                op = 'Square root'
                answer = math.sqrt(num)
            elif op[0] == 'e':
                op = 'Exponential'
                answer = math.exp(num)
            else:
                answer = ('INVALID')

            sendAnswer = (str(op) + '(' + str(num) + ') = ' + str(answer))
            print ('successful!')
        except:
            print ('Invalid input')
            sendAnswer = ('Invalid input')

        if not data:
            break
        s_sock.send(str.encode(sendAnswer))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8828))
    print("listening...")
    s.listen(28)

    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

            except Exception as e:
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
           s.close()

