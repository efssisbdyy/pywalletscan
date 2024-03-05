# pywalletscan

A Python Wrapper Implementation of Etherscan

# Prerequisite

Pywalletscan uses Etherescan API as a datasource. API key is required to run. Please refer to [Getting an API Key](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics) on Etherscan Web page.

# Getting Started

```ipython
>>> import pywalletscan as scan
>>> from pprint import pprint
>>> res = scan.get_transaction(network="sepolia", address=f"{YOUR_WALLET_ADDRESS}", api_key=f"{YOUR_API_KEY}")
>>> pprint(res)
[{'blockHash': '0x8ed677f6e5c21dfc528f76124d739591bf1087dc7e5a4f0e212c7cba1d654396',
  'blockNumber': '5419226',
  'confirmations': '13',
  'contractAddress': '',
  'cumulativeGasUsed': '153392',
  'from': '0x7ed746476a7f6520babd24eee1fdbcd0f7fb271f',
  'functionName': '',
  'gas': '84000',
  'gasPrice': '3982623228',
  'gasUsed': '21000',
  'hash': '0x9e86110e2e78382e844487d1442175d9f081c9de0b567d2fc8ace04dac889108',
  'input': '0x',
  'isError': '0',
  'methodId': '0x',
  'nonce': '819302',
  'timeStamp': '1709612220',
  'to': '0xede522b5cb39606b4f46d85cd9ea786371fc5401',
  'transactionIndex': '4',
  'txreceipt_status': '1',
  'value': '500000000000000000'}]
>>>
```

# Recognized network

goerli, sepolia, eth(etherium) (Case insensitive)

# Build

```sh
python setup.py sdist bdist_wheel

# Test
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

twine upload dist/*
```
