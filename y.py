"""KNN classification program"""

from sklearn.neighbors import KNeighborsClassifier
X = [[30],[39],[40],[50],[60],[20],[10],[70]]
Y = [0,0,1,1,1,0,0,1]
classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )
classifier.fit(X,Y)
X_marks=[[50]]
print(classifier.predict(X_marks))
