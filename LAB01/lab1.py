
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
    print(factorialValue)
    return factorialValue










def fibonacci(num):
    for n in range(num):
        total = fibRecursion(n)
        if n == num-1:
            print(total)
            
     


def fibRecursion(n):
    if n <= 1:
        return n
    else:
        return(fibRecursion(n-1)+ fibRecursion(n-2))






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