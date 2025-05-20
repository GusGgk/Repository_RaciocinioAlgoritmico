"""CRIAÇÃO DE DICIONARIO"""
users = {
    "005111560106106": "Maicris Fernandes",
    "1413366717717161": "Monitor Gostosão",
}

print(users["005111560106106"]) #Resposta Maicris Fernandes

users["005111560106106"] = "Maicris"
print(users["005111560106106"]) # Resposta Maicris

if "111111111" in users:
    print(users["111111111"])