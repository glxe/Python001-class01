from sklearn import datasets

iris = datasets.load_iris()
X, y = iris.data, iris.target

print(X, y)

print(iris.feature_names)

print(iris.target_names)