from Crypto.Util.number import long_to_bytes
import socket

def get_variables_from_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    data = s.recv(4096).decode().strip().split('\n')
    s.close()
    
    variables = {}
    for line in data:
        if ': ' in line:
            print(line)
            key, value = line.split(': ')
            variables[key.strip()] = value.strip()
    
    return variables


host = 'verbal-sleep.picoctf.net'
port = 51510
variables = get_variables_from_server(host, port)


N = int(variables['N'])
e = int(variables['e'])
c = int(variables['cyphertext'])


q = N // 2
phi_N = q - 1
d = pow(e, -1, phi_N)


m = pow(c, d, N)
flag = long_to_bytes(m)

print("flag:", flag.decode())
