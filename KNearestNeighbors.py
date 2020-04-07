import math
class KNN(object):
    def __init__(self, dados, labels, k=5):
        self.k = k
        self.labels = labels
        self.dados = dados
        self.trata_dados(self.dados) # Trata os dados caso haja campos que não sejam numéricos

    def predict(self, dado):
        self.trata_dados(dado)
        
        self.distancias = {}
        for i in range(len(self.dados)): # Para cada linha dos dados
            distancia = 0
            for j in range(len(self.dados[0])): # calcula-se a distancia de cada atributo
                distancia += pow(dado[0][j] - self.dados[i][j], 2)

            distancia = math.sqrt(distancia)
            
            if(len(self.distancias) >= self.k):
                if(distancia < max(self.distancias)):
                    del self.distancias[max(self.distancias)]
                    self.distancias[distancia] = self.labels[i]
            else:
                self.distancias[distancia] = self.labels[i]
        
        l = {}
        for i, j in enumerate(self.distancias):
            if(l.get(self.distancias[j]) == None):
                l[self.distancias[j]] = 0
            
            l[self.distancias[j]]+= 1
        
        return list(l.keys())[list(l.values()).index(max(l.values()))]
    
    def trata_dados(self, dados):
        for i in range(len(dados[0])):
            if(not (type(dados[0][i]) == int or type(dados[0][i]) == float)):
                c = 0
                obj = {}
                for j in range(len(dados)):
                    if(obj.get(dados[j][i]) == None):
                        obj[dados[j][i]] = c
                        c += 1
                        
                    dados[j][i] = obj[dados[j][i]]