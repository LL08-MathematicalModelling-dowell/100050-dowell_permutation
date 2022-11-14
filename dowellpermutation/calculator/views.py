import json
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .do_permutation import do_permutation

def calcpermutations(request):
    method = request.method
    is_ajax = request.headers.get('X-Requested-with') == 'XMLHttpRequest'
    if is_ajax:
        if method == 'POST':
            data = json.load(request)
            payload = data.get('payload')

            def fact(n):
                res = 1
                for i in range (1, n+1):
                    res *= i
                return res

            def nPr(n, r):
                return fact(n)/fact(n-r)

            n = int(payload['n'])
            r = int(payload['r'])

            print("The nPr value is: ", nPr(n, r))

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


def index(request):
    return render(request, 'calculator/index.html')

def permutataionselect(request):
    return render(request, 'calculator/permutationselect.html')


def permuationsFunction(permutationsVariables, nextVariable):
    permutationsList = []
    for j in range(len(permutationsVariables)+1):
        permutations = list(permutationsVariables)
        permutations.insert(j, nextVariable)
        permutationsList.append(permutations)
    return permutationsList


def save(request):
    if request.method == 'POST':
        data = request.POST
        print("data ",data)
        # print("data['char[0][]''] ",data['char[0][]'])
        if data.getlist('char[0][]'):
            print("req data :",data.getlist('char[0][]'))
            request.session['session'] = data.getlist('char[0][]')
            print("Session data :",request.session['session'])
            return JsonResponse(request.session['session'], safe=False,status=200)
        else:
            print("req data :",data.getlist('char[]'))
            request.session['session'] = data.getlist('char[]')
            print("Session data :",request.session['session'])
            return JsonResponse(request.session['session'], safe=False,status=200)


def clear_session(request):
    if request.method == 'POST':
        request.session.flush()
        message = "Session cleared"
        return JsonResponse({'data': message},safe=False, status=200)

def calculateperm(request, format=None):
    if request.method == 'POST':
        try:
            sessiondata = request.session['session']
        except:
            sessiondata = ''
        #char = JSONParser().parse(request)
        char = request.POST['char']
        print("char :",char)
        # for i in char.values():
        #      char = i
        permutations = permuationsFunction(sessiondata,char)
        print("permutations :", permutations)
        return JsonResponse(permutations,safe=False, status=200)
