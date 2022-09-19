# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 11:30:23 2022

@author: Bradley
"""


def permutations():

    import pymongo
    import pandas as pd

    #database connection
    """
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]

    mycol1 = mydb["permutations1"]
    mycol2 = mydb["permutations_r<n"]
    mycol3 = mydb["combinations_r<n"]
    """
    #user defined functions

    #uniqueness in the list
    def unique(list1):
        unique_list = []
        for x in list1:
            if x not in unique_list:
                unique_list.append(x)
        return unique_list

    #to take inputs (one by one)
    def inputCharacter():
        x1 = input("Choose your character to insert: ")
        var=[]
        var.append(x1)
        return var

    #slicing the array and inserting new object
    def insert(var,string,i):
        output = string[:i] + var + string[i:]
        return output
    
    #splitting a list into list of lists
    def split(word):
        return [char for char in word]

#-------------------------------------------------------- 
#--------------------------------------------------------
    flag = True
    string = ""
    new_perms=[]
    new_perms.append(string)
    choice = 1

    while (flag):
        
        if (choice == 1 and new_perms):
        
            #to list out variables
            z=[]
            for i in new_perms:
                y=i[(len(new_perms[0])-1):]
                z.append(y)
                d=unique(sorted(z))

            perms = [perm for perm in new_perms]           
            perms1=[split(perm) for perm in perms]
            
            #inserting into mongodb
            doc1={ "variables":d,
                   "AoC":str(choice),
                   "Permutations":perms}
            #mycol1.insert_one(doc1)

        else:
            #to list out variables 
            z=[]
            for i in new_perms:
                y=i[(len(new_perms[0])-1):]
                z.append(y)
                d=unique(sorted(z))
            
            #user input to save particular permutation
            x=int(input("Enter the permutation to be saved, by indication it's position: "))
            perms = [new_perms[x-1]]
            print("Permutation to be saved is: ")
            
            perms1=[split(perm) for perm in perms]
            print(perms1)
            
            #inserting permutation to mongodb
            doc1={ "variables":d,
                   "AoC":str(choice),
                   "Permutations":perms1}
            #mycol1.insert_one(doc1)    
            
        
        #adding inputs 
        char = inputCharacter()
        new_perms=[]
    
        for i in perms1:
            for j in range(0,len(i)+1):
                new_perm= insert(char,i,j)
                new_perms.append(new_perm)

        print("new permutations are printing")
        print(new_perms)
        print("the number of permutations is ",len(new_perms))
    
        a=int(input("select '1' to save particular permutation and add new variable or '2' to just save a permutation and proceed: "))
        
        if a==1:
            choice=2
            flag=True
        
        if a==2 :
            flag=False
            z=[]
            for i in new_perms:
                y=i[(len(new_perms[0])-1):]
                z.append(y)
                d=unique(sorted(z))
            
            #user input to save particular permutation
            x=int(input("select which permutation  to be saved, by indicating it's position: "))
            perms = [new_perms[x-1]]
            print("Permutation to be saved is: ")
            
            perms1=[split(perm) for perm in perms]
            print(perms1)
            
            #inserting permutation into mongodb
            doc1={ "variables":d,
                  "AoC":str(choice),
                  "Permutations":perms1}
            #mycol1.insert_one(doc1)

        
    #Computing permutations and combinations of size r
    a=int(input("select '1' to make r <= n sized permutations or\ select '2' to make r <=n sized combinations : " ))
        
    if a==1:
        rvalue=int(input("Enter r value <= n: "))
        z=[]
        for i in new_perms:
            y=i[(len(new_perms[0])-rvalue):]
            z.append(y)
        d=unique(z)
    
        d1=[split(i) for i in d]
            
        doc2={"Permutations":d1}
        #mycol2.insert_one(doc2)
        
        df1=pd.DataFrame(d)
        print("the permutations are: ")
        print(df1)
        flag=False
        
    if a==2:
        rvalue=int(input("Enter r value <= n: "))
        z=[]
        for i in new_perms:
            y=i[(len(new_perms[0])-rvalue):]
            z.append(y)
        d=unique(z)
        
        x=[]
        for i in d:
            r=sorted(i)
            x.append(r)
        e=unique(x)
            
        e1=[split(i) for i in e]
            
        doc3={"Permutations ":e1}
        #mycol3.insert_one(doc3)
        
        df2=pd.DataFrame(e)
        print("the combinations are: ")
        print(df2)
        flag=False

    #return()    
permutations()
#permutations(Apple,1,1,TV,2)




