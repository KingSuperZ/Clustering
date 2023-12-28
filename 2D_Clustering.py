# My plan is to use the variable C1 and combine it with the y coordinates in 
# correlation to it to the original using indexing and then we do the same thing for
# the variable C2 and the rest of the y coordinates
# I want to take the datapoints and take the data points so that the gaps between them will be as small as possible

# Make two new empty lists, C1 and C2
# Create a 2D array, X
# Make it into two lists, one with the x coordinates and one with the y coordinates
# Calculate the standard deviation on both lists
# Take each stds and find out which one is bigger
# Use the list that has the highest std and sort it in number order, CordList
# Find the distance between each point from CordList
# Find which gap is the biggest
# Find which two numbers make the biggest gap from CordList
# Find out which number is the lowest of the two numbers
# Put that number and all numbers lower than it into the first empty list, C1
# Find out which number is the highest of the two numbers that make the biggest gap from CordList
# Put that number with all numbers higher than it into the second empty list, C2
# Append the x coordinates from the array into C1 and C2 based on where they belong


import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

#X = np.array([[1,3],[2,0],[13,14],[10,9]])
#X = np.array([[0,0],[0,1],[0,5]]) 
#X = np.array([[0,0],[1,0],[5,0]])
X,_ = make_blobs(n_samples = 1000, n_features = 2, centers = 2, cluster_std = 0.5)

plt.scatter(X[:,0],X[:,1])
plt.figure()
xcord = X[:,0]
ycord = X[:,1]
xstd = np.std(xcord)
ystd = np.std(ycord)


if ystd > xstd:
   
   CordArg = np.argsort(ycord) 
   CordList = ycord[CordArg] # Array of datapoints

   gaps = [] # Creates a list for the gaps of the datapoints

   for i in range(0,len(CordList)-1): # Iterates through all of the datapoints 
       gaps.append(CordList[i+1] - CordList[i]) # Finds the gaps between the datapoints

   G = np.array(gaps) # Changes the list of gaps to an array
   #maxgap = Y.max() # Finds the biggest gap in the list

   C1 = [] # List for first cluster
   C2 = [] # List for second cluster

   for i in range(0,len(X)): # Iterates through the array
       if CordList[i] <= CordList[G.argmax()]: # States that if the number is less than the biggest gap then that will be added to the first cluster
           C1.append(CordList[i])
       elif CordList[i] > CordList[G.argmax()]: #  States that if the number is greater than the biggest gap then that will be added to the second cluster
           C2.append(CordList[i])

   C1 = np.array(C1)
   C2 = np.array(C2)
   X2 = xcord[CordArg]
   C3 = np.array(X2[:len(C1)])
   C4 = np.array(X2[len(C1):])

   plt.scatter(C3,C1, s = 10, c = "red")
   plt.scatter(C4,C2, s = 10, c = "blue")

   zeros = np.zeros(len(C1))
   ones = np.ones(len(C2))
   ypred = np.append(zeros,ones)
   print(ypred)
if xstd > ystd:
    CordArg = np.argsort(xcord) 
    CordList = xcord[CordArg] # Array of datapoints

    gaps = [] # Creates a list for the gaps of the datapoints

    for i in range(0,len(CordList)-1): # Iterates through all of the datapoints 
        gaps.append(CordList[i+1] - CordList[i]) # Finds the gaps between the datapoints

    G = np.array(gaps) # Changes the list of gaps to an array
    #maxgap = Y.max() # Finds the biggest gap in the list

    C1 = [] # List for first cluster
    C2 = [] # List for second cluster

    for i in range(0,len(X)): # Iterates through the array
        if CordList[i] <= CordList[G.argmax()]: # States that if the number is less than the biggest gap then that will be added to the first cluster
            C1.append(CordList[i])
        elif CordList[i] > CordList[G.argmax()]: #  States that if the number is greater than the biggest gap then that will be added to the second cluster
            C2.append(CordList[i])

    C1 = np.array(C1)
    C2 = np.array(C2)
    X2 = ycord[CordArg]
    C3 = np.array(X2[:len(C1)])
    C4 = np.array(X2[len(C1):])

    plt.scatter(C1,C3, s = 10, c = "red")
    plt.scatter(C2,C4, s = 10, c = "blue")

    zeros = np.zeros(len(C1))
    ones = np.ones(len(C2))
    ypred = np.append(zeros,ones)
    print(ypred)
