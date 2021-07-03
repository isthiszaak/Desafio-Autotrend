# Desafio 6: ANAGRAMAS (médio/difícil) -- 70 pontos

# Link do desafio: https://osprogramadores.com/desafios/d06/


# Autor: Isaac Manoel da Silva Barros
# Contato: (86) 9 9996-1191
# Email: isaac050587@gmail.com
# Data : 03/07/2021


# Algoritmo proposto:
    
# 1) Adquire entrada do usuário

# 2) Verifica se há erros na entrada
    
# 3) "Limpa" entrada fornecida (remove espacos vazios)

# 4) Obtem as combinações possíveis para a entrada

# 5) Verificando quais combinações estão no banco de palavras

# 6) Imprimindo palavras encontradas



# =======================================
# ======    Bibliotecas usadas    =======
# =======================================

import numpy as np
import re
from itertools import permutations
import sys


# ==============================================
# ====== Inicializando banco de palavras =======
# ==============================================


with open("words.txt") as f:
    
    banco = np.array(f.readlines()) # Banco de palavras no formato vetor
    
for i in range(len(banco)) :
    
    banco[i] = "-" + banco[i] + "-" # Inserindo caracter que irá delimitar o inicio e o fim de uma palavra do banco


banco2 = str(banco.tolist()) # Passando o banco de palavras para o formato de lista
banco2 = banco2.replace("\\","")    
banco2 = banco2.replace("'","") 
banco2 = banco2.replace("n","")
 
caracteres = "[@_!#$%^&*()<>?/\|}{~:]0123456789.¨-ªº'áàäéèëíìïóòöúùüñ+,°´`Çÿ" # Caracteres proibidos   

flag = 1  # Inicializando flag de erro

# =======================================
# ====== Funções usadas no código =======
# =======================================

# =============================================================================
# Função que verifica se há caractere especial  ou excede o limite de caracteres

def verifica_erro(texto1):    
    
    if len(texto1) > 16 :
        
        print("\n\nEntrada maior que 16 caracteres.\nAbordando código!")
                        
        sys.exit() # aborta código!
    
    if any(c in caracteres for c in texto1): # ERRO!
        
        print("\n\nCaracteres especiais encontrados.\nAbordando código!")
                        
        sys.exit() # aborta código!
        
    else: # SEM ERRO
        
       combinacoes(texto1)  # Envia entrada para função de combinacoes
       
# ============================================================
# Funcao que obtem os anagramas possiveis da entrada do usuário

def combinacoes(texto2) :

      texto2 = texto2.replace(" ",'') # Removendo espaços em branco da entrada
      
      possibilidades = []

      for i in range(1, len(texto2)+1):
      
          for c in permutations(texto2, i):
          
              possibilidades.append("".join(c))

      print("\n\n--- Lista de combinações com sua entrada ----\n")
      print(possibilidades) 
      print("\n---------------------------------------------")
      
      procura_palavras(possibilidades)

# ===================================================================
# Funcao que procura anagramas da entrada dentro do banco de palavras

def procura_palavras(possibilidades1):
      
      contador = 0 
      conjunto = []
      
      for x in range(len(possibilidades1)):
            
        
          palavra = possibilidades1[x]
        
          palavra2 = "-" + str(palavra) +"-," #Procura no banco a palavra, com os delimitadores para marcar o inicio e o fim das palavras
     
        
          if palavra2 in banco2:                
              
              contador = contador + 1 
              
              conjunto.append(palavra)  
      
      print("\n\nPalavras obtidas:\n\n")
      print(np.unique(np.array(conjunto))) # Exibindo anagramas obtidos
      print("\nTotal de anagramas localizadas: %d" %contador) 
      

# =======================================
# =========== Loop Principal ============
# =======================================

while flag == 1:         
  
    
# Adquirindo entrada do usuário

    entrada = input('Insira uma entrada de até 16 caracteres (excluindo números, pontuação, e caracteres acentuados)\n\n')

    entrada = entrada.upper() # Entrada em letras maiúculas

    verifica_erro(entrada)   # Inicia chamada de funções
        
    
