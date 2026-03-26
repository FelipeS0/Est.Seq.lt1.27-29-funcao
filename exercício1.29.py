#Declaração de Variáveis 
Pou1: int = 0
Ren2: int = 0
Aux: int = 0
Valor: float = 0.0
Valor_cor: float = 0.0

#Início
Valor = float(input("Qual o valor do investimento?"))
Aux =  int(input(" Qual o tipo de investimento? 1 = poupança e 2 = renda fixa"))
def main(escolha, poupança, renda_fixa):
   if escolha == 1: 
    Valor_cor = (poupança + (poupança * 0.03 ))
    print ("Seu valor corrigido    será:", Valor_cor)
   elif escolha == 2:
    Valor_cor = (renda_fixa + float(renda_fixa * 0.05))
    print ("Seu valor corrigido    será:", Valor_cor)
   else:
    print ("Não foi possível determinar o investimento desejado, tente novamente")
if __name__ == "__main__":
    resultado = main(Aux, Valor, Valor)
#fim