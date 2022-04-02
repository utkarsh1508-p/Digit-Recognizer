# Digit-Recognizer
MNIST Handwritten digit dataset link https://www.kaggle.com/avnishnish/mnist-original

Implemented a Neural Network with 1 hidden layer having 100 activation units (excluding bias units). The data is loaded from a .mat file, features(X) and labels(y) were extracted. Then features are divided by 255 to rescale them into a range of [0,1] to avoid overflow during computation. Data is split up into 60,000 training and 10,000 testing examples. Feedforward is performed with the training set for calculating the hypothesis and then backpropagation is done in order to reduce the error between the layers. The regularization parameter lambda is set to 0.1 to address the problem of overfitting. Optimizer is run for 70 iterations to find the best fit model. 

![image](https://user-images.githubusercontent.com/81741487/158324382-f460583b-fe08-430a-882f-56af367ad328.png)

**Result**

Training set accuracy of 99.440000%

Test set accuracy of 97.320000%  

Precision of 0.9944
