from asyncio import tasks
import json, requests, asyncio
import requests_async as asyncRequests

class GetData():


    def get_data(url):
        """
            Method: GET  Path: /  Duration: 14.112628112999971  Status: 200
            10129 function calls (9949 primitive calls) in 14.112 seconds

        """
        response = requests.get(url)
        
        return response.json()

    def get_data_async(url, session):
        """
        api za berze: za 14 sekundi je normalno za get metodu bez async

        1. prvi test koristi async with iz pypi doc

            Method: GET  Path: /async  Duration: 26.165393703000063  Status: 200
            137961 function calls (137635 primitive calls) in 26.164 seconds

        2. drugi test bez async with - daje bolje preformanse jer se stalno otvara i zatvara sessia sa with blokom

            Method: GET  Path: /async  Duration: 16.120499150000114  Status: 200
            132422 function calls (132041 primitive calls) in 16.122 seconds

        3. treci test znatno bolji u preformansama jer smo dodali:
            asyncio.create_task - kreira loop i daje prijoritet tasku (uradi ovaj zadatak sto je bre moguce i vrati rezultat)

            Method: GET  Path: /async  Duration: 1.830500751999807  Status: 200
            107699 function calls (107373 primitive calls) in 1.830 seconds
        """
        tasks = []
        # for i in range(10):
        tasks.append(asyncio.create_task(session.get(url)))
        return tasks