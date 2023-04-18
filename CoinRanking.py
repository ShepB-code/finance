import requests
import json
from dotenv import dotenv_values

class CoinRank:
    def __init__(self):
        self.key = dotenv_values('.env')['ACCESS_TOKEN']

    def make_query(self, endpoint, payload) -> requests.models.Response:
        request_url = f'https://api.coinranking.com/v2/{endpoint}'
    
        headers = {
            'Content-Type': 'application/json',
            'x-access-token': self.key,
        }

        req = requests.get(url=request_url, headers=headers, params=payload)
        return req
    
    def get_coins(self, num_res=50, order_by="price"):
        endpoint = 'coins'

        payload = {
            'limit': num_res,
            'orderBy': order_by
        }

        res = self.make_query(endpoint, payload)
        
        
        return [item for item in res.json()['data']['coins']]



if __name__ == "__main__":
    cr = CoinRank()

    # get the coin with the highest change
    coins = cr.get_coins(100, 'change')
    print(coins[0])

