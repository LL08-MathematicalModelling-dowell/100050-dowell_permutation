def do_permutation(word):
    if len(word) == 1:
        return [word]

    perms = do_permutation(word[1:])
    char = word[0]
    result = []

    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i]+ char + perm[i:])
    return result

# def do_permutation(char,data):
#     if len(char) == 1:
#         return [char]

#     perms = do_permutation(char[1:],data)
#     char = char[0]
#     result = []

#     for perm in perms:
#         for i in range(len(perm)+1):
#             result.append(perm[:i]+ char + perm[i:])
#     return result


# print(do_permutation('A','B'))


#slicing the array and inserting new object
def insert(var,string,i):
    output = string[:i] + var + string[i:]
    return output

#splitting a list into list of lists
# def split(word):
#     return [char for char in word]

# #calculate permutations of two variables
# def do_permutation(char,data):
#     perms = [perm for perm in char]
#     perms1=[split(perm) for perm in perms]
#     new_perms=[]
#     for i in perms1:
#         for j in range(0,len(i)+1):
#             new_perm= insert(data,i,j)
#             new_perms.append(new_perm)
#     return new_perms

# A Python program to print all



# print(do_permutation('A','B'))