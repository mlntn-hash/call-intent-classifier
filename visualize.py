import matplotlib.pyplot as plt
import numpy as np


def plot_confusion_matrix(cm, labels, save_path="confusion_matrix.png" ):
    fig, ax = plt.subplots(figsize=(6,5))
    im = ax.imshow(cm, cmap="Blues")

    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_yticklabels(labels, rotation=45, ha="right")
    ax.set_xticklabels(labels)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")

    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, cm[i, j], ha="center", va="center")

    plt.tight_layout()
    plt.savefig(save_path)
    print("Saved to", save_path)