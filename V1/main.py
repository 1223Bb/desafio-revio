import requests
import json

allCitiesURL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios"

# Get all cities in São Paulo
allCitiesAPIResponse = requests.get(allCitiesURL).json()


# Create a dict where each key corresponds to a city. ID : Name
allCitiesDict = [{"id": city["id"], "nome": city["nome"]} for city in allCitiesAPIResponse]

# Empty arrays which will contain cities where Gabriel appears in top ten, and also
citiesWithGabrielInTopTen = []
gabrielEntries=[]

# For every city that we found...
for city in allCitiesDict:
    print(f"Buscando IBGE API cidade {city['nome']}")
    print(f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade={city['id']}")
    testResponse = requests.get((f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade={city['id']}")).json()
    topNames = [{"rank": name["ranking"], "frequencia": name["frequencia"], "nome": name["nome"]} for name in testResponse[0]["res"]]
    print(topNames)
    if(any(name["nome"] == "GABRIEL" for name in topNames[:10])):
        gabriel_entry = next((item for item in topNames if item["nome"] == "GABRIEL"), None)
        gabrielEntries.append(gabriel_entry)
        citiesWithGabrielInTopTen.append(city['nome'])

citiesWithFrequency = {city: name["frequencia"] for city, name in zip(citiesWithGabrielInTopTen, gabrielEntries)}

# Sorting in desc order
citiesWithFrequencyInDescendingOrder = dict(sorted(citiesWithFrequency.items(), key=lambda entry: entry[1], reverse=True))

print(citiesWithFrequencyInDescendingOrder)


with open("output.json", "w", encoding="utf-8") as f:
    json.dump(citiesWithFrequencyInDescendingOrder, f, ensure_ascii=False, indent=4)
