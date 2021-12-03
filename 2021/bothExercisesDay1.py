import csv
class diaUno:
  def main(self, iniciador):
    contador = 0
    centinela = 0
    continuar = True
    sumatoria = 0
    size = 2
    sumatoriaTemporal = 0
    finalizar = 2
    with open ('submarino.csv', newline="") as convertido:
      reader = list(csv.reader(convertido))
      while(continuar == True):
        primera = 0
        segunda = 0 
        tercera = 0
        contador = 0
        for row in range(iniciador, len(reader)):
          contador += 1
          if(contador == 1):
            primera = int("".join(reader[row]))
          if(contador == 2):
            segunda = int("".join(reader[row]))
          if(contador == 3):
            tercera = int("".join(reader[row]))
            sumatoria = primera + segunda + tercera
            if(sumatoria > sumatoriaTemporal):
              centinela += 1
            sumatoriaTemporal = sumatoria
            print(sumatoria)
            finalizar += 1
            iniciador += 1
            size = len(reader)
            if(finalizar == size):
              continuar = False
            break
            

      
contadorFinal = 0
comparador = 0
iniciador = 0
comenzar = diaUno()
comenzar.main(iniciador)
