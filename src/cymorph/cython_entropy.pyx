import numpy as np

from libc.math cimport log10

cimport numpy as np
cimport cython


############################################
#     Funcoes de entropia:
# entrada:
#    image - matriz do tipo np(list(list))
#    bins - numero de patamares
# retorna:
#    coeficiente encontrado,
#    matriz
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef float get_entropy(float[:,:] image, int bins):
    cdef:
        float[:] freq, line
        float[:] binagem
        long[:] temp
        float somatorio,coef
        tuple x
        list entropies
        int w, h, i
    w, h = len(image[0]), len(image)
    line = ravel(image) # TODO test substitutio for ravel from np

    freq = np.array([0.0 for i in range(bins)], dtype=np.float32)
    temp, binagem = np.histogram(line,bins)
    
    somatorio = 0.0
    for i in range(bins):
        somatorio = somatorio + temp[i] # TODO substitute by count_not_masked in ravel
    
    for i in range(bins):
        freq[i] = float(temp[i])/float(somatorio)
    somatorio = 0.0
    for i in range(bins):
        if freq[i]>0.0:
            somatorio = somatorio - freq[i]*log10(freq[i])
    coef = somatorio/log10(bins)
    
    return coef


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cdef float[:] ravel(float[:,:] image):
    cdef:
          int w, h, count_not_masked, j, i,it
          float[:] line
    w, h = len(image[0]), len(image)
    count_not_masked = 0
    for i in range(w):
        for j in range(h):
            if(image[j, i] != 0.0):
               count_not_masked = count_not_masked + 1
    line = np.array([0.0 for i in range(count_not_masked)], dtype=np.float32)
    it = 0
    for i in range(w):
        for j in range(h):
            if(image[j, i] != 0.0):
                line[it] = image[j, i]
                it = it + 1 
    return line