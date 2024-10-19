### XOR Properties

""" In the last challenge, you saw how XOR worked at the level of bits. In this one, we're going to cover the properties of the XOR operation and then use them to undo a chain of operations that have encrypted a flag. Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator

Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

Let's break this down. Commutative means that the order of the XOR operations is not important. Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf  """

""" HINT: Before you XOR these objects, be sure to decode from hex to bytes """

KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')

KEY2_xor_KEY1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')

KEY2_xor_KEY3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')

FLAG_xor_KEY1_xor_KEY3_xor_KEY2 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')


# XOR KEY1 and KEY2_xor_KEY1 to get KEY2
KEY2 = bytes(a ^ b for a, b in zip(KEY1, KEY2_xor_KEY1))

# XOR KEY2 and KEY2_xor_KEY3 to get KEY3
KEY3 = bytes(a ^ b for a, b in zip(KEY2, KEY2_xor_KEY3))

# XOR KEY1 and FLAG_xor_KEY1_xor_KEY3_xor_KEY2 to get FLAG_xor_KEY3_xor_KEY2
FLAG_xor_KEY3_xor_KEY2 = bytes(a ^ b for a, b in zip(KEY1, FLAG_xor_KEY1_xor_KEY3_xor_KEY2))

# XOR KEY2 and FLAG_xor_KEY3_xor_KEY2 to get FLAG_xor_KEY3
FLAG_xor_KEY3 = bytes(a ^ b for a, b in zip(KEY2, FLAG_xor_KEY3_xor_KEY2))

# XOR KEY3 and FLAG_xor_KEY3 to get FLAG
FLAG = bytes(a ^ b for a, b in zip(KEY3, FLAG_xor_KEY3))

print(FLAG.decode('utf-8'))


