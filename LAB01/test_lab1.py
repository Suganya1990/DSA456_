
import unittest
# from lab1 import wins_rock_scissors_paper, factorial, fibonacci, sum_to_goal,UpCounter,DownCounter

def wins_rock_scissors_paper(plGuess, opGuess):
    #converts string into number
    p = convertOption(plGuess)
    o = convertOption(opGuess)

    if ( p == o   or p ==-1 or o ==-1 ):
        return False
    if(p ==1 and o ==3 ) or (p==2 and o ==1 ) or (p==3 and o ==2 ):
        return True
    elif(p==1 and o == 2) or (p==2 and o==3) or (p==3 and o ==1 ):
        return False


def convertOption(option):
    match(option.lower()):
        case 'rock':
            return 1
        case 'paper':
            return 2
        case 'scissors':
            return 3
        case _:
            return -1


def factorial(num):
    i = num-1
    factorialValue= num  
    if(num < 0):
        return 
    if(num == 0 ):
        return 1
    else:
        while (i > 0 and i < num   ):
            factorialValue = factorialValue*i 
            i = i-1
    return factorialValue

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return(fibonacci(n-1)+ fibonacci(n-2))



def sum_to_goal(dataArr, target):
    sumPair=[0,0]
    product = 0
    
    #Sort Array
    sortedArr = sortArr(dataArr)
    arrLen = len(sortedArr)
    
    #find complemntary number that euquals target - array[n]
    for i in range(arrLen):
        complimentNum = target-sortedArr[i]
        
        #then we search the array for that number 
        for j in range(arrLen):
            if(complimentNum == sortedArr[j]):
                sumPair[0]=sortedArr[j]
                sumPair[1]=sortedArr[i]
    
    product= sumPair[0]*sumPair[1]
    return product
   
              

def sortArr(data): 
    n = len(data) 
    i = 1
    for i in range(n):
        temp = data[i]
        j = i-1
        while temp < data[j] and j>=0:
            data[j+1] = data[j]
            j = j-1
        data[j+1]= temp
    return data


#Function 4cd 
class UpCounter:
    def __init__(self, step = 1):
        self.Counter  = 0 
        self.step = step 

    def count(self):
        return self.Counter
    def update(self):
        tempCounter = self.Counter + self.step
        self.Counter =tempCounter
    
class DownCounter(UpCounter):
    def __init__(self, step=1):
        super().__init__(step)

    def update(self):
         tempCounter = self.Counter - self.step
         self.Counter =tempCounter




class Lab1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of lab1"""
    
    def test_win_rock_scissors_paper(self):
        self.assertEqual(wins_rock_scissors_paper("rock","scissors"),True)
        self.assertEqual(wins_rock_scissors_paper("rock","paper"),False)
        self.assertEqual(wins_rock_scissors_paper("scissors".upper(),"paper"),True)
        self.assertEqual(wins_rock_scissors_paper("Scissors","Rock"),False)
        self.assertEqual(wins_rock_scissors_paper("paper","sCiSsOrs"),False)
        self.assertEqual(wins_rock_scissors_paper("paper".title(),"ROCK"),True)
        self.assertEqual(wins_rock_scissors_paper("paper","PaPeR"),False)
        self.assertEqual(wins_rock_scissors_paper("rock","ROCK"),False)
        self.assertEqual(wins_rock_scissors_paper("SCISSORS","scissors"),False)


    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(19),121645100408832000)
        self.assertEqual(factorial(8),40320)


    def test_fibonacci(self):
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        self.assertEqual(fibonacci(3),2)
        self.assertEqual(fibonacci(35),9227465)


    def test_sum_to_goal(self):
        mylist =[5741, 5742, 4234, 1950, 2255, 3899, 974, 1332, 726, 4208, 2914, 4721, 2094, 2252, 1892, 
                676, 3097, 2725, 1639, 1122, 4212, 3191, 616, 5346, 1121, 444, 2873, 2597, 1134, 1262, 3838, 
                1564, 4176, 1873, 4068, 3277, 1765, 4431, 1256, 924, 3440, 4143, 5444, 5653, 5436, 3992, 4902, 
                2476, 5976, 3699, 2683, 2786, 4001, 2293, 2191, 2530, 4336, 3000, 4713, 2061, 4900, 2844, 128, 
                4539, 465, 550, 5067, 2636, 5579, 512, 323, 4547, 4125, 4112, 4746, 3860, 1104, 1261, 1791, 5301, 
                3293, 1464, 3989, 193, 4036, 1132, 3247, 4618, 4033, 3332, 3579, 3221, 5410, 2242, 1495, 2513, 
                4430, 4508, 3262, 3259]

        self.assertEqual(sum_to_goal(mylist,8716),18969664)
        self.assertEqual(sum_to_goal(mylist,3385),1470976)
        self.assertEqual(sum_to_goal(mylist,7327),13257612)
        self.assertEqual(sum_to_goal(mylist,3103),2399496)
        self.assertEqual(sum_to_goal(mylist,3470),632461)
        self.assertEqual(sum_to_goal(mylist,0),0)
        self.assertEqual(sum_to_goal(mylist,3471),0)
        self.assertEqual(sum_to_goal(mylist,5080),0)


    def test_UPCounter(self):
        counter=UpCounter(5)
        counter.update()
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),15)
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),25)


    def test_DownCounter(self):
        counter=DownCounter(3)
        counter.update()
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),-9)
        counter.update()
        counter.update()
        self.assertEqual(counter.count(),-15)
 
if __name__ == '__main__':
    unittest.main()
