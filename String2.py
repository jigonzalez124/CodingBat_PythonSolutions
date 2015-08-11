##Given a string, return a string where for every char in the original, there are two chars. 

def double_char(str):
  
    phrase = ''
    for i in range(len(str)):
        phrase += str[i]
        phrase += str[i]
    return phrase



##-------------------------------------------------
#Return the number of times that the string "hi" appears anywhere in the given string.

def count_hi(str):
  
    count = 0
    for i in range(len(str)-1):
        if(str[i:i+2] == 'hi'):
            count += 1
    return count



##-------------------------------------------------
##Return True if the string "cat" and "dog" appear the same number of times
##in the given string.

def cat_dog(str):
  
    countCat = 0
    countDog = 0
    
    for i in range(len(str)-2):
        if(str[i:i+3]=='cat'):
            countCat+=1
        if(str[i:i+3]=='dog'):
            countDog+=1
    if(countCat == countDog):
        return True
    return False



##-------------------------------------------------
##Return the number of times that the string "code" appears anywhere in the given string,
##except we'll accept any letter for the 'd', so "cope" and "cooe" count. 

def count_code(str):
    
    count = 0
    for i in range(len(str)-3):
        if(str[i:i+2] == 'co'):
            if(str[i+3] == 'e'):
                count+=1
    return count



##-------------------------------------------------
##Given two strings, return True if either of the strings appears at the very end of
##the other string, ignoring upper/lower case differences (in other words, the computation
##should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string. 

def end_other(a, b):
  
    if (len(a) <= len(b)):
        if(a.lower() == b[-len(a):].lower()):
            return True
        return False
    if (len(b) <= len(a)):
        if(b.lower() == a[-len(b):].lower()):
            return True
        return False
    return False



##-------------------------------------------------
##Return True if the given string contains an appearance of "xyz" where the xyz is not
##directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

def xyz_there(str):

    skip = 0
    for i in range(len(str)-2):
        if(str[i:i+3] =='xyz' and skip == 0):
            return True
        if(str[i] == '.'):
            skip = 1
        elif(skip == 1):
            skip = 0
    return False
