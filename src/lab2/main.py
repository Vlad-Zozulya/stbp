import aes, os

text = b'Vladislav Zozulia'

# key = os.urandom(16)
key = b"\x02\xc6\x0c\xde}\xc1\x87S\xae\xb6\x04\xd8'\xa2\xc5z"

# iv = os.urandom(16)
iv = b"*'\xd4\xb0\x85\xa4\x17N\x05\xd9z\xcc\x88^\xda("

encrypted = aes.AES(key).encrypt_ctr(text, iv)


print(f'TEXT                   :{text}')
print(f'TEXT IN BYTES          :{text.hex()}')
print(f'KEY                    :{key.hex()}')
print(f'IV                     :{iv.hex()}')
print(f'ENCRYPTED              :{encrypted.hex()}')

decrypted = aes.AES(key).decrypt_ctr(encrypted, iv)
print(f'DECRYPTED              :{decrypted}')
print(f'DECRYPTED IN BYTES     :{decrypted.hex()}')
