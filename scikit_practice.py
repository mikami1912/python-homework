from sklearn import datasets
from sklearn import svm
import numpy

clf = svm.SVC(gamma=0.001, C=100.)
iris = datasets.load_iris()
digits = datasets.load_digits()



print (digits.data)
print (digits.target)
clf.fit(digits.data[:-1], digits.target[:-1])
result = clf.predict(digits.data[-1:])
print (result)
print (digits.images[0])
