'''
Question 3: Write a program that creates a menu for a statistical calculator.
The calculator has the following functions:
i) Mean
ii) Mode
iii) Median
iv) Variance
'''
import sys
from collections import Counter

class Calculator:
    def __init__(self):
        self.menu = {0: 'Mean', 1: 'Mode', 2: 'Median', 3: 'Variance'}

    #utils operations
    def printMenu(self):
        for fx in self.menu:
            print('{} : {}'.format(fx+1, self.menu[fx]))

    def exit(self):
        print("Bye")
        sys.exit()

    def doOp(self):
        try:
            N = int(input("How many numbers do you want to compute? N: "))
        except ValueError:
            print("Please, only enter integers in the calculator")
            self.exit()
        else:
            array = input("Enter a comma-separated list of numbers to compute: ")
            array = array.split(",")
            if (len(array) != N):
                    print("You must enter only as much numbers as you specified.")
                    print("You entered {} as N but entered {} number of numbers.".format(N, len(array)))
                    self.exit()
            else:
                return [N, array]

    def doAgain(self):
        op = input("Perform another operation? [y/n] ")
        if (op.strip() == "y"):
            self.start()
        else:
            self.exit()

    def failedAndDoAgain(self):
        print("Invalid input.")
        self.doAgain()

    #calc operations
    def selfMean(self, array):
        #because elements of array are strings, sum(array) will fail
        ans = 0
        for n in array:
            ans += int(n)
        return (ans/len(array))
        
    def Mean(self):
        #tmp = array(N, array(x, y, ..))
        tmp = self.doOp()
        ans = self.selfMean(tmp[1])
        print("The mean is: {}".format(ans))
        self.doAgain()

    def Mode(self):
        tmp = self.doOp()
        
        map_ = Counter(tmp[1])
        map_extract = dict(map_)
        mode = [k for k, v in map_extract.items() if v == max(list(map_.values()))]

        if (len(mode) == tmp[0]):
            print("The list of numbers you entered does not have a mode.")
        else:
            print("Mode(s) for {}: {}".format(tmp[1], ''.join(map(str, mode))))
        self.doAgain()

    def Median(self):
        tmp = self.doOp()
        N = tmp[0]
        array = tmp[1]
        array.sort()

        if ((tmp[0] % 2) == 0):
            #even list
            #[1,2,3,4]
            #let n = len(array)
            #let m1 = array[(n/2) - 1]
            #let m2 = array[array.indexOf(m1) + 1]
            #let ans = (m1 + m2) / 2
            m1 = int(array[N//2 - 1])
            m2 = int(array[N//2])
            median = (m1 + m2)/2
        else:
            #odd list
            #[1,2,3,4,5]
            #n = len(array)
            #m = array[Math.floor(n/2)]
            median = array[N//2]
        print("The median of {} is: {}".format(array, median))
        self.doAgain()

    def Variance(self):
        tmp = self.doOp()
        # v = sum of (n - mean)**2 / N
        N = tmp[0]
        mean = self.selfMean(tmp[1])
        deviations = [(int(x) - mean) ** 2 for x in tmp[1]]
        variance = sum(deviations) / N
        print("The variance of {} is: {}".format(tmp[1], variance))
        self.doAgain()
        

    #start
    def start(self):
        fx = input("Enter 0 to quit, 1 to show menu: ")
        if (fx == '0'):
            self.exit()
        elif (fx == '1'):
            print("Menu")
            self.printMenu()
            op = input("Enter a number to perform the corresponding operation: ")

            if (op == '1'):
                self.Mean()
            elif (op == '2'):
                self.Mode()
            elif (op == '3'):
                self.Median()
            elif (op == '4'):
                self.Variance()
            else:
                self.failedAndDoAgain()
        else:
            self.failedAndDoAgain()

calculator = Calculator()
calculator.start()
