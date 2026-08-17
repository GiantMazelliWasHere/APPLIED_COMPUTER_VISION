import cv2

img = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/3Aula/img/remedio.png")

cinza = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

limiar_ots, mascara = cv2.threshold(
    cinza,
    0,
    255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print(f"Threshold calculado: {limiar_ots}")

quantidade_rotulos, rotulos, estatisticas, centroides = (
    cv2.connectedComponentsWithStats(
        mascara,
        connectivity=8
    )
)

area_minima = 14000

quantidade_comprimidos = 0

for i in range(1, quantidade_rotulos):
    area = estatisticas[
        i,
        cv2.CC_STAT_AREA
    ]

    if area >= area_minima:
        quantidade_comprimidos += 1

print(f"Quantidade de Comprimidos: {quantidade_comprimidos}")

cv2.imshow(
    "Imagem Original",
    img
)

cv2.imshow(
    "Tons de Cinza",
    cinza
)

cv2.imshow(
    "Mascara Otsu",
    mascara
)

cv2.waitKey(0)
cv2.destroyAllWindows()