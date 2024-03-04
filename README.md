# pywalletscan

A Python Wrapper Implementation of Etherscan

# Prerequisite

Pywalletscan uses Etherescan API as a datasource. API key is required to run. Please refer to [Getting an API Key](https://docs.etherscan.io/getting-started/viewing-api-usage-statistics) on Etherscan Web page.

# Getting Started

```ipython
>> import pywalletscan as scan
>> scan.get_transaction(network="eth", address=f"{YOUR_WALLET_ADDRESS}", api_key=f"{YOUR_API_KEY}")
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
