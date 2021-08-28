"""
Plots the confusion matrix of inter-block probabilities used to construct the block model.
"""


import itertools
import numpy as np
import matplotlib.pyplot as plt


cnf_matrix = [[0.005030819409873796, 0.004203347585633323, 0.0007447001073944312, 0.005150902900540084, 0.0007807989749236244], [0.004203347585633323, 0.005728495030765911, 0.004088874400070833, 0.0014595198237273728, 0.006548059095289867], [0.0007447001073944312, 0.004088874400070833, 0.0033300518629148014, 0.00034743835204802386, 0.00044608628820590705], [0.005150902900540084, 0.0014595198237273728, 0.00034743835204802386, 0.004914135832684608, 0.000465676976193497], [0.0007807989749236244, 0.006548059095289867, 0.00044608628820590705, 0.000465676976193497, 0.0055408410753398285]]


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='blockmodel'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.set_cmap('Blues')
    plt.imshow(cm, interpolation='nearest')
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else '.4f'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    #plt.ylabel('True label')
    #plt.xlabel('Predicted label')
    plt.tight_layout()

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(np.array(cnf_matrix), classes=["1", "2", "3", "4", "5"], normalize=False,
                      title='Block Model')

plt.show()