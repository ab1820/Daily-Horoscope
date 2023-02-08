import requests

baseUrl = "http://sandipbgt.com/theastrologer/api"

def getSigns():
  return requests.get("http://sandipbgt.com/theastrologer/api/sunsigns").json()

def getHoroscope(sign, timeFrame):
  return requests.get(f"http://sandipbgt.com/theastrologer/api/horoscope/{sign}/{timeFrame}")