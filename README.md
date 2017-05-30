# interactive-MNIST-CNN
A Convolutional neural network heavily based upon the tensorflow advanced MNIST example but equipped with labels to visualize and allowing the user to draw an image and then have the system predict the result.

## Test on images
`python test.py` will try to predict the correct digits of the images inside `imgs`

## Train
`python train.py`

## Draw and predict
`python draw.py`

## Visualize with tensorboard
`tensorboard --logdir=logs/mnist-cnn`