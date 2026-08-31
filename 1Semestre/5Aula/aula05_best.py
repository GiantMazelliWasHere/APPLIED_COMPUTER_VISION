# pip install opencv-python

import cv2


# ============================================================
# CONFIGURACOES
# ============================================================

# Tamanho da vizinhanca usada pelo filtro de mediana.
#
# Valores menores, como 3:
#   -> menos suavizacao
#   -> mais detalhes preservados
#   -> mais ruido pode permanecer
#
# Valores maiores, como 5 ou 7:
#   -> mais ruido pode ser removido
#   -> maior risco de perder detalhes finos
#
# Use valores impares: 3, 5, 7...
KERNEL = 5


# Limiar baixo do Canny.
#
# Se diminuir:
#   -> mais bordas podem aparecer
#   -> aumenta a sensibilidade
#   -> mais ruido pode ser detectado
#
# Se aumentar:
#   -> menos bordas aparecem
#   -> detalhes sutis podem desaparecer
CANNY_MIN = 100


# Limiar alto do Canny.
#
# Se diminuir:
#   -> mais respostas podem ser consideradas bordas fortes
#   -> mais bordas tendem a ser mantidas
#
# Se aumentar:
#   -> apenas variacoes mais intensas sao consideradas fortes
#   -> resultado mais seletivo
CANNY_MAX = 200


# ============================================================
# 1. CARREGAR A IMAGEM
# ============================================================

imagem = cv2.imread("APPLIED_COMPUTER_VISION/1Semestre/5Aula/img/imagem 1.png")


# ============================================================
# 2. APLICAR FILTRO DE MEDIANA
# ============================================================

mediana = cv2.medianBlur(
    imagem,
    KERNEL
)


# ============================================================
# 3. CONVERTER PARA TONS DE CINZA
#    APENAS PARA DETECCAO DE BORDAS
# ============================================================

cinza_original = cv2.cvtColor(
    imagem,
    cv2.COLOR_BGR2GRAY
)

cinza_mediana = cv2.cvtColor(
    mediana,
    cv2.COLOR_BGR2GRAY
)


# ============================================================
# 4. CANNY NA IMAGEM ORIGINAL
# ============================================================

canny_original = cv2.Canny(
    cinza_original,
    CANNY_MIN,
    CANNY_MAX
)


# ============================================================
# 5. CANNY APOS FILTRO DE MEDIANA
# ============================================================

canny_mediana = cv2.Canny(
    cinza_mediana,
    CANNY_MIN,
    CANNY_MAX
)


# ============================================================
# 6. MOSTRAR OS RESULTADOS
# ============================================================

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