from pytea import TEA
import os

key = os.urandom(16)
print('key is: ', key)
content = 'hola'
tea = TEA(key)
e = tea.encrypt(content.encode())
print('e: ', e)
print('encrypt hex:', e.hex())
d = tea.decrypt(e)
print('decrypt:', d.decode())