#Declaração de Variáveis
vol: int = 0
ext_circuito: int = 0
ext_circuito_km: int = 0
tempo: int = 0
tempoH:int = 0
vel_M: float = 0.0

#Início
vol = int(input("Qual o total de voltas dadas?"))
ext_circuito = int(input("Qual o total do tamanho do circuito?"))
tempo = int(input("Qual o total de tempo?"))

ext_circuito_km = (vol * ext_circuito) /1000
tempoH = tempo /60
 
def main(Ext_circ_KM, TempoHo,):
 vel_M = Ext_circ_KM / TempoHo
 return vel_M
if __name__ == "__main__":
    resultado = main(ext_circuito_km, tempoH)
    print("A velocidade média é:", round(resultado, 2), "km/h")

 
 
