from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time


class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, "rb") as file:
            file_data = file.read()
            #encriptacion
        datos_encriptados = self.encrypt(file_data, self.key)
        with open(file_name + ".aes", 'wb') as file:
            file.write(datos_encriptados)
        os.remove(file_name)
        
    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, "rb") as file:
            datos_encriptados = file.read()
        datos = self.decrypt(datos_encriptados,self.key)
        with open(file_name[:-4], 'wb') as file:
            file.write(datos)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'C:/Users/Luis/Desktop/aes password/AES-256/descifrar hola.txt.aes'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
aes = Encryptor(key)
clear = lambda: os.system('cls')

if os.path.isfile('C:/Users/Luis/Desktop/aes password/AES-256/hola.txt.aes'):
    while True:
        print("python3\nse ejecutara el programa cifrado_aes256.py\ndescifrar el archivo hola.txt.aes\n")
        password = str(input("Introdusca la contraseña: "))
        aes.decrypt_file("C:/Users/Luis/Desktop/aes password/AES-256/hola.txt.aes")
        os.rename("C:/Users/Luis/Desktop/aes password/AES-256/hola.txt","C:/Users/Luis/Desktop/aes password/AES-256/hola_descifrado.txt")
        #secundaria 93
        break
    while True:
        clear()
        opcion = int(input(
            "1. Cifrar archivo.\n2. Desencriptar archivo.\n3. Cifrar todos los archivos de la misma direccion.\n4. Descifrar todos los archivos de la direccion.\n5. Salir.\n"))
        clear()
        if opcion == 1:
            aes.encrypt_file("C:/Users/Luis/Desktop/aes password/AES-256/"+str(input("Ingrese el nombre del archivo para cifrar: ")))
        elif opcion == 2:
            aes.decrypt_file("C:/Users/Luis/Desktop/aes password/AES-256/"+str(input("Ingrese el nombre del archivo para descifrar: ")))
        elif opcion == 3:
            aes.encrypt_all_files()
        elif opcion == 4:
            aes.decrypt_all_files()
        elif opcion == 5:
            exit()
        else:
            print("Selecciona una opcion valida")

else:
    while True:
        clear()
        print("python3\nse ejecutara el programa cifrado_aes256.py\ncifrar el archivo hola.txt\n")
        password = str(input("Ingrese una contraseña para cifrar. "))
        repassword = str(input("Confirme la contraseña: "))
        if password == repassword:
            break
        else:
            print("Las contraseñas no coinciden")
    
    aes.encrypt_file("C:/Users/Luis/Desktop/aes password/AES-256/hola.txt")
    print("Vuelve a ejecutar el programa para desencriptar (Reinicia)")
    time.sleep(15)



