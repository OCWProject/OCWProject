# MIT6.0001- LECTURE 5: TUPLES, LISTS, ALIASING, MUTABILITY, CLONING


#############################
# Mutable: List             #
# Immutable: Tuple, String  #
#############################

# Tuples
# t1 = ()
# t2 = (1, "two", 3.0)
# print(t1)
# print(t2)
#
# # Returns multiple values with tuples
# def findDivisor(n1, n2):
#     divisor = ()
#     for i in range(1, min(n1, n2)):
#         if n1 % i == 0 and n2 % i == 0:
#             divisor += (i, )
#     return divisor
#
# divisor = findDivisor(12, 16)
# print(divisor)

# Lists, Mutability
# Create empty list
# L = []
# L = ['I dit it all', 4, 'love']
# for i in range(len(L)):
#     print(L[i])
##############################################################
# List operators                                             #
# L.append(e): adds the object e to the end of L             #
# L.count(e): returns numbers of time object e occurs in L   #
# L.insert(i, e): insert object e into L at index i          #
# L.extend(L2): adds items in L2 at the end of L             #
# L.remove(e): deletes the first occurrence of e in L        #
# L.index(e): returns the index of the                       #
#    # first occurrence of e in L -> Raise EXCEPTION         #
# L.pop(i): remove and return item at index i,               #
#    # otherwise return -1                                   #
# L.sort() sort elements of L (default: ASC order)           #
# L.reverse(): reverse elements order in L                   #
##############################################################

# L1 = [1, 2, 3, 4]
# L1.reverse()
# print(L1)
# L1.extend(L)
# print(L1)
# print(L1)

# Cloning
# Reference L1 = L
# Cloning L1 = L[:]
# L2 = [-1, 1, -3, 0]
# Aliasing: L2 = L1
#  <=> L1 & L2 are referenced to the same object
# L3 = L2
# L3.remove(-1)
# L3.remove(0)
# print('L2: ', L2)
# print('L3: ', L3)

# Cloning L2 = L1[:]
# L2 is copy all elements of L1
# but L1 and L2 are referenced 2 different objects

# L4 = [23, 6, 1994]
# L5 = L4[:]
# L5.remove(6)
# print('L4: ', L4)
# print('L5: ', L5)

# sort vs sorted
# sort: mutates list returns nothing
# sorted: does not mutates list
# L6 = [23, 6, 1994, 5, 11, 1995]
# L7 = L6[:]
# print('L6: ', L6)
# L6.sort()
# print('L6.sort(): ', L6)
# print()
# print('L7: ', L7)
# sorted(L7)
# print('sorted(L7): ', L7)
