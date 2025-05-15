import json
import os
from classes import IBGEAPI

def SaveObjToJSONFile(object, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(object, f, ensure_ascii=False, indent=4)

api = IBGEAPI()

print("Pegando cidades de São Paulo...")
allCitiesInSP = api.fetchAllCitiesInSP()
allCitiesDict = [{"id": city["id"], "nome": city["nome"]} for city in allCitiesInSP]

print("Cidades de São Paulo e IDS, como o desafio pede:")
print(allCitiesDict)

citiesWithGabrielInTopTen = []
gabrielEntries=[]

for city in allCitiesDict:
    print(f"Pegando rank de nomes da cidade de {city["nome"]}")
    topNames = api.fetchTopNamesInCity(city['id'])
    if(any(name["nome"] == "GABRIEL" for name in topNames[:10])):
        print(f"Gabriel aparece no top 10! ({city["nome"]})")
        gabrielEntry = next((item for item in topNames if item["nome"] == "GABRIEL"), None)
        gabrielEntries.append(gabrielEntry)
        citiesWithGabrielInTopTen.append(city['nome'])

citiesWithFrequency = {city: name["frequencia"] for city, name in zip(citiesWithGabrielInTopTen, gabrielEntries)}

citiesWithFrequencyInDescendingOrder = dict(sorted(citiesWithFrequency.items(), key=lambda entry: entry[1], reverse=True))

currentDirectory = os.path.dirname(os.path.abspath(__file__))
outputPath = os.path.join(currentDirectory, "resultado.json")
print(f"Salvando arquivo em {currentDirectory}...")
SaveObjToJSONFile(citiesWithFrequencyInDescendingOrder, outputPath)
print(f"Pronto! Arquivo disponível em {outputPath}")