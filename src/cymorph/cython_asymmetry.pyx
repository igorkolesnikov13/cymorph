import numpy as np

cimport numpy as np
cimport cython

############################################
#     Funcoes de assimetria:
# entrada:
#    mat - matriz do tipo np(list(list))
#    corrFunction - funcao de correlacao (stats.pearsonr, stats.spearmanr, ....)
# retorna:
#    coeficiente encontrado,
#    matrizRotacionada
#    pontos de correlacao (I,I_h)
#    mascara de pontos considerados (rotacionado e nao rotacionado)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef get_asymmetry(float[:,:] image):
    cdef:
         float[:,:]  rotated_image, final_image
         int w, h, collected_points
    w, h = len(image[0]), len(image)

    rotated_image = np.rot90(image,2)
    final_image = np.zeros(shape=(w, h), dtype=np.float32)
    
    collected_points = 0
    v1 = []
    v2 = []
    for i in range(w):
        for j in range(h):
            if (image[j,i] != 0) and (rotated_image[j,i] != 0):
                final_image[j,i] = image[j,i]
                v1.append(image[j,i])
                v2.append(rotated_image[j,i])
                collected_points = collected_points+1
    
    return v1, v2, rotated_image, final_image, collected_points
