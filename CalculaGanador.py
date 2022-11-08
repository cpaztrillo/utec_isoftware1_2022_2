import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos
# que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
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

    def calcularvotos(self, data):
        votosxcandidato = {}
        for fila in data:
            if not fila[4] in votosxcandidato:
                votosxcandidato[fila[4]] = 0
            if fila[5] == '1' and len(fila[3]) == 8:
                votosxcandidato[fila[4]] = votosxcandidato[fila[4]] + 1
        return votosxcandidato

    def seleccionarganador(self, votosxcandidato):
        maxvotos = 0
        candidatoganador = ''
        votosvalidos = 0
        for candidato in votosxcandidato:
            votosvalidos = votosvalidos + votosxcandidato[candidato]
            if votosxcandidato[candidato] > maxvotos:
                candidatoganador = candidato
                maxvotos = votosxcandidato[candidato]
        return [candidatoganador]

    def calcularganador(self, data):
        votosxcandidato = self.calcularvotos(data)
        return self.seleccionarganador(votosxcandidato)

c = CalculaGanador()
#c.calcularvotos(c.leerdatos())
datatest = [
['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
]
#print(c.calcularganador(datatest))
