import numpy as np
from libc.math cimport sqrt

from scipy import fftpack
from scipy.ndimage.filters import gaussian_filter

cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
cpdef float butterworth(float d,float d0,float n):
    return 1.0/(1.0+pow(d/d0,2.0*n))

@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def filter_butterworth_2d(float[:,:] image, float smoothness_degradation, float butterworth_order, float max_d0):
    # frac -> max smoothing at center
    cdef:
        int heigth,width,cx,cy, i, j
        float[:,:] smoothed
        np.complex64_t[:,:]  freq

    heigth, width = len(image),len(image[0])
    cx, cy = width/2, heigth/2

    smoothed = np.array([[0.0 for i in range(width)] for j in range(heigth)],dtype=np.float32)
    for i in range(heigth):
        for j in range(width):
            smoothed[i][j] = image[i][j]
            

    freq = fftpack.fft2(image)
    freq = fftpack.fftshift(freq)
    for i in range(heigth):
        for j in range(width):
            freq[i][j] = freq[i][j] * butterworth(sqrt(((float(i) - float(heigth) / 2.0)*(float(i) - float(heigth) / 2.0)) + ((float(j) - float(width) / 2.0)*(float(j) - float(width) / 2.0))) ,smoothness_degradation * max_d0, butterworth_order)
    smoothed = np.real(fftpack.ifft2(fftpack.ifftshift(freq))).astype(np.float32)
    return smoothed

############################################ 
#     Funcao Smoothness (Suavizacao):
# entrada:
#    mat - matriz do tipo numpy(list(list))
#    kernel - matriz de convolucao
#    corrFunction - funcao de correlacao (stats.pearsonr, stats.spearmanr, ....)
# retorna:
#    coeficiente encontrado (valor e prob. da hipotese nula),
#    matriz,
#    matrizRotacionada
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def get_smoothness(float[:,:] image, float[:,:] smoothed_image):
    cdef:
        int w, h, countPts, it, i, j
        float[:,:] final_image
    w, h = len(image[0]), len(image)

    final_image = np.zeros(shape=(w, h), dtype=np.float32)
    countPts=0
    for i in range(w):
        for j in range(h):
            if(image[j, i] != 0.0):
                countPts += 1
    
    # É complicado analisar imagens muito pequenas, uma correlação com menos de 6 pontos não é estatisticamente relevante. 
    # Não vejo este tipo de detalhe sendo discutido nos artigos clássicos de análise não paramétrica (como o do Conscelice), 
    # por isso adotei um N de corte de acordo com o que achava melhor.
    if(countPts<6):
        return (305, 305, image) # flag value
    it = 0 
    
    v1, v2 = [0.0 for i in range(countPts)],[0.0 for i in range(countPts)]

    for i in range(w):
        for j in range(h):
            if (image[j,i] != 0.0 and smoothed_image[j,i] != 0.0):
                final_image[j,i] = image[j,i]
                v1[it] = image[j,i]
                v2[it] = smoothed_image[j,i]
                it = it + 1

    return v1, v2, final_image