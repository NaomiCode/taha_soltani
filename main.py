from web3 import Web3
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3, EthereumTesterProvider
from web3.middleware import construct_sign_and_send_raw_middleware


url_defult = "https://mainnet.infura.io/v3/8cb9d441420b4009afa02ce71849560e"
w3 = Web3(Web3.WebsocketProvider(url_defult))

# lastest block
block_number = w3.eth.block_number
print(block_number)

addess_defult = "0x89e51fA8CA5D66cd220bAed62ED01e8951aa7c40"
addess_defult = Web3.to_checksum_address(addess_defult)
balance_wei = w3.eth.get_balance(addess_defult)
print(balance_wei)
balance_eth = Web3.from_wei(balance_wei,'ether')

print(F"{balance_eth}")



pv_key = "ff01718ab77f53f7f3108f5436918448425c412f497cefacb8167869a201ddc1"
account_finance = Account.from_key(pv_key)


pv_key2 = "ff09878ab77f53f7f3108f5436918448425c412f497cefacb8167869a201ddc1"
account_finance2 = Account.from_key(pv_key2)

transaction = {
    'from': account_finance.address,
    'to': account_finance2.address,
    'value': 1000000000,
    'nonce': w3.eth.get_transaction_count(account_finance.address),
    'gas': 200000,
    'maxFeePerGas': 2000000000,
    'maxPriorityFeePerGas': 1000000000,
}

signed_tx = w3.eth.account.sign_transaction(transaction,account_finance.key)
print(signed_tx)


tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
time.sleep("wait till transaction mines")
w3.eth.wait_for_transaction_receipt(tx_hash)
