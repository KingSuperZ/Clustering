import numpy as np

X = np.array([8,9,12,13]) # Array of datapoints

X.sort() # Puts all of the numbers in number order

gaps = [] # Creates a list for the gaps of the datapoints

for i in range(0,len(X)-1): # Iterates through all of the datapoints 
    gaps.append(X[i+1] - X[i]) # Finds the gaps between the datapoints

Y = np.array(gaps) # Changes the list of gaps to an array
maxgap = Y.max() # Finds the biggest gap in the list
Y.argmax()

C1 = [] # List for first cluster
C2 = [] # List for second cluster

for i in range(0,len(X)): # Iterates through the array
    if X[i] <= X[Y.argmax()]: # States that if the number is less than the biggest gap then that will be added to the first cluster
        C1.append(X[i])
    elif X[i] > X[Y.argmax()]: #  States that if the number is greater than the biggest gap then that will be added to the second cluster
        C2.append(X[i])

print(C1,C2) # Prints both of the clusters