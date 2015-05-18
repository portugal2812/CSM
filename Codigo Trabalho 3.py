# -*- coding: utf-8 -*-
"""
Created on Mon May 04 15:56:56 2015

@author: Administrator
"""
from scipy.fftpack  import dct, idct
import numpy as np
from PIL import Image

##---------------------------exercicio 1---------------------------##

def cortarimagem (imagem):
        
     ## calcula quantos blocos a imagem terá
    dimensaodoarray = (img_height * img_width) / (bloco_Y * bloco_X)
    
     ## cria um array 3D que vai conter todos os blocos separados
    imagemblocos = np.zeros((dimensaodoarray,bloco_Y,bloco_X))
     
    counter=0 ## o counter serve para saber qual e o index onde será posto o proximo cubo
    
     ## ciclo for que vai percorrer todas as linhas
    for linha in range(0, img_height, bloco_Y):
         ## ciclo for que vai percorrer todas as colunas
        for coluna in range(0, img_width, bloco_X):
             ## vai extrair um bloco guardar-lo no array
            imagemblocos[counter] = x_img.crop((coluna, linha, coluna + bloco_X, linha + bloco_Y))
             ## incrementa o "counter" para mudar para a proxima posição do array "imagemblocos"
            counter = counter + 1
            
     ## retorna um array com a imagem separada em blocos       
    return imagemblocos


 ## pede um array 3D e converte e faz a DCT de cada bloco e retorna o array com a DCT
def codificador (arrayblocos):
    
     ## percorre o array e substitui os valores de cada bloco pelo seu DCT
    for i in range(len(arrayblocos)):
        arrayblocos[i] = dct(dct(arrayblocos[i].T, norm='ortho').T , norm='ortho')
    
     ## retorna o array depois de se aplicar o DCT
    return(arrayblocos)
    
    
 ## pede um array 3D e aplica-lhe a IDCT 
def descodificador (arrayblocos):
    
      ## percorre o array e substitui os valores de cada bloco pelo seu IDCT
    for i in range(len(arrayblocos)):
        arrayblocos[i] = idct(idct(arrayblocos[i].T, norm='ortho').T , norm='ortho')

     ## retorna o array depois de se aplicar o IDCT
    return(arrayblocos)


## Função que pede um array 3D e retorna uma array 2D com as dimensoes da imagem original
def agrupaarray (arraylocosIDCT):

    ##Cria um array 2D com as mesmas dimençoes que a imagem original
    arrIDCTcompleto = np.zeros((img_width,img_height))

    mudancadelinha = img_width / bloco_X ##saber quantos blocos são em cada linha
    
    b_c = -1 ##bloco_linha/ defenir a posiçao no array arrIDCTcompleto
    
    b_l = 0 ##bloco_coluna/ defenir a posiçao no array arrIDCTcompleto
    
    for i in range(len(arraylocosIDCT)): ##percorre todos os cubos
    
        b_c = b_c + 1 ##Sempre que se preenche um bloco ele avança 1 para a esuqerda.
        
        if (i == mudancadelinha): ##sempre que uma linha esta completa ele muda de linha
            
            b_l = b_l + 1 ##mudança de linha
            
            b_c = 0 ##reposiçao do x no inicio
            
            ##Muda a variavel mudancadelinha para saber qual e a proxima vez que tera que mudar de linha
            mudancadelinha = mudancadelinha + (img_width / bloco_X) 

        ##percorre o conteudo de cada bloco do array "arraylocosIDCT" e coloca no array "arrIDCTcompleto"  
        for y in range(bloco_Y): 
            for x in range(bloco_X):
                arrIDCTcompleto[b_l * bloco_Y + y][b_c * bloco_X + x]  = arraylocosIDCT[i][y][x]
                
    ##retorna a o array 2D completo que originou do array de blocos introduzidos
    return(arrIDCTcompleto)



## Pede um array ou lista e converte-o para uma image e grava-a.
def arraytoimage (img_array, nome):
     ## certefica-se se o "img_array" é um array e nao uma lista fazendo a converção.
    img_array = np.asarray(img_array)
    
     ## converte os valores para 8-bit
    img_array = img_array.astype('uint8')
    
     ## Converte o array "img_array" numa imagem a tons de cinzento
    imagem_final = Image.fromarray(img_array ,'L')
    
     ## grava a imagem com o nome inicioalizado pela funçao
    imagem_final.save(nome)

##---------------------------exercicio 2---------------------------##



def quantificacao (arrayblocos):

    for i in range(len(arrayblocos)):
        for linha in range(bloco_Y): 
            for coluna in range(bloco_X):
                    arrayblocos[i][linha][coluna] = arrayblocos[i][linha][coluna] / (Q[linha][coluna] * qualidade)
                    

    return(arrayblocos)


def quality_factor(q):
    if(q <= 50):
        factor = 50.0 / q
    else:
        factor = 2.0 - (q * 2.0)/100.0
    return factor 



def desquantificacao (arrayblocos):
    


    for i in range(len(arrayblocos)):
        for linha in range(bloco_Y): 
            for coluna in range(bloco_X):
                    arrayblocos[i][linha][coluna] = (Q[linha][coluna] * qualidade) * arrayblocos[i][linha][coluna]                             


    return(arrayblocos)













##----------------------------main----------------------------##

 ## importação da imagem

x_img = Image.open("lena.tiff")
 ## carregamento da imagem
img = x_img.load()

 ## guarda a largura da imagem
img_width = x_img.size[0]

 ## guardar a altura da image
img_height = x_img.size[1]

 ## define as dimensoes de cada bloco
bloco_Y = 8
bloco_X = 8

 ## table K1 - Luminance quantize Matrix  
Q = np.zeros((8, 8))
Q[0] = [ 16,  11,  10,  16,  24,  40,  51,  61]
Q[1] = [ 12,  12,  14,  19,  26,  58,  60,  55]
Q[2] = [ 14,  13,  16,  24,  40,  57,  69,  56]
Q[3] = [ 14,  17,  22,  29,  51,  87,  80,  62]
Q[4] = [ 18,  22,  37,  56,  68, 109, 103,  77]
Q[5] = [ 24,  35,  55,  64,  81, 104, 113,  92]
Q[6] = [ 49,  64,  78,  87, 103, 121, 120, 101]
Q[7] = [ 72,  92,  95,  98, 112, 100, 103,  99]












##----Exercicio-1----##

imagemblocos = cortarimagem(x_img) ## Corta a imagem em blocos

DCT = codificador(imagemblocos) ## Faz a DCT de cada bloco

DCT_agrupado = agrupaarray(DCT) ## Agrupa os blocos num array com as dimensoes da imagem original

arraytoimage(DCT_agrupado,'Lena_exercicio_1_DCT.tiff') ## Exporta a imagem com a DCT

IDCT = descodificador(DCT) ## Faz a IDC do array de blocos DCT

IDCTagrupado = agrupaarray(IDCT) ## Agrupa os blocos num array com as dimensoes da imagem original

arraytoimage(IDCTagrupado,'Lena_exercicio_1.tiff') ## Exporta a imagem depois de IDCT


##----Exercicio-2----##

qualidade = quality_factor(50)

imagemblocos = cortarimagem(x_img) ## Corta a imagem em blocos

DCT = codificador(imagemblocos) ## Faz a DCT de cada bloco

DCTquantificado = quantificacao(DCT)

DCTquantificadoagrupado = agrupaarray(DCTquantificado)

arraytoimage(DCTquantificadoagrupado,'Lena_exercicio_2DCT.tiff')

DCTdesquantificado = desquantificacao(DCTquantificado)

IDCTdesquantificado = descodificador(DCTdesquantificado)

IDCTdesquantificadoAgrupado = agrupaarray(IDCTdesquantificado)

arraytoimage(IDCTdesquantificadoAgrupado,'Lena_exercicio_2.tiff')






