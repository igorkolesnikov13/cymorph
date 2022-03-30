from cymorph.cython_entropy import get_entropy
import matplotlib.pyplot as plt
import seaborn as sns

class Entropy:
    def __init__(self, segmented_image, entropy_bins) -> None:
        self.segmented_image = segmented_image
        self.entropy_bins = entropy_bins
    
    def get_bins_plot(self):
        line = self.segmented_image.flatten()
        line = line[line != 0]

        px = 1/plt.rcParams['figure.dpi']  # pixel in inches
        # coluna, linha
        fig_size = (500*px, 500*px)
        f, ax = plt.subplots(figsize=fig_size)
        ax = sns.histplot(line, kde=True, binwidth=50)
        ax.set_xlabel('Flux value', fontsize=20)
        ax.set_ylabel('Frequency', fontsize=20)
        ax.tick_params(labelsize=16)

        return ax

    def get_entropy(self):
        return get_entropy(self.segmented_image, self.entropy_bins)
    
