temperatura = int(input("Digite a temperatura: "))

if temperatura < 10:
    print(f"Está muito frio.")
elif temperatura > 10 and temperatura < 24:
    print(f"Está agradável.")
elif temperatura > 25 and temperatura < 30:
    print("Está quente.")
elif temperatura > 30:
    print("Está muito quente.")