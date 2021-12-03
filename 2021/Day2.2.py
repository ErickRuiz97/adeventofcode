import csv
class reto:
  def main(self):
    totalF = 0
    totalD = 0
    totalU = 0
    resulFinal = 0
    profundidad = 0
    centinela = 0
    with open ('movimientos.csv', newline="") as convertido:
      reader = csv.DictReader(convertido)
      for row in reader:
        if(row['mov']=='forward'):
          totalF += int(row['numero'])
          if(totalD != 0 | totalU != 0):
            profundidad += int(row['numero']) * centinela
        if(row['mov'] == 'down'):
          totalD += int(row['numero'])
          centinela += int(row['numero'])
        if(row['mov'] == 'up'):
          totalU += int(row['numero'])
          centinela -= int(row['numero'])
    resulFinal = totalF * profundidad
    print(resulFinal)

inicio = reto()
inicio.main()