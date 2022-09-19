from tkinter import N
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from django.shortcuts import render, redirect

from django.views import View
import json

# import pymongo
import pandas as pd
from django.core import serializers



class IndexView(View):

    def get(self, request):

        return render(request, 'calculator/index.html')


class DesktopTwoView(View):

    def get(self, request):
        return render(request, 'calculator/desktop-2.html')

class DesktopThreeView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-3.html')

class DesktopFourView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-4.html')

class DesktopFiveView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-5.html')

class DesktopSixView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-6.html')

class DesktopSevenView(View):
    def get(self, request):
        return render(request, 'calculator/desktop-7.html')


# def calculate(request):
#     def fact(n):
#         res = 1
#         for i in range (1, n+1):
#             res *= i
#         return res

#     def nPr(n, r):
#         return fact(n)/fact(n-r)

#         n = int(input("Enter the n value: "))
#         r = int(input("Enter the r value: "))
#         print("The nPr value is: ", nPr(n, r))




def permutations(request):
    method = request.method
    is_ajax = request.headers.get('X-Requested-with') == 'XMLHttpRequest'
    if is_ajax:
        if method == 'POST':
            data = json.load(request)
            payload = data.get('payload')

            # initialize result #
            # result = None
            # permutation_result = None
            # permutation_result = serializers.serialize('json', [ result, ])


            def fact(n):
                res = 1
                for i in range (1, n+1):
                    res *= i
                return res

            def nPr(n, r):
                return fact(n)/fact(n-r)

            # n = int(input("Enter the n value: "))
            # r = int(input("Enter the r value: "))
            n = int(payload['n'])
            r = int(payload['r'])

            print("The nPr value is: ", nPr(n, r))

            # RUN PERMUTATION FUNCTION HERE #
            data = {
                'status': 200,
                'n':n,
                'r':r,
                'result': nPr(n, r)
            }
            
            return JsonResponse({'data': data}, status=200)
            
        else:
            return JsonResponse({'response': 'something went wrong'}, status=400)
    else:
        return HttpResponseBadRequest('Invalid request')

    # return redirect('DesktopFourView')
        
    

def get_permutation(request):

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
        # x1 = payload['n']
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

   


index_view = IndexView.as_view()
desktop_two_view = DesktopTwoView.as_view()
desktop_three_view = DesktopThreeView.as_view()
desktop_four_view = DesktopFourView.as_view()
desktop_five_view = DesktopFiveView.as_view()
desktop_six_view = DesktopSixView.as_view()
desktop_seven_view = DesktopSevenView.as_view()




