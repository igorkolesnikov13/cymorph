from cymorph.cython_smoothness import get_smoothness, filter_butterworth_2d
from scipy.stats.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt

class Smoothness:
    def __init__(self, clean_image, segmented_mask, smoothing_degradation, butterworth_order) -> None:
        self.segmented_image = clean_image * segmented_mask
        self.clean_image = clean_image
        self.segmented_mask = segmented_mask
        self.smoothing_degradation = smoothing_degradation
        self.butterworth_order = butterworth_order
        self.height, self.width = self.clean_image.shape

        self.smoothness()
        
    def smoothness(self):
        self.smoothed_image = self.get_smoothed_image()

        self.smoothness_v1, self.smoothness_v2, self.final_image = get_smoothness(self.segmented_image, self.smoothed_image)
    
    def get_collected_points_plot(self):
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        # coluna, linha
        fig_size = (500*px, 500*px)
        f, ax = plt.subplots(figsize=fig_size)
        ax.set_xlabel('Original image', fontsize=20)
        ax.set_ylabel('Smoothed image', fontsize=20)
        ax.tick_params(labelsize=16)
        ax.scatter(self.smoothness_v1, self.smoothness_v2, s=10, alpha=0.5)
        
        return ax

    def get_smoothed_image(self):
        smoothed_image_aux = filter_butterworth_2d(self.clean_image, self.smoothing_degradation, self.butterworth_order, self.height/2)

        return smoothed_image_aux * self.segmented_mask

    def get_pearsonr(self):
        try:
            symmetry_pearsonr_correlation_coeficient  = pearsonr(self.smoothness_v1, self.smoothness_v2)[0]
        except TypeError:
            return None
        
        return (1 - symmetry_pearsonr_correlation_coeficient)
    
    def get_spearmanr(self):
        try:
            symmetry_spearmanr_correlation_coeficient = spearmanr(self.smoothness_v1, self.smoothness_v2)[0]
        except TypeError:
            return None
        
        return (1 - symmetry_spearmanr_correlation_coeficient)
