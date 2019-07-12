#importações de módulos
import os
import re
from DefineHomePath import out_folder

#função para analisar o arquivo
def analisador(arquivo):
    
    #cria arrays para cada tipo de dados
    vendedores = []
    clientes = []
    vendas = []
    
    #verifica cada linha do arquivo
    for linha in arquivo:
        if re.search('001Ã§', linha):
            vendedores.append(linha)
        if re.search('002Ã§', linha):
            clientes.append(linha)
        if re.search('003Ã§', linha):
            vendas.append(linha)
    
    #verifica qual a id da venda mais cara
    itens = []
    ids = []
    totais_vendas = []
        
    for venda in vendas:
        venda_organizada_array = venda.split('Ã§')
        id_venda = venda_organizada_array[1]
        ids.append(id_venda)
        itemId_itemQuantity_itemPrice = venda_organizada_array[2]
        
        #remover colchetes iniciais e finais
        itemId_itemQuantity_itemPrice = itemId_itemQuantity_itemPrice.replace(itemId_itemQuantity_itemPrice[0], "")
        tamanho_texto_itens = len(itemId_itemQuantity_itemPrice)
        tamanho_texto_itens = tamanho_texto_itens - 1
        itemId_itemQuantity_itemPrice = itemId_itemQuantity_itemPrice.replace(itemId_itemQuantity_itemPrice[tamanho_texto_itens], "")
        
        itens = itemId_itemQuantity_itemPrice.split(',')
        
        total_venda = 0;
        
        for item in itens:
            item = item.split('-')
            total_venda = total_venda + (int(item[1]) * float(item[2]))
        totais_vendas.append(total_venda)
    
    
    list_as_dict = dict(zip(ids, totais_vendas))
    
    maior = 0
    id_maior_venda = '';
    
    for chave, valor in list_as_dict.items():
        if valor >= maior:
            maior = valor
            id_maior_venda = chave
    
    #verifica o nome do pior vendedor
    menor = maior
    id_menor_venda = ''
    
    for chave, valor in list_as_dict.items():
        if valor < menor:
            menor = valor
            id_menor_venda = chave
            
    for venda in vendas:
        venda_objeto = re.split('Ã§', venda) 
        if venda_objeto[1] == id_menor_venda:
            nome_pior_vendedor = venda_objeto[3]
    
    #gerar arquivo de saída
    linha1 = "Quantidade de clientes no arquivo de entrada: " + str(len(clientes)) + "\n"
    linha2 = "Quantidade de vendedores no arquivo de entrada: " + str(len(vendedores)) + "\n"
    linha3 = "ID da venda mais cara: " + str(id_maior_venda) + "\n"
    linha4 = "O pior vendedor: " + str(nome_pior_vendedor) + "\n"
    
    #pegando nome original do arquivo
    new_file = "{flat_file_name}.done.dat"
    
    #criando arquivo de saída
    os.chdir(out_folder)
    f=open(new_file,'w')
    texto = []
    texto.append(linha1)
    texto.append(linha2)
    texto.append(linha3)
    texto.append(linha4)
    f.writelines(texto)
    f.close()
    print("RELATÓRIO PRODUZIDO: " + out_folder + "\\" + new_file)
    