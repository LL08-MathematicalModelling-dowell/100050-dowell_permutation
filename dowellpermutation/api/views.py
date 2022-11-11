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
        except:
            sessiondata = ''
        #char = JSONParser().parse(request)
        char = request.data
        print(char)
        for i in char.values():
             char = i
        print(char)
        permutations = permuationsFunction(sessiondata,char)
        print(permutations)
        return Response(permutations, status=status.HTTP_201_CREATED)
