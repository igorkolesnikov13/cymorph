from cymorph.cython_asymmetry import get_asymmetry
from scipy.stats.stats import pearsonr, spearmanr
import matplotlib.pyplot as plt


class Asymmetry:
    def __init__(self, segmented_image) -> None:
        self.segmented_image = segmented_image
        self.asymmetry()

    def asymmetry(self):
        self.asymmetry_v1, self.asymmetry_v2, self.rotated_image, self.final_image, self.collected_points = get_asymmetry(
            self.segmented_image)

    def get_collected_points_plot(self):
        px = 1/plt.rcParams['figure.dpi']  # pixel in inches

        # coluna, linha
        fig_size = (500*px, 500*px)
        f, ax = plt.subplots(figsize=fig_size)
        ax.set_xlabel('Original image', fontsize=20)
        ax.set_ylabel('Rotated image', fontsize=20)
        ax.tick_params(labelsize=16)
        ax.scatter(self.asymmetry_v1, self.asymmetry_v2, s=10, alpha=0.5)

        return ax

    def get_pearsonr(self):
        symmetry_pearsonr_correlation_coeficient = pearsonr(
            self.asymmetry_v1, self.asymmetry_v2)[0]
        
        return (1 - symmetry_pearsonr_correlation_coeficient)

    def get_spearmanr(self):
        symmetry_spearmanr_correlation_coeficient = spearmanr(
            self.asymmetry_v1, self.asymmetry_v2)[0]
        
        return (1 - symmetry_spearmanr_correlation_coeficient)
