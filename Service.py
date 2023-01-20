import requests


def getRequest(url):
    return requests.get(url)


def getFact(number):
    url = f"http://numbersapi.com/{number}"
    response = getRequest(url)
    return response


def getRandomFact():
    url = f"http://numbersapi.com/random"
    response = getRequest(url)
    return response



