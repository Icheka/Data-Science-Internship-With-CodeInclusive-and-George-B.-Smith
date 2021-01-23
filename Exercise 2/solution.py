#!/usr/bin/env python
# coding: utf-8

# In[57]:


'''
Working with NumPy, create a function whic generates 20 random integers between 20
and 70.
Compute the mean, variance, standard deviation, median, naximum and minimmum values
of this data set. The result should be returned as a dictionary.
Use appropraite names for the keys of the dictionary. The dictionary being returned
should include the data generated as one of its values.
'''

import numpy as np
import matplotlib.pyplot as plt

class NpData:
    def __init__(self, min, max, size=(1,1)):
        self.arr = self._generateRandom(min, max, size)
    
    def _generateRandom(self, min, max, size):
        return np.random.randint(min, max, size)
    
    def computeMinBool(self, val):
        pass
    
    def computeZScores(self):
        '''
        (data - mean)/std
        '''
        arr = np.array([((n - self.result['mean'])/self.result['std-dv']) for n in self.arr])
        return arr
    
    def computeProps(self):
        result = {}
        result['data-set'] = self.arr
        result['mean'] = np.mean(self.arr)
        result['variance'] = np.var(self.arr)
        result['std-dv'] = np.std(self.arr)
        result['median'] = np.median(self.arr)
        result['minimum'] = np.amin(self.arr)
        result['maximum'] = np.amax(self.arr)
        
        self.result = result
        
        return result
    
    def boxplot(self):
        plt.boxplot(self.arr)
        plt.show()
        
    def modify(self, idx, val):
        self.arr[0, idx] = val
    
    
data = NpData(20, 70, (1,20))
result = data.computeProps()

def question1():
    print("\n1) Data set:>> {}".format(result))
    
def question2a():
    p = np.sum(data.arr < result['mean'])
    print("\n2a) Elements less than mean:>> {}".format(p))
    
def question2b():
    p = data.computeZScores()
    print("\n2b) Z-scores:>> {}".format(p))
    q = np.all((p >= -3) & (p <= 3))
    if (q == True):
        print("All elements of the ndarray lie between -3 and 3")
    else:
        print("One or more elements of the ndarray lie outside the (-3 <= x <= 3) range")

def question3a():
    print("\n3a")
    data.boxplot()
    
def question4():
    print("================== After modifying the data set ==================")
    print("4")
    data.modify(15, 270)
    question1()
    question2a()
    question2b()
    question3a()
  
def runThroughEachQuestion():
    question1()
    question2a()
    question2b()
    question3a()
    question4()
        
runThroughEachQuestion()
