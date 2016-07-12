import svm
from svmutil import *

#training data
labels = [0, 1, 1, 2]
samples = [[0, 1, 0], [1, 1, 1], [1, 1, 0], [0, 0, 0]]

#SVM params
param = svm_parameter()
param.C = 10
param.kernel_type = LINEAR
#instantiate the problem
problem = svm_problem(labels, samples)
#train the model
model = svm_train(problem, param)
# saved model can be loaded as below
#model = svm_load_model('model_file')

#save the model
svm_save_model('model_file', model)

#test data
test_data = [[0, 1, 1], [1, 0, 1]]
#predict the labels
p_labels, p_accs, p_vals = svm_predict([0]*len(test_data), test_data, model)
print p_labels



