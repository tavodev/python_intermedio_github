import csv

with open('console_games.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Platform'])

# id | Rank | Name | Platform | Year | Genre | Publisher | NA_Sales | EU_Sales | JP_Sales | Other_Sales

# Estructura de directorios

# Plataforma / Year / archivo.txt
# Nintendo/2000/videogames.txt
# en el archivo debe de ir el contenido de esa plataforma y ese año