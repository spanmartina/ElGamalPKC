# ElGamal PKC
# TSI project --- Martina Span

import random
from math import pow
import sympy

#computes the greatest common denominator of a and b,  assumes a > b
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Modular exponentiation
#a-base, b-exp, c-modulus
def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

# Generating large random numbers
def gen_key(p):
    key = random.randint(1, (p - 1) // 2)
    #the key keeps being randomly selected until the condition gcd(q,p)=1 is satisfied
    while gcd(p, key) != 1:
        key = random.randint(1, (p - 1) // 2)
    return key

#finds a primitive root for prime p
def find_primitive_root(p):
    p1 = (p-1) // 2
    while 1:
        g = random.randint(2, p - 1)
        if not power(g, (p-1)//2, p) == 1:
            if not power(g, (p-1)//p1, p) == 1:
                return g

# Asymmetric encryption
def encrypt(msg, p, g, h):
    en_msg = []
    # Private key selected by Bob (1 <= k < p)
    k = gen_key(p)  # Private key for sender
    # k = random.randint(2, (p - 1))
    print("Bob alege cheia secreta: ", k)
    gk = power(g, k, p)  # C1
    gxk = power(h, k, p) # for C2

    # transform message in array
    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    print("g^k used : ", gk)
    print("g^ak used : ", gxk)
    for i in range(0, len(en_msg)):
        # C2 = M* h^k(mod p)
        en_msg[i] = gxk * ord(en_msg[i]) #ord - convert a single Unicode character to its integer equivalent

    return gk, en_msg, #Send C1 C2


def decrypt(C1, en_msg, p, g, key):
    # C2 * (C1^key)^-1 mod p
    # en_msg = (C1^key)^-1 mod p
    dr_msg = []
    h = power(C1, key, p)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i] / h))) # / cause it's raised to the power -1
    return dr_msg

def main():
    #Alice prepares the channel for communication
    n = input('Enter the number of bits for the prime number: ')
    p = sympy.randprime(pow(2, int(n)-2), pow(2, int(n)-1))
    print('The prime number: ', p)
    g = find_primitive_root(p)
    print('The generator: ', g)

    #Alice(receivers) private key
    x = gen_key(p)
    # x = random.randint(1, (p - 1))

    h = power(g, x, p)  # g^x mod p, 1 <= key < p
    print("Alice secret key:", x)
    print('_______________________________________')
    print('COMMUNICATION CHANNEL')
    print('Public Key (p,g,h)')
    print('p : ', p)
    print('g : ', g)
    print('h : ', h)
    print('_______________________________________')


    #Bob receives the public key from the communication channel
    msg = str(input('Input the message Bob want to send: '))

    #Bob encrypt the message
    C1, en_msg = encrypt(msg, p, g, h)
    print('_______________________________________')
    print('COMMUNICATION CHANNEL')
    print('C1: ', C1)
    print('C2: ', en_msg)
    print('_______________________________________')

    #Alice decrypts the message
    dr_msg = decrypt(C1, en_msg, p, g, x)
    dmsg = ''.join(dr_msg)
    print("Decrypted Message :", dmsg)

if __name__ == '__main__':
    main()