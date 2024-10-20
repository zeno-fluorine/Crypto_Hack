### You either know, XOR you don't

""" I've encrypted the flag with my secret key, you'll never be able to guess it.
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104 """

""" HINT: Remember the flag format and how it might help you in this challenge!
Flag format: crypto{FLAG} """


secret = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

Crypto = bytes([0x63, 0x72, 0x79, 0x70, 0x74, 0x6F, 0x7B])

KEY = bytes(a ^ b for a, b in zip(secret, Crypto))
print(KEY)

# Character to add as a byte
extra_char = b'y'

# Create a new KEY by appending the extra character
KEY = KEY + extra_char

# Repeat the key until it matches the length of secret
KEY = (KEY * (len(secret) // len(KEY) + 1))[:len(secret)]

FLAG = bytes(a ^ b for a, b in zip(secret, KEY))
print(FLAG)
