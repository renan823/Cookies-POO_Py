import time

class Cookie:
    def __init__(self, sabor, cobertura = False):

        self.sabor = sabor
        self.cobertura = cobertura

    def assando(self):
        print()
        if (self.cobertura == False):
            print(f"Pronto! Aproveite seu cookie de {(self.sabor).lower()}!")
        else:
            print(f"Pronto! Aproveite seu cookie de {(self.sabor).lower()} com cobertura de {(self.cobertura).lower()}!")     

def exibir(lista):
    valor = 1
    for item in lista:
        print(f"{valor} - {item}")
        valor = valor + 1
        
sabores = ['Chocolate', 'Baunilha', 'Morango']
coberturas = ['Gotas de chocolate', 'Doce de leite', 'Nutella', 'Confete']


print("--LOJA DE COOKIES--")
print()
print("Digite o valor do sabor desejado: ")
exibir(sabores) 
acao = -1
while(len(sabores) < acao or 0 > acao):
    acao = int(input("Digite o valor do sabor: "))
sabor = sabores[acao - 1]

print()
valores = ['S', 'N']
achou = False
while(achou == False):
    addcobertura = str(input("Quer cobertura ? (S/N): ")).upper()
    if addcobertura in valores:
        achou = True
    else:
        achou = False

if(addcobertura == 'S'):
    print()
    print("Digite o valor da cobertura desejada: ")
    exibir(coberturas)

    cobertura = -1
    while(len(coberturas) < cobertura or 0 > cobertura):
        cobertura = int(input("Digite o valor da cobertura: "))
    cobertura = coberturas[cobertura - 1]
else:
    cobertura = False
    
cookie = Cookie(sabor, cobertura)
print()
print("Seu cookie está sendo preparado, aguarde!")
time.sleep(10)
cookie.assando()

