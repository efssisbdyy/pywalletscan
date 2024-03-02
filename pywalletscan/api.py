import json
import requests
import time
import web3
import sys

# 5calls/sec: Etherscan limit for free account
DEFAULT_WAIT_SEC=0.2
url_base = "https://api.etherscan.io/api"

def get_abi(address, api_key):
    payload = {
        "module":"contract",
        "action":"getabi",
        "address": {address},
        "apikey": {api_key}
    }
    res = requests.get(url_base, params=payload)
    time.sleep(DEFAULT_WAIT_SEC)
    return json.loads(res.json()["result"])

def get_contract(address):
    abi = get_abi(address)
    contract = web3.eth.contract(address=web3.to_checksum_address(address), abi=abi)
    return contract

def decode_input(address, data):
    contract = get_contract(address)
    fn, value = contract.decode_function_input(data)
    return fn, value

def get_transaction(address="", api_key=""):
    payload = {
        "module":"account",
        "action":"txlist",
        "address": f"{address.lower()}",
        "startblock": 0,
        "endblock": sys.maxsize,
        "sort": "asc",
        "apikey": {api_key}
    }
    res = requests.get(url_base, params=payload)
    return res.json()["result"]
