# from calculator.do_permutation import do_permutation
import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

from .connection import connection, get_event_id


inserted_id = None


def permuationsFunction(permutationsVariables, nextVariable):
    if nextVariable == "":
        return [permutationsVariables]
    permutationsList = []
    for j in range(len(permutationsVariables) + 1):
        permutations = list(permutationsVariables)
        permutations.insert(j, nextVariable)
        permutationsList.append(permutations)
    return permutationsList


@csrf_exempt
@api_view(["GET", "POST"])
def index(request):
    return Response(
        {"response": "Welcome to Dowell Permutation API v1"}, status=status.HTTP_200_OK
    )


@csrf_exempt
@api_view(["GET", "POST"])
def calcperm(request):
    """
    1. Get the data from the request , r data and n data
    2. calculate the permutations
    3. save on dowell connection
    4. response -> result, dowell output
    """
    payload = JSONParser().parse(request)
    print("payload ", payload)
    n = int(payload["n"])
    r = int(payload["r"])

    def fact(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def nPr(n, r):
        return fact(n) / fact(n - r)

    result = nPr(n, r)
    data = {"status": 200, "n": n, "r": r, "result": result}

    # save to dowell connection

    command = "insert"
    fields = {
        "n": n,
        "r": r,
        "result": result,
        "value": "",
        "permutationResult": "",
        "event_id": get_event_id(),
    }
    output = connection(command, fields)
    resp = json.loads(output)

    respsonse = {"result": result, "output": resp}
    return Response(respsonse, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["GET", "POST"])
def calculateperm(request):
    if request.method == "POST":
        """
        1. Get the data from the request
        2. get data from dowell connection
        3. calculate the permutations
        4. Return the permutations
        """
        data = JSONParser().parse(request)
        print("data ", data)
        value = data.get("value")
        inserted_id = data.get("inserted_id")

        # get data from dowell connection
        command = "find"
        fields = {"_id": inserted_id}
        output = connection(command, fields)
        print("output ", output)
        output_json = json.loads(output)
        print(output_json)

        # calculate the permutations
        print("value ", output_json["data"]["value"])
        resp_value = output_json["data"]["value"]

        permutations = permuationsFunction(value, resp_value)

        # update value in dowell connection
        command = "update"
        fields = {"_id": inserted_id}
        update_fields = {"value": value, "permutationResult": permutations}
        output1 = connection(command, fields, update_fields)
        output_json1 = json.loads(output1)
        print(output_json1)

        return Response(
            {
                "result": data,
                "output": output_json,
                "value": value,
                "permutations": permutations,
                "output1": output_json1,
            },
            status=status.HTTP_201_CREATED,
        )
    if request.method == "GET":
        pass


@api_view(["GET", "POST"])
def save(request):
    if request.method == "POST":
        """
        1. Get the data from the request
        2. Save the permutations to the dowell connection
        3. return the saved data and status/id
        """
        data = JSONParser().parse(request)
        print("data ", data)
        data = data.get("char")
        print("data ", data)
        fields = {"event_id": get_event_id(), "data": data}
        # save to dowell connection
        command = "insert"
        output = connection(command, fields)
        print("output ", output)
        print(output)
        print(type(output))
        output_json = json.loads(output)
        print(output_json)
        print(type(output_json))

        # extract inserted_id from output
        try:
            inserted_id = output_json["inserted_id"]
        except:
            inserted_id = None

        print("inserted_id ", inserted_id)

        return Response(
            {"saved": data, "output": output_json, "inserted_id": inserted_id},
            status=status.HTTP_201_CREATED,
        )
    if request.method == "GET":
        pass
