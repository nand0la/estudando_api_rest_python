import requests 

cep = input("Digite seu CEP: ")
print()

r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

for k, v in r.json().items():
    print(f"{k}: {v}")
