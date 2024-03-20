#from sklearn.datasets import load_iris
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot



#load_iris


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

print(dataset)
print(dataset.shape)

# head(Peek at the Data)
print(dataset.head(3))

# descriptions(count, mean, the min, max values,some percentiles)
print(dataset.describe())

# class distribution(number of instances (rows))
print(dataset.groupby('class').size())

# box and whisker plots for input numeric variables
dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
pyplot.show()

# histograms of each input variable
dataset.hist()
pyplot.show()




from sklearn.datasets import load_diabetes
diabetes = load_diabetes()

print(diabetes.data.shape, diabetes.target.shape)

print(diabetes.data[0:2])
print(diabetes.target[0:2])


import matplotlib.pyplot as plt
plt.scatter(diabetes.data[:,5], diabetes.target)
plt.xlabel('5rd feature')
plt.ylabel('target data')
plt.show()