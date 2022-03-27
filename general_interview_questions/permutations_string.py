
# Python program to print all permutations with
# duplicates allowed

# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
coll = []
def permute(a, l, r):
    if l == r:
        coll.append(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


# Driver program to test the above function
def test_permute():
    string = "ABC"
    n = len(string)
    a = list(string)
    permute(a, 0, n-1)
    print(coll)
    assert coll == ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']
