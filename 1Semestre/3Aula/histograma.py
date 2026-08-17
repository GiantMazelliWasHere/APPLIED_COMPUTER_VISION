#pip install opencv-python matplotlib

import cv2
import matplotlib.pyplot as plt


# Carregar imagem em tons de cinza
img = cv2.imread(
    "APPLIED_COMPUTER_VISION/1Semestre/3Aula/img/remedio.png",
    cv2.IMREAD_GRAYSCALE
)


# Calcular histograma
histograma = cv2.calcHist(
    [img],      # imagem
    [0],        # canal
    None,       # mÃ¡scara
    [256],      # quantidade de nÃ­veis
    [0, 256]    # intervalo de intensidades
)


# Exibir histograma
plt.plot(histograma)

plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")

plt.xlim([0, 255])

plt.show()