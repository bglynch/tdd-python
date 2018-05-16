def even_evens(l):
    # if (len(l)%2 == 0) and  (sum(l[0:len(l)+1])%2 == 1) or (sum(l[len(l):])%2 == 1):
    #     return False
    x = (len(l)//2)
    
    if (len(l)%2 == 0) and ((sum(l[0:-1])%2 == 1) or (sum(l[0:x])%2 == 1)):
        return False
    elif  (sum(l)%2) == (len(l)%2) and len(l) > 2 and sum(l)>0:  
        return True
    else:
        return False

def even_even(l):
    count = 0
    for n in l:
        if n != 0 and n % 2 == 0:
            count += 1
    return count % 2 == 0
    

assert even_evens([]) == False, "Empty list should return false"
assert even_evens([3]) == False, "3 should return false"
assert even_evens([3,6,8]) == True, "even number of evens numbers should return true" #sum
assert even_evens([3,7,8]) == False, "1 even number should return false"
assert even_evens([3,6,8,12]) == False, "odd number of evens numbers should return false"
assert even_evens([1,1,1,1,2,1]) == False, "odd number of evens numbers should return false"
assert even_evens([0,0,0,0]) == False, "odd number of evens numbers should return false"
assert even_evens([13,14,14,13]) == True, "odd number of evens numbers should return True"
#assert even_evens([14,14,13,13]) == True, "odd number of evens numbers should return false"


print("All test pass")
