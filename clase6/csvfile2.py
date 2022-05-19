import csv
import os
import time

start = time.time()

os.system('cls')
ruta = "C:\\Users\\tavodev\\Desktop\\python_intermedio_github\\clase6\\practica\\"

with open('console_games.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"plataforma => {row['Platform']} año=> {row['Year']}")
        
        try:
            if row['Platform']:
                os.makedirs(f"{ruta}{row['Platform']}\\{row['Year']}")

        except FileExistsError as ex:
            pass

        if row['Platform']:
            ruta_archivo = f"{ruta}{row['Platform']}\\{row['Year']}\\archivo.txt"
            cadena = ''

            for key, value in row.items():
                cadena += value + ","

            cadena += "\n"

            with open(ruta_archivo, 'a') as archivo:
                archivo.write(cadena)

end = time.time()

print(end - start)
# id | Rank | Name | Platform | Year | Genre | Publisher | NA_Sales | EU_Sales | JP_Sales | Other_Sales

# Estructura de directorios

# Plataforma / Year / archivo.txt
# Nintendo/2000/videogames.txt
# en el archivo debe de ir el contenido de esa plataforma y ese año