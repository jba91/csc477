#!/usr/bin/python3.5

import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

### test to make sure matplotlib works
print("\n---verify that matplotlib works---")
plt.plot([1,2,3,4])
plt.plot([2,4,7,14])
plt.ylabel('Just a TEST')
plt.show()
print(); input("Press Enter to continue...")

### read in our crime data
### data is from https://catalog.data.gov/dataset/crime-data-from-2010-to-present
z = pandas.read_csv("crime.csv.full")
print("\n---show the head (first few columns of data)---")
print(z.head())
print(); input("Press Enter to continue...")

# prints all columns
print("\n---show the columns in crime.csv---")
print(z.columns)
print(); input("Press Enter to continue...")

# show just the Age
print("\n---show the columns in crime.csv---")
print(z.Age)
print(); input("Press Enter to continue...")

# histogram of all Age
print("\n---show a historgram of all the Ages in the data---")
plt.hist(z["Age"])
plt.show()
print(); input("Press Enter to continue...")

### print crimes with Victims older than 90
print("\n---show all the crimes with victims older than 90 yrs old---")
print(z[z["Age"] > 90.0].iloc[0])
print(); input("Press Enter to continue...")

# k-means clustering
# find patterns in the data by grouping similar rows together
# create model with 2 params - num of clusters and random stat.
kmeans_model = KMeans(n_clusters=5, random_state=1)

# get numeric columns from z
good_cols = z._get_numeric_data()
print(good_cols)
print(); input("Press Enter to continue...")

# fit the model using the good columns
# COULD NOT GET THIS TO SUCCEED
kmeans_model.fit(good_cols)
exit(0)


# get cluster assignments
labels = kmeans_model.labels_
print(type(labels))

### clusters : create PCA model
pca_2 = PCA(2)

# fit the PCA model using the columns defined earlier
plot_cols = pca_2.fit_transform(good_cols)

# create the scatter plot
plt.scatter(x=plot_cols[:,0], y=plot_cols[:,1], c=labels)

# display the plot
plt.show()

print(); input("Press Enter to continue...")
