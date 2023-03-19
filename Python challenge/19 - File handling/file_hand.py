# Manejo de archivos
# (.txt, .json, .xml, .csv, .tsv, .excel)

'''
"r" - read - Valor predeterminado. Abre un archivo para lectura, devuelve un error si el archivo no existe
"a" - append - Abre un archivo para agregar, crea el archivo si no existe
"w" - wright - Abre un archivo para escribir, crea el archivo si no existe
"x" - Create - Crea el archivo especificado, devuelve un error si el archivo existe
"t" - Text - Valor por defecto. Modo de texto
"b" - Binary - Modo binario (por ejemplo, imágenes)
'''

# read 

f = open('test.txt')
#print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

### Un archivo abierto debe cerrarse con el método close() .

'''
Después de abrir un archivo, debemos cerrarlo. Hay una alta tendencia a olvidarse de cerrarlos. 
Hay una nueva forma de abrir archivos usando with - cierra los archivos por sí mismo. 
Reescribamos el ejemplo anterior con el método with : '''
with open ('test.txt') as f:
    lines = f.readlines()
    #print(lines)
    

#JSON
 
# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"JUAN",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''


import json
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

#Archivo con extensión xlsx
#Para leer archivos de Excel necesitamos instalar el paquete xlrd . 
# Cubriremos esto después de que cubramos la instalación del paquete usando pip.

import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)


##### Exercises: Day 19- file handling ########
