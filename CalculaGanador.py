import csv
from UnleashClient import UnleashClient
from decimal import *

# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con el texto "segunda vuelta"
# el DNI debe ser valido (8 digitos)
class CalculaGanador:

    def leerdatos(self):
        data = []
        with open('0204.csv', 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                data.append( fila)
        return data
    #for candidato in votosxcandidato:
    #    print('candidato: ' + candidato + ' votos validos: ' + str(votosxcandidato[candidato]))

    def calcularvotos(self, data, client):
        votosxcandidato = {}
        for fila in data:
            nombrecandidato = fila[4]
            if not nombrecandidato in votosxcandidato:
                votosxcandidato[nombrecandidato] = 0
            if fila[5] == '1' and len(fila[3]) == 8:
                votosxcandidato[nombrecandidato] = votosxcandidato[nombrecandidato] + 1
        return votosxcandidato

    def seleccionarganador(self, votosxcandidato, client):
        maxvotos = 0
        candidatoganador = ''
        votosvalidos = 0
        #app_context = {"userId": "cpaztrillo@gmail.com"}
        #isnuevocalculo = client.is_enabled("demofeature", app_context)
        isnuevocalculo = True
        if(isnuevocalculo):
            print ("usando nuevo calculo")
            for candidato in votosxcandidato:
                votosvalidos = votosvalidos + votosxcandidato[candidato]
            sorted_x = sorted(votosxcandidato.items(), key=lambda kv: kv[1], reverse=True)
            if sorted_x[0][1] >  0.5*votosvalidos:
                return [sorted_x[0][0]]
            return ['Segunda Vuelta']
            [sorted_x[0][0], sorted_x[1][0]]
        else:
            for candidato in votosxcandidato:
                votosvalidos = votosvalidos + votosxcandidato[candidato]
                if votosxcandidato[candidato] > maxvotos:
                    candidatoganador = candidato
                    maxvotos = votosxcandidato[candidato]
            if maxvotos > 0.5*votosvalidos:
                return [candidatoganador]
            return ['Segunda Vuelta']

    def calcularganador(self, data, client):
        votosxcandidato = self.calcularvotos(data, client)
        return self.seleccionarganador(votosxcandidato, client)

#client = UnleashClient(
#    url="http://localhost:4242/api",
#    app_name="my-python-app",
#    custom_headers={'Authorization': 'default:development.unleash-insecure-api-token'}
#    )

#client.initialize_client()
client = 0

c = CalculaGanador()
#c.calcularvotos(c.leerdatos())
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
print(c.calcularganador(datatest, client))
