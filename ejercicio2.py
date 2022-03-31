alfabeto=('AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz')
texto=input("inserte una palabra: ")
contar=0

for i in texto:
    if i in alfabeto:
        contar+=1
    else:
        print('se ha encontrado caracteres no alfabeticos')
        break
if contar==len(texto):
    print('se ha encontrado caracteres alfabeticos')
            