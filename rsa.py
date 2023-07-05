import random


def mod_inv(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = mod_inv(b % a, a)
        return (g, x - (b // a) * y, y)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keyPairs():
    p = 7
    q = 5

    n = p * q

    phi = (p - 1) * (q - 1)

    e = random.randint(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)


    d = mod_inv(e, phi)[1]
    if d < 0:
        d += phi

    return ((e, n), (d, n))


def decrypt(ctext, private_key):
    d, n = private_key
    text = []
    for char in ctext:
        text.append(pow(char, d, n))
    return text


def encrypt(text, public_key):
    e, n = public_key
    ctext = []
    for i in text:
        ctext.append(pow(i, e, n))
    return ctext


public_key, private_key = generate_keyPairs()
print("Public: ", public_key)
print("Private: ", private_key)

ctext = encrypt([45], public_key)
print("encrypted  =", ctext)
plaintext = decrypt(ctext, private_key)
print("decrypted =", plaintext)

