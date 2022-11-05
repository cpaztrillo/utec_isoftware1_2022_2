class CalculaImpuesto:
    limites = ()
    def calcula5ta(self, valor):
        if valor>self.limite:
            return valor*self.igv
        else:
            return 0

ci = CalculaImpuesto()
print('%.2f' %ci.calcula(1))