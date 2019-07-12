#importações de módulos
import os
from DefineHomePath import in_folder

arquivo = []

#agrupar todos os arquivos em um só
def agrupador(file):
    os.chdir(in_folder)
    os.access(file, os.R_OK)
    f = open(file)
    for linha in f:
        arquivo.append(linha)    
    return arquivo