import requests

class internet:
    def __init__(self):
        url="https://www.google.com/"
        """if requests.get(url):
            print("Internet connection is ON!")
        else:
            print("Error! There is no internet connection.")"""
        try:
            requests.get(url,timeout=5)
            print("Internet connection is ON!")
        except Exception as e:
            print(e)


int=internet()