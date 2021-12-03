import csv
class reto:
  def main(self):
    totalF = 0
    totalD = 0
    totalU = 0
    finalProfundidad = 0
    resulFinal = 0
    with open ('movimientos.csv', newline="") as convertido:
      reader = csv.DictReader(convertido)
      for row in reader:
        print(row['mov'])
        if(row['mov']=='forward'):
          totalF += int(row['numero'])
        if(row['mov'] == 'down'):
          totalD += int(row['numero'])
        if(row['mov'] == 'up'):
          totalU += int(row['numero'])
    finalProfundidad = totalD - totalU
    resulFinal = totalF * finalProfundidad
    print(resulFinal)

inicio = reto()
inicio.main()