import pandas as pd
R=pd.read_csv
import hashlib
Q=hashlib.pbkdf2_hmac
X=hashlib.sha256
import binascii
import unicodedata
P=unicodedata.normalize
from Crypto.Cipher import PKCS1_OAEP
K=PKCS1_OAEP.new
from Crypto.PublicKey import RSA
E=RSA.import_key
A=RSA.generate
from Crypto.Hash import HMAC
D=HMAC.new
from struct import pack
def q(lang):
 if lang=='en':
  df=R('./lab4/en_words.txt',names=['words']).reset_index().set_index('words')
  nums=df.to_dict()['index']
 elif lang=='ua':
  df=R('./lab4/ua_words.txt',names=['words']).reset_index().set_index('words')
  nums=df.to_dict()['index']
 return nums
class w(object):
 def __init__(self,seed):
  self.index=0
  self.seed=seed
  self.buffer=b""
 def __call__(self,n):
  while len(self.buffer)<n:
   self.buffer+=D(self.seed+pack("<I",self.index)).digest()
   self.index+=1
  result,self.buffer=self.buffer[:n],self.buffer[n:]
  return result
def U(text,mnemonic):
 rsa=A(1024,randfunc=w(I(mnemonic)))
 public_key=rsa.public_key().export_key('PEM')
 print(f'PUBLIC KEY           : {public_key}')
 cipher=K(E(public_key))
 encrypted_text=cipher.encrypt(text)
 return encrypted_text
def f(encrypted_text,mnemonic):
 rsa=A(1024,randfunc=w(I(mnemonic)))
 private_key=rsa.export_key('PEM')
 print(f'PRIVATE KEY          : {private_key}')
 cipher=K(E(private_key))
 decrypted_text=cipher.decrypt(encrypted_text)
 return decrypted_text
class O(Exception):
def g(num_words:int)->int:
 try:
  return{12:128,15:160,18:192,21:224,24:256}[num_words]
 except KeyError:
  raise O("Invalid number of words provided, " "BIP39 mnemonic phrases are only specified for 12, 15, 18, 21, or 24 words.")
def n(phrase:str)->bytes:
 if not all(c in LETTERS for c in phrase):
  raise O(f"Invalid mnemonic phrase {repr(phrase)} provided, phrase contains an invalid character.")
 words=phrase.split()
 num_bits_entropy=g(len(words))
 num_bits_checksum=num_bits_entropy//32
 bits=0
 for word in words:
  bits<<=11
  try:
   bits|=WORD_TO_INDEX_TABLE[word]
  except KeyError:
   raise O(f"Invalid mnemonic phrase {repr(phrase)} provided, word '{word}' is not in the BIP39 wordlist.")
 checksum=bits&(2**num_bits_checksum-1)
 bits>>=num_bits_checksum
 data=bits.to_bytes(num_bits_entropy//8,byteorder="big")
 checksum_for_verification=X(data).digest()[0]>>(8-num_bits_checksum)
 if checksum!=checksum_for_verification:
  raise O(f"Invalid mnemonic phrase {repr(phrase)} provided, checksum invalid!")
 return data
def h(txt:str)->str:
 assert type(txt)is str
 return P("NFKD",txt)
def I(mnemonic:str,passphrase:str="")->bytes:
 n(mnemonic)
 mnemonic=h(mnemonic)
 passphrase="mnemonic"+h(passphrase)
 mnemonic_bytes=mnemonic.encode("utf-8")
 passphrase_bytes=passphrase.encode("utf-8")
 stretched=Q("sha512",mnemonic_bytes,passphrase_bytes,PBKDF2_ROUNDS)
 print(f'GENERATED SEED       : {stretched.hex()}')
 return stretched
LANG='ua'
LETTERS={'ua':" 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя",'en':" abcdefghijklmnopqrstuvwxyz"}[LANG]
WORD_TO_INDEX_TABLE=q(lang=LANG)
PBKDF2_ROUNDS=2048
if __name__=='__main__':
 text=b'Vladislav Zozulia'
 mnemonic='абсолютно абсолютно абсолютно абсолютно абсолютно абсолютно абсолютно абсолютно абсолютно абсолютно абсолютно автобус'
 print(f'MNEMONIC             : {mnemonic}')
 print(f'ORIGINAL TEXT        : {text}')
 print('----'*40)
 print('----'*19+'ENCRYPTION'+'----'*19)
 print('----'*40)
 encrypted_text=U(text,mnemonic)
 print(f'ENCRYPTED TEXT       : {encrypted_text.hex()}')
 print('----'*40)
 print('----'*19+'DECRYPTION'+'----'*19)
 print('----'*40)
 decrypted_text=f(encrypted_text,mnemonic)
 print(f'DECRYPTED TEXT       : {decrypted_text}')
 print('-----'*30)
# Created by pyminifier (https://github.com/liftoff/pyminifier)

