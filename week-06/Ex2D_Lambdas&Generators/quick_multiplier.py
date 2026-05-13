# Lab 1
#2. Create the doubler lambda
doubler = lambda n: n * 2

# 3. Print the variable
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))

# 4. Create the tripler lambda (Same logic, just changing the multiplier to 3.)
tripler = lambda n: n * 3

# Test with the same values
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))

# 5. The multiplier function 
def multiplier(m):
    return lambda n: n * m

#  Create the specific variables using the function
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# 6. Print each of the new variables
print(quadrupler(10))  
print(quintupler(10))   
print(sextupler(10))    
print(septupler(10))    
print(octupler(10))     
print(nonupler(10))     
print(decupler(10))     

