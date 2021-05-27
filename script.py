import webbrowser
import time
from pytea import TEA
import os

# Cifrar el mensaje

key = os.urandom(16) 
print('key is: ', key)
content = 'hola' # Texto que se quiere cifrar
tea = TEA(key)
e = tea.encrypt(content.encode())
print('encrypt hex:', e.hex())
d = tea.decrypt(e)
print('decrypt:', d.decode())

# Variables que ayudan a mantener mas limpio el codigo del contenido del html

title = "Tarea 3: Cifrado en produccion"
message = "Este sitio contiene un mensaje secreto"
cifrado = e.hex()
password = key

# Esta linea es lo que va a contener nuestro html

html_content = f"""<html> <head> </head> <h1> {title} </h1> <body> </body> <p>{message}</p> <div class="algorithm" id="msg_cifrado" <p hidden>{cifrado}</p><p hidden>{password}</p></div> </html>
<script src="./tea.js"></script>
<script src="./node.js"></script>
<script src="./monki.js"></script>"""

with open("index.html", "w") as html_file:
    html_file.write(html_content)
    print("Html file created")

# Abrir la pagina en una nueva ventana

time.sleep(2)
webbrowser.open_new_tab("index.html")