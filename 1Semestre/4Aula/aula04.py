import cv2
import numpy as np

iterations = 2
kernel = np.ones((3, 3), np.uint8)

#img = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/4Aula/img/formas-coloridas.png")
#img = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/4Aula/img/meme.jpg")
#img = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/4Aula/img/memeV2.jpg")

cv2.imshow("Imagem Original", img)

erosao = cv2.erode(
    img,
    kernel,
    iterations=iterations
)

cv2.imshow("Erosao", erosao)

dilatacao = cv2.dilate(
    img,
    kernel,
    iterations=iterations
)

cv2.imshow("Dilatacao", dilatacao)

abertura = cv2.morphologyEx(
    img,
    cv2.MORPH_OPEN,
    kernel,
    iterations=iterations
)

cv2.imshow("Abertura", abertura)

fechamento = cv2.morphologyEx(
    img,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=iterations
)

cv2.imshow("Fechamento", fechamento)

cv2.waitKey(0)
cv2.destroyAllWindows()