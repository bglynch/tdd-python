# First tested code--------------------------------------------------------
# def count_upper_case(message):
# 	count = 0
# 	for c in message:
# 		if c.isupper():
# 			count += 1
# 	return count

# Second tested code--------------------------------------------------------


def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") 			== 0, "Empty String should return 0"
assert count_upper_case("A")			== 1, "A should return 1"
assert count_upper_case("the  bEst")	== 1, "the  bEst should return 1"
assert count_upper_case("!@£$%^&*") 	== 0, "Characters should return 1"
assert count_upper_case("      ")		== 0, "Should return 0"
assert count_upper_case("HELLO-WORLD")	== 10, "Should return 0"

print("All test pass")







