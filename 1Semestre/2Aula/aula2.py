import cv2
import numpy as np


# Carrega a imagem.
imagem = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/2Aula/img/pessoa-deriva-mar.png")
imagem2 = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/2Aula/img/pessoa-deriva-mar-2.png")

print("Qual Imagem: 1 ou 2")
user = int(input("Digite o numero: "))

if(user == 1):
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

    laranja_minimo = np.array([10,100,100])
    laranja_maximo = np.array([20,255,255])

    mascara = cv2.inRange(hsv,laranja_minimo,laranja_maximo)

    linhas,colunas = np.where(mascara>0)

    if len(colunas)>0:
        eixo_x = colunas[0]
        eixo_y = linhas[0]
        print("Coordenadas:")
        print(f"Coordenada x {eixo_x}")
        print(f"Coordenada y {eixo_y}")
    else:
        print("Coordenadas não encontradas")

    r = cv2.bitwise_and(imagem,imagem,mask=mascara)

    cv2.imshow("O Origem de Tudo",imagem)
    cv2.imshow("A Mascara da Morte", mascara)
    cv2.imshow("O Resultado de Tudo Isso", r)

    cv2.waitKey(0)
elif(user == 2):
    hsv = cv2.cvtColor(imagem2, cv2.COLOR_BGR2HSV)

    laranja_minimo = np.array([10,100,100])
    laranja_maximo = np.array([20,255,255])

    mascara = cv2.inRange(hsv,laranja_minimo,laranja_maximo)

    linhas,colunas = np.where(mascara>0)

    if len(colunas)>0:
        eixo_x = colunas[0]
        eixo_y = linhas[0]
        print("Coordenadas:")
        print(f"Coordenada x {eixo_x}")
        print(f"Coordenada y {eixo_y}")
    else:
        print("Coordenadas não encontradas")

    r = cv2.bitwise_and(imagem2,imagem2,mask=mascara)

    cv2.imshow("O Origem de Tudo",imagem2)
    cv2.imshow("A Mascara da Morte", mascara)
    cv2.imshow("O Resultado de Tudo Isso", r)

    cv2.waitKey(0)
else:
    print("Opcao nao encontrada")

