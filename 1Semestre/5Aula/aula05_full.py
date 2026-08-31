import cv2


KERNEL = 3

CANNY_MIN = 100

CANNY_MAX = 200

imagem = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/5Aula/img/memeV2.jpg")

media = cv2.blur(
    imagem,
    (KERNEL, KERNEL)
)

gauss = cv2.GaussianBlur(
    imagem,
    (KERNEL, KERNEL),
    0
)

mediana = cv2.medianBlur(
    imagem,
    KERNEL
)

cinza_original = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2GRAY
)

cinza_media = cv2.cvtColor(
    media,
    cv2.COLOR_BGR2GRAY
)

cinza_gauss = cv2.cvtColor(
    gauss,
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

canny_media = cv2.Canny(
    cinza_media,
    CANNY_MIN,
    CANNY_MAX
)

canny_gauss = cv2.Canny(
    cinza_gauss,
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
    f"2 - Media {KERNEL}x{KERNEL}",
    media
)

cv2.imshow(
    f"3 - Gaussiano {KERNEL}x{KERNEL}",
    gauss
)

cv2.imshow(
    f"4 - Mediana {KERNEL}x{KERNEL}",
    mediana
)

cv2.imshow(
    "5 - Canny Original",
    canny_original
)

cv2.imshow(
    f"6 - Canny apos Media {KERNEL}x{KERNEL}",
    canny_media
)

cv2.imshow(
    f"7 - Canny apos Gaussiano {KERNEL}x{KERNEL}",
    canny_gauss
)

cv2.imshow(
    f"8 - Canny apos Mediana {KERNEL}x{KERNEL}",
    canny_mediana
)

cv2.waitKey(0)
cv2.destroyAllWindows()