numero_1 = int(input("informe o primeiro numero "))
numero_2 = int(input("informe o segundo numero "))
operador = input("informe o operador \n+ adicao \n- subtracao \n* multiplicacao \n/ divisao \n=> ")
if operador == "+":
    resultado = numero_1 + numero_2
    print(f"resultado {resultado}")
elif operador == "-":
    resultado = numero_1 - numero_2
    print(f"resultado {resultado}")
elif operador == "*":
    resultado = numero_1 * numero_2
    print(f"resultado {resultado}")
elif operador == "/":
    resultado = numero_1 / numero_2
    print(f"resultado {resultado}")
else:
    print("escolha uma das 4 opcoes")

    def soma(a, b):
        return a + b
    def subtracao (a, b):
        return a - b
    def divisao(a, b):
        if b !=0:
             return a / b
        else:
             return "Nao e possvel..."

    def multiplicacao(a, b):
        if b !=0:
            return a * b
        else:
            return "Nao e possvel..."