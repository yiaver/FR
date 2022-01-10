import re

class FR():
    def __init__(self,content=str):
        if content == False:
            return False
        self.coteudo = content
        self.filtrado = ""
    def filtra_numeros(self,subistituto =" "):
        self.filtrado = re.sub(r"[0-9]",subistituto,self.coteudo)
        return self.filtrado
    def filtra_letras_minusculas(self,subistituto =" "):
        self.filtrado = re.sub(r"[a-z]",subistituto,self.coteudo)
        return self.filtrado
    def filtra_letras_maiusculas(self,subistituto =" "):
        self.filtrado = re.sub(r"[A-Z]",subistituto,self.coteudo)
        return self.filtrado
    def filtra_simbulos(self,subistituto =" "):
        self.filtrado = re.sub(r"[\!\@\#\$\%\*\(\)\_\-\´\[\]\{\}\`\~\^\,\;\<\>\:\.\/\?\\]",subistituto,self.coteudo)
        return self.filtrado
    def filtros(self,Letras_minusculas = False,Letras_maiusculas=False,Numeros=False,Simbulos=False):
        if Letras_maiusculas:
            self.filtra_letras_maiusculas()
        if Letras_minusculas:
            self.filtra_letras_minusculas()
        if Numeros:
            self.filtra_numeros()
        if Simbulos:
            self.filtra_simbulos()
        else:
            return "Por favor adicione um ou mais filtros a serem aplicados na string"
    def filtro_especifico(self,filtro=str,subistituto=""):
        self.filtrado(filtro,subistituto,self.coteudo)
        return self.filtrado
        
