import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

csv = pd.read_csv('./KneeXray/Test_correct.csv', names = ['data', 'label'])
Test_correct_label = csv['label']
Test_correct_label_list = Test_correct_label.values.tolist()

csv = pd.read_csv('./submission.csv', names = ['data', 'label'])
submission_label = csv['label']
submission_label_list = submission_label.values.tolist()
accuracy_score=accuracy_score(Test_correct_label_list, submission_label_list)
print('accuracy_score : {}'.format(accuracy_score))
print()

label=['0', '1', '2', '3', '4'] # 라벨 설정
normalize='true'
conf_matrix = confusion_matrix(Test_correct_label_list, submission_label_list, labels=label, normalize=normalize)
print(conf_matrix)
                             
title = 'Confusion Matrix'
cmap=plt.cm.Greens
plt.figure(figsize=(6, 6))
plt.imshow(conf_matrix, interpolation='nearest', cmap=cmap)  # , cmap=plt.cm.Greens
plt.title(title, size=12)
plt.colorbar(fraction=0.05, pad=0.05)
tick_marks = np.arange(5, 5)
plt.xlabel('Predicted label\naccuracy={:0.5f}'.format(accuracy_score))
plt.ylabel('True label')
plt.xticks(np.arange(5), ('0', '1', '2', '3', '4'))
plt.yticks(np.arange(5), ('0', '1', '2', '3', '4'))

fmt = '.3f' if normalize else 'd'
thresh = 200
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        plt.text(j, i, format(conf_matrix[i, j], fmt),
                 ha="center", va="center", color="white" if conf_matrix[i, j] > thresh else "black")  #horizontalalignment

plt.show()