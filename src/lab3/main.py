from my_rsa import RSA, RSAKey
import rsa

def my_rsa(text, bits):
    key = RSAKey(bits=bits)
    public_key = (key.e, key.N)
    private_key = (key.d, key.N)

    print(f'MY_RSA: public_key       : {public_key}')
    print(f'MY_RSA: private_key      : {private_key}')
    cipher = RSA(key)

    encrypted = cipher.encrypt_data(text.encode())

    print(f'MY_RSA: Original text    : {text}')
    print(f'MY_RSA: Encrypted text   : {encrypted.hex()}')

    decrypted = cipher.decrypt_data(encrypted)
    print(f'MY_RSA: Decrypted text   : {decrypted.decode()}')


def rsa_lib(text, bits):
    public_key, private_key = rsa.newkeys(bits)
    print(f'RSA_LIB: public_key       : {public_key}')
    print(f'RSA_LIB: private_key      : {private_key}')

    encrypted = rsa.encrypt(text.encode(), public_key)

    print(f'RSA_LIB: Original text     : {text}')
    print(f'RSA_LIB: Encrypted text    : {encrypted.hex()}')

    decrypted = rsa.decrypt(encrypted, private_key)

    print(f'RSA_LIB: Decrypted text    : {decrypted.decode()}')


if __name__ == '__main__':
    TEXT = 'Vladislav Zozulia'
    BITS = 1024

    my_rsa(TEXT, BITS)
    print('---'*30)
    print('---'*30)
    print('---'*30)
    rsa_lib(TEXT, BITS)
