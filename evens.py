# Write a function that accepts a list of numbers and returns True if the list contains an even number of even numbers.
# This is a relatively simple statement, most program specifications are for more complex. However even a program as simple as this as room for some ambiguity.


# INITIAL CODE FOR EVEN NUMBER OF EVENS FUNCTIONS -------------------------------------------------------------------

# def even_evens2(l):
    # if (len(l)%2 == 0) and  (sum(l[0:len(l)+1])%2 == 1) or (sum(l[len(l):])%2 == 1):
    #     return False
    # x = (len(l)//2)
    
    # if (len(l)%2 == 0) and ((sum(l[0:-1])%2 == 1) or (sum(l[0:x])%2 == 1)):
    #     return False
    # elif  (sum(l)%2) == (len(l)%2) and len(l) > 2 and sum(l)>0:  
    #     return True
    # else:
    #     return False

# REVISED CODE FOR EVEN NUMBER OF EVENS FUNCTIONS -------------------------------------------------------------------
    
def even_evens(l):
    if 0 in l:
        l.remove(0)
    if len(l) < 2:                          #list with 0 or 1 item
        return False
    if sum(l) == 0:                         #items all 0
        return False
    if len(l)%2 == 1 and sum(l)%2 == 1 and sum(l[0:-1])%2 == 0 :     # odd no. of items, all odd
        return False  
    if len(l)%2 == 0 and sum(l)%2 == 0 and sum(l[0:-1])%2 != 0 and l[-1]%2 != 0 and (l[-1]+l[-2])%2 == 1:     # case 12.
        return True
    if len(l)%2 == 0 and sum(l)%2 == 0 and sum(l[0:-1])%2 == 1 and l[-1]%2 != 0 :     # even no. of items, all odd
        return False
    if len(l)%2 == 1 and sum(l)%2 == 1:     # odd no. of items, even no. of evens
        return True
    if len(l)%2 == 0 and sum(l)%2 == 0:     # even no. of items, even no. of evens
        return True
    if len(l)%2 == 0 and sum(l)%2 == 1:     # even no. of items, odd no. of evens
        return False
    if len(l)%2 == 1 and sum(l)%2 == 0:     # odd no. of items, odd no. of evens
        return False


# LOOP CODE FOR EVEN NUMBER OF EVENS FUNCTIONS -------------------------------------------------------------------

# def even_even(l):
#     count = 0
#     for n in l:
#         if n != 0 and n % 2 == 0:
#             count += 1
#         if count == 0:
#             return False
#         if count % 2 == 0:
#             return True
#         else:
#             return False
    
assert even_evens([]) == False, "01. Empty list should return False"
assert even_evens([3]) == False, "02. One number should return False"
assert even_evens([0,0,0,0]) == False, "11.  should return False"
assert even_evens([3,6,8]) == True, "03. Two even numbers should return True"
assert even_evens([3,6,8,6,8]) == True, "04. Four even numbers should return True"
assert even_evens([3,7,8]) == False, "05. should return False"
assert even_evens([3,7,8,12]) == True, "06. should return True"
assert even_evens([3,7,9,12]) == False, "07. should return False"
assert even_evens([1,3,5]) == False, "08. should return False"
assert even_evens([1,3,5,9]) == False, "09. should return False"
assert even_evens([1,1,1,1,2,1]) == False, "10. should return false"
assert even_evens([5,2,8,13]) == True, "12. should return True"
assert even_evens([5,2,2,3,4,3,13]) == False, "13. should return Flase"
assert even_evens([0,13]) == False, "14. should return False"
assert even_evens([0,0,13]) == False, "15. should return False"
# assert even_evens([1,3,2,2,13]) == True, "16. should return True"
# assert even_evens([1,3,0,2,2,0,13]) == True, "17. should return True" 


print("All test pass")
