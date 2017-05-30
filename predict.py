import os

from MNISTTester import MNISTTester

####################
# directory settings
script_dir = os.path.dirname(os.path.abspath(__file__))

#data_path = script_dir + '/mnist/data/'
model_path = script_dir + '/models_no_labels/mnist-cnn'
mnist = MNISTTester(
            model_path=model_path)

#################################
# prediction test with image file
# mnist = MNISTTester(model_path)
print ""
print "Thinking ..."
mnist.predict(script_dir + '/imgs/interactive.png')
