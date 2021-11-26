# qs1 Palindrome check
def isPalindrome(phrase):
    return phrase == phrase[::-1]

'''print(isPalindrome(input("give a word to check if it is a palindrome : ")))'''

# qs2 Prime check
def isPrime(num):
    if num == 1:
        return True
    else:
        for i in range(2,num):
            if num%i==0:
                return False 
        return True
    
'''print(isPrime(int(input("Give a number to check if it is a prime num : "))))'''


#qs3 a number is in a given range check
def isInRange(start,end,num):
    return num in range(start,end)

'''print(isInRange(int(input("Give the start of the interval : ")),
                int(input("Give the end of the interval : ")),
                int(input("Give the num to check if he is in the given interval : "))))'''


#qs4 fact of a number
def fact(num):
    if num<=1:
        return 1
    return num*(fact(num-1))

'''print(fact(int(input("Give a number to calculate its factorila ! :"))))'''

#qs5 reverse a string
def reverseString(string):
    return string[::-1]

'''print(reverseString(input("Give a string to reverse : ")))'''

#qs6 sum of a list (we can use the sum(iterable) function)
def sumOfList(list):
    return sum(list)

'''print(sumOfList(int(input("give the number {} element for the list : ".format(i+1))) for i in range(int(input("give the len of the list : ")))))''' 

#qs7 max of 3 numbers (we will use a list of 3 and find its max)  
def maxOfThree(listOfNum):
    return max(listOfNum)

print(maxOfThree(int(input("give the {} number :".format(i+1))) for i in range(3)))