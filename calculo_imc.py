nome = input("Qual o seu nome: ")
alt = float(input("Qual a sua altura: "))
kg = float(input("Qual o seu peso: "))
IMC = kg / (alt * alt)
print("Ola", nome, "seu IMC é", IMC)
print(f"Ola {nome} seu IMC é {IMC}")

if IMC < 17:
    print("Muito abaixo do peso")
elif IMC >= 17 and IMC <= 18.49:
    print("Abaixo do peso")
elif IMC >= 18.50 and IMC <= 24.99:
    print("Peso normal")
elif IMC >= 25 and IMC <= 29.99:
    print("Acima do peso")
elif IMC >= 30 and IMC <= 34.99:
    print("Obesidade 1")