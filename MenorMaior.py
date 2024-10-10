valor = float(input("Me fale um primeiro valor \n"))
valor2 = float(input("Me fale um segundo valor \n"))
valor3 = float(input("Me fale um terceiro valor \n"))

maior_valor = valor

if maior_valor < valor2:
    maior_valor = valor2
if maior_valor < valor3:
    maior_valor = valor3

menor = valor
if menor > valor2:
    menor = valor2
if menor > valor3:
    menor = valor3

print(f"Seu maior valor é o:{maior_valor}")
print(f"Seu menor valor é o:{menor}")