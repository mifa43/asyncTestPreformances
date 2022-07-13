from asyncio import gather
import asyncio
from urllib import response
from req import GetData 
from fastapi_cprofile.profiler import CProfileMiddleware
from fastapi import FastAPI
import logging
import requests_async as asyncRequests
import asyncio
import json, requests

logger = logging.getLogger(__name__) 
logger.setLevel("DEBUG")

# kreiranje logger consol
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# format
formatter = logging.Formatter('%(levelname)s:     %(name)s.%(funcName)s: %(message)s')

# dodaj format u consol-u
ch.setFormatter(formatter)

# dodaj consol-u logger
logger.addHandler(ch)


app = FastAPI()
app.add_middleware(CProfileMiddleware, enable=True, server_app = app, filename='/tmp/output.pstats', strip_dirs = True, sort_by='cumulative', print_each_request = True)


@app.get("/normal")
def normalDef():
    url = ("https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=be061200b9c30793c89b0573852de35b")

    for urls in range(10):

        GetData.get_data(url)


    logger.info("{200: ok}")
   
    return {"Health": "OK"}

@app.get("/async")
async def asyncDefTest():
    url = ("https://financialmodelingprep.com/api/v3/financial-statement-symbol-lists?apikey=be061200b9c30793c89b0573852de35b")
    glob = []
    # for urls in range(10):
    #     glob.append(url)
        
    # s = await GetData.get_data_async(glob)
    async with asyncRequests.Session() as session:
        job = GetData.get_data_async(url, session)
        response = await asyncio.gather(*job)
        # for resp in response:
        # response[0].json()



    logger.info(response[0].json())
   
    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, loop="asyncio")