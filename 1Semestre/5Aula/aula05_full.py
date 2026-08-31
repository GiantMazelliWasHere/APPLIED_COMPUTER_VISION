# pip install opencv-python

import cv2


# ============================================================
# CONFIGURACOES
# ============================================================

# Tamanho da vizinhanca usada pelos filtros.
#
# Valores menores, como 3:
#   -> menos suavizacao
#   -> mais detalhes preservados
#   -> mais ruido pode permanecer
#
# Valores maiores, como 7 ou 9:
#   -> mais suavizacao
#   -> mais ruido pode ser reduzido
#   -> maior risco de apagar detalhes e bordas finas
#
# Use valores impares: 3, 5, 7, 9...
KERNEL = 3


# Limiar baixo do Canny.
#
# Se diminuir:
#   -> mais respostas fracas podem ser consideradas
#   -> mais bordas aparecem
#   -> tambem pode aumentar a quantidade de ruido detectado
#
# Se aumentar:
#   -> mais respostas fracas sao descartadas
#   -> menos bordas aparecem
#   -> detalhes sutis podem desaparecer
CANNY_MIN = 100


# Limiar alto do Canny.
#
# Se diminuir:
#   -> fica mais facil uma resposta ser considerada uma borda forte
#   -> mais bordas tendem a ser mantidas
#   -> aumenta o risco de falsas bordas
#
# Se aumentar:
#   -> somente variacoes mais intensas sao consideradas fortes
#   -> o resultado tende a ficar mais seletivo
#   -> algumas bordas importantes podem desaparecer
CANNY_MAX = 200


# ============================================================
# 1. CARREGAR A IMAGEM
# ============================================================

imagem = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/5Aula/img/imagem 1.png")


# ============================================================
# 2. FILTRO DE MEDIA
# ============================================================

media = cv2.blur(
    imagem,
    (KERNEL, KERNEL)
)


# ============================================================
# 3. FILTRO GAUSSIANO
# ============================================================

gauss = cv2.GaussianBlur(
    imagem,
    (KERNEL, KERNEL),
    0
)


# ============================================================
# 4. FILTRO DE MEDIANA
# ============================================================

mediana = cv2.medianBlur(
    imagem,
    KERNEL
)


# ============================================================
# 5. CONVERTER AS IMAGENS PARA TONS DE CINZA
#    APENAS PARA A DETECCAO DE BORDAS
# ============================================================

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


# ============================================================
# 6. CANNY NA IMAGEM ORIGINAL
# ============================================================

canny_original = cv2.Canny(
    cinza_original,
    CANNY_MIN,
    CANNY_MAX
)


# ============================================================
# 7. CANNY APOS FILTRO DE MEDIA
# ============================================================

canny_media = cv2.Canny(
    cinza_media,
    CANNY_MIN,
    CANNY_MAX
)


# ============================================================
# 8. CANNY APOS FILTRO GAUSSIANO
# ============================================================

canny_gauss = cv2.Canny(
    cinza_gauss,
    CANNY_MIN,
    CANNY_MAX
)


# ============================================================
# 9. CANNY APOS FILTRO DE MEDIANA
# ============================================================

canny_mediana = cv2.Canny(
    cinza_mediana,
    CANNY_MIN,
    CANNY_MAX
)


# ============================================================
# 10. MOSTRAR OS RESULTADOS
# ============================================================

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