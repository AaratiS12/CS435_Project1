import random
import sys
def getRandomArray(n):
    dicts = {}
    arr = []
    for i in range(n):
        a = True
        while a:
            #val = random.randint(0,1000)
            val = random.randint(-sys.maxint - 1, sys.maxint)
            ans = dicts.get(val, "no")
            if ans == "no":
                dicts[val] = 1
                a = False
        arr.append(val)
    return arr
        
        #val = random.randint(-sys.maxint - 1, sys.maxint)
def getSortedArray(n):
    arr = []
    for i in range(n,0,-1):
        arr.append(i)
    return arr
    
def main():
    print(getRandomArray(5))
    print(getSortedArray(5))
if __name__ == "__main__":
    main()
