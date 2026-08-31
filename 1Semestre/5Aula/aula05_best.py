import cv2


KERNEL = 5

CANNY_MIN = 100

CANNY_MAX = 200

imagem = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/5Aula/img/memeV2.jpg")

mediana = cv2.medianBlur(
    imagem,
    KERNEL
)

cinza_original = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2GRAY
)

cinza_mediana = cv2.cvtColor(
    mediana,
    cv2.COLOR_BGR2GRAY
)

canny_original = cv2.Canny(
    cinza_original,
    CANNY_MIN,
    CANNY_MAX
)

canny_mediana = cv2.Canny(
    cinza_mediana,
    CANNY_MIN,
    CANNY_MAX
)

cv2.imshow(
    "1 - Original",
    imagem
)

cv2.imshow(
    f"2 - Mediana {KERNEL}x{KERNEL}",
    mediana
)

cv2.imshow(
    "3 - Canny Original",
    canny_original
)

cv2.imshow(
    f"4 - Canny apos Mediana {KERNEL}x{KERNEL}",
    canny_mediana
)

cv2.waitKey(0)
cv2.destroyAllWindows()