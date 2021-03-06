# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FTxuLri26X76zpX9XTBufYFsKWu5Kq3l
"""

import pandas as pd
from google.colab import drive
drive.mount('/content/gdrive')
import numpy as np
import os
import keras
import matplotlib.pyplot as plt
from keras.layers import Dense,GlobalAveragePooling2D, Flatten, Dropout
from keras.applications import MobileNetV2
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.optimizers import Adam

from keras.layers import Dense,GlobalAveragePooling2D, Flatten, Dropout
from keras.applications import MobileNetV2
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model
from keras.optimizers import Adam
Y_train = np.load("../content/gdrive/My Drive/Y_train_PLS.npy")
X_valid = np.load("../content/gdrive/My Drive/X_val_PLS.npy")
Y_valid = np.load("../content/gdrive/My Drive/Y_val_PLS.npy")
X_train = np.load("../content/gdrive/My Drive/X_train_PLS.npy")
model5=MobileNetV2(weights='imagenet',include_top=False,input_shape=(224,224,3))
x=model5.output
x = Flatten()(x)
features = Dense(256,activation=keras.layers.LeakyReLU(alpha=0.1))(x)
preds=Dense(7,activation='softmax')(features)
bbmodel = Model(inputs = model5.input,output = preds)
adam = keras.optimizers.Adam(lr=5e-5)
bbmodel.compile(optimizer=adam, loss='categorical_crossentropy', metrics=['accuracy'])
num_iter = 64
history = bbmodel.fit(X_train, Y_train, epochs = num_iter, batch_size = 20, shuffle = True, verbose = 1, 
                     validation_data=(X_valid, Y_valid))



print(history.history.keys())
# summarize history for accuracy
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#print(history.history.keys())
with open('/trainHistoryDict', 'wb') as file_pi:
        pickle.dump(history.history, file_pi)

#Summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.show()

# plot the confusion matrix
plot_confusion_matrix(confusion_mtx, classes = range(7))

plot_confusion_matrix(confusion_mtx, classes = range(7))

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels
import numpy as np
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
 plt.imshow(cm, interpolation='nearest', cmap=cmap)
 plt.title(title)
 plt.colorbar()
 tick_marks = np.arange(len(classes))
 plt.xticks(tick_marks, classes, rotation=45)
 plt.yticks(tick_marks, classes)

 if normalize:
   cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

   thresh = cm.max() / 2.
   for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
      plt.text(j, i, cm[i, j],
             horizontalalignment="center",
             color="white" if cm[i, j] > thresh else "black")

 plt.tight_layout()
 plt.ylabel('True label')
 plt.xlabel('Predicted label')
 Y_pred = model5.predict(X_valid)
 Y_pred_classes = np.argmax(Y_pred,axis = 1) 
 Y_true = np.argmax(Y_valid,axis = 1) 
 confusion_mtx = confusion_matrix(Y_true, Y_pred_classes)
 plot_confusion_matrix(confusion_mtx, classes = range(7))

def plot_confusion_matrix(y_true, y_pred, classes,
                          normalize=False,
                          title=None,
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if not title:
        if normalize:
            title = 'Normalized confusion matrix'
        else:
            title = 'Confusion matrix, without normalization'

    # Compute confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    # Only use the labels that appear in the data
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           # ... and label them with the respective list entries
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax


np.set_printoptions(precision=2)
Y_pred = model5.predict(X_valid)
Y_pred_classes = np.argmax(Y_pred,axis = 1) 
Y_true = np.argmax(Y_valid,axis = 1) 
confusion_mtx = confusion_matrix(Y_true, Y_pred_classes)
plot_confusion_matrix(confusion_mtx, classes = range(7))


plt.show()
