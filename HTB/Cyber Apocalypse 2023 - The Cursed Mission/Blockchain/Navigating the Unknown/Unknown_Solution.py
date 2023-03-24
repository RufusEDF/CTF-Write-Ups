#Additional resources:
#https://book.getfoundry.sh/
#https://web3py.readthedocs.io/en/stable/quickstart.html#quickstart
#https://remix-ide.readthedocs.io/en/latest/running_js_scripts.html#compile-a-contract-and-run-a-script-on-the-fly


#Install required libraries from pip
#└─$ pip install web3
#Run the solution in interactive mode.  This allows easy troubleshooting.
#└─$ python3 -i ./Unknown_Solution.py

#import required libraries
from web3 import Web3, AsyncWeb3

#Blocks on Etherium based block chains have a concept of Smart Contracts.  Smart Contract blocks contain compiled code, written in a language such as Solidity.

# └─$ cat README.md
#We connect to the block chain and get the latest block to confirm we are connected.
w3 = Web3(Web3.HTTPProvider('http://165.232.108.36:32663/'))
print(w3)
#<web3.main.Web3 object at 0x7f7990e5e560>
print(w3.eth.get_block('latest'))

# └─$ cat README.md
# └─$ nc 165.232.98.21 31359
#1 - Connection information
#2 - Restart Instance
#3 - Get flag
#action? 1
#Private key : 0x8f6ec09cb914e70eb63a39864b6cfe2f3706b001fbd3b859a46c90e088c3fdff
#Address : 0xEaa0632Bd9fd67053F28B7Bb70A67a86a3207C1b
#Target contract : 0x5a35e1dbc92538eF62E6e99c893ffd954973e0a2
#Setup contract : 0x88620b8dc9e938d2741467BD6ba7efe300e9d44E

private_key = "0x8f6ec09cb914e70eb63a39864b6cfe2f3706b001fbd3b859a46c90e088c3fdff"
wallet_address = "0xEaa0632Bd9fd67053F28B7Bb70A67a86a3207C1b"
target_address = "0x5a35e1dbc92538eF62E6e99c893ffd954973e0a2"
setup_address = "0x88620b8dc9e938d2741467BD6ba7efe300e9d44E"

#Generate abi's by compiling .sol files --> https://remix.ethereum.org/#lang=en
target_abi = [{'inputs': [{'internalType': 'uint256', 'name': 'version', 'type': 'uint256'}], 'name': 'updateSensors', 'outputs': [], 'stateMutability': 'nonpayable', 'type': 'function'}, {'inputs': [], 'name': 'updated', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}]

setup_abi = [{'inputs': [], 'stateMutability': 'nonpayable', 'type': 'constructor'}, {'inputs': [], 'name': 'TARGET', 'outputs': [{'internalType': 'contract Unknown', 'name': '', 'type': 'address'}], 'stateMutability': 'view', 'type': 'function'}, {'inputs': [], 'name': 'isSolved', 'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}], 'stateMutability': 'view', 'type': 'function'}]

target_contract_instance = w3.eth.contract(address = target_address, abi = target_abi)
setup_contract_instance = w3.eth.contract(address = setup_address, abi = setup_abi)

#The above is common to all blockchain challenges.  Below is specific to this challenge.

# └─$ cat Setup.sol
#    function isSolved() public view returns (bool) {
#        return TARGET.updated();   }

# └─$ cat Unknown.sol
#    bool public updated;
#
#    function updateSensors(uint256 version) external {
#        if (version == 10) {
#            updated = true;        }

#https://ethereum.stackexchange.com/questions/765/what-is-the-difference-between-a-transaction-and-a-call
#target_contract_instance.functions.updateSensors(10).call()   <-- This would run the function in a read-only mode.  We need to transact() for the function to run in a write mode, publishing changes to the blockchain.
target_contract_instance.functions.updateSensors(10).transact()
#HexBytes('0x5d0f7a31ee8c3b403d1079a55cff94b46141ec99a00fddf939f52761e4406ae3')

setup_contract_instance.functions.updated().call()
#True

# └─$ nc 165.232.98.21 31359
#1 - Connection information
#2 - Restart Instance
#3 - Get flag
#action? 3
#HTB{Flag!}