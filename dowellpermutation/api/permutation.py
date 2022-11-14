

# def permuationsFunction(current,session):
#     numberOfVariables = int(input("Enter the Number of Variables You Want: "))
#     firstVariable = input("Enter First Variable: ")
#     permutationsVariables = [firstVariable]
#     permutationsList = []
#     for i in range(0,numberOfVariables-1):
#         nextVariable = input("Enter Next Variable: ")
#         for j in range(len(permutationsVariables)+1):
#             permutations = list(permutationsVariables)
#             permutations.insert(j, nextVariable)
#             permutationsList.append(permutations)
#         print(permutationsList)
#         permutationSelection = int(input("Enter the Index of Permutation that you want to select: "))
#         print("Selected Permutation: ", permutationsList[permutationSelection])
#         permutationsVariables = list(permutationsList[permutationSelection])
#         permutationsList.clear()
#     return(permutationsVariables)
# print(print(permuationsFunction()))


# session = ['A']
# char = ['B']
# calculate(char,session)  => return [[A,B],[B,A]]

# value = ['A','B']
# save(value) => save in session [A,B] => return [A,B]
# session = ['A','B']
# char = ['C']

# calculate(char,session) => return [[C,A,B],[A,C,B],[A,B,C]]

# value = ['C','A','B']
# save(value) => save in session [C,A,B] => return [C,A,B]
# session = ['C','A','B']

def permuationsFunction(permutationsVariables, nextVariable):
    permutationsList = []
    for j in range(len(permutationsVariables)+1):
        permutations = list(permutationsVariables)
        permutations.insert(j, nextVariable)
        permutationsList.append(permutations)
    return permutationsList

print(permuationsFunction(['A','B','C'],'4'))

# def callPermutationsFunction(nextVariable):
#     #numberOfVariables = int(input("Enter the Number of Variables You Want: "))
#     numberOfVariables = 3
#     #firstVariable = input("Enter First Variable: ")
#     firstVariable = 'A'
#     permutationsList = []
#     permutationsVariables = [firstVariable]
#     for i in range(0,numberOfVariables-1):
#         # nextVariable = input("Enter Next Variable: ")
#         permutationsList = permuationsFunction(permutationsVariables, nextVariable)
#         print(permutationsList)
#         permutationSelection = int(input("Enter the Index of Permutation that you want to select: "))
#         print("Selected Permutation: ", permutationsList[permutationSelection])
#         permutationsVariables = list(permutationsList[permutationSelection])
#         permutationsList.clear()

#     return permutationsVariables

# print(callPermutationsFunction())