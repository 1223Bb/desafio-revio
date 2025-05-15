import requests

class Fetcher:
    def __init__(self):
        pass
    def fetch(self, url):
        return requests.get(url)

class IBGEAPI:
    def __init__(self):
        pass
    def fetchAllCitiesInSP(self):
        fetcher = Fetcher()
        allCitiesURL = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/SP/municipios"
        return fetcher.fetch(allCitiesURL).json()
    def fetchTopNamesInCity(self, id):
        fetcher = Fetcher()
        URL = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking?localidade={id}"
        response = fetcher.fetch(URL).json()
        return [{"rank": name["ranking"], "frequencia": name["frequencia"], "nome": name["nome"]} for name in response[0]["res"]]

