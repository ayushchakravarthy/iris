# summarize the dataset
from pandas import read_csv

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

# Print Shape
print(dataset.shape)

# Print head
print(dataset.head(20))

# Print Description
print(dataset.describe())

# Print Class Distribution
print(dataset.groupby('class').size())
