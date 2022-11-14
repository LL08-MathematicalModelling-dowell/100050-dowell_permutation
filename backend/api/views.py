#from calculator.do_permutation import do_permutation
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

def permuationsFunction(permutationsVariables, nextVariable):
    permutationsList = []
    for j in range(len(permutationsVariables)+1):
        permutations = list(permutationsVariables)
        permutations.insert(j, nextVariable)
        permutationsList.append(permutations)
    return permutationsList


@api_view(['GET'])
def index(request):
    return Response("Hello, Welcome to Dowell Permutation Calculator.")



@api_view(['GET', 'POST'])
def save(request):
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        data = request.data
        print("data ",data)
        if data.getlist('char[0][]'):
            print("req data :",data.getlist('char[0][]'))
            request.session['session'] = data.getlist('char[0][]')
            print("Session data :",request.session['session'])
            return Response(request.session['session'], status=status.HTTP_201_CREATED)
        else:
            print("req data :",data.getlist('char[]'))
            request.session['session'] = data.getlist('char[]')
            print("Session data :",request.session['session'])
            return Response(request.session['session'], status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def clear_session(request):
    if request.method == 'POST':
        request.session.flush()
        message = "Session cleared"
        return Response(message,status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def permutation(request, format=None):
    if request.method == 'POST':
        try:
            sessiondata = request.session['session']
            print("try sessiondata :",sessiondata)
        except:
            sessiondata = ''
            print("except sessiondata :",sessiondata)
        #char = JSONParser().parse(request)
        char = request.data
        print(char)
        for i in char.values():
             char = i
        print(char)
        permutations = permuationsFunction(sessiondata,char)
        print(permutations)
        return Response(permutations, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def permutations(request):
    if request.method == 'POST':
        """
        requst data format
        {
            "n": 5,
            "r": 3
        }
        """
        data = request.data
        print("data ",data)
        print("type of data ",type(data))
        n = int(data['n'])
        r = int(data['r'])
        print("n ",n)
        print("r ",r)
        def fact(n):
            res = 1
            for i in range (1, n+1):
                res *= i
            return res

        def nPr(n, r):
            return fact(n)/fact(n-r)


        print("The nPr value is: ", nPr(n, r))

        data = {
                'status': 200,
                'n':n,
                'r':r,
                'result': nPr(n, r)
        }
        return Response({'data': data}, status=200)

    else:
        return Response({'data': 'Invalid Request'}, status=400)