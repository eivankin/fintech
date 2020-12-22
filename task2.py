from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://0.0.0.0:8545'))
accounts = set()
for n in range(w3.eth.blockNumber + 1):
    for transaction in w3.eth.getBlock(n, True)['transactions']:
        for account in (transaction['from'], transaction['to']):
            if account not in accounts and w3.eth.getBalance(account) != 0:
                accounts.add(account)
print(len(accounts))
print(accounts)
