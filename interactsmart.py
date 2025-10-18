from web3 import Web3
import json

# Connect to Ethereum network
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check if connected
if not web3.is_connected():
    raise Exception("Failed to connect to Ethereum network")

# Load contract ABI and address
contract_address = '0xYourContractAddress'
with open('TrancheManagerABI.json') as f:
    contract_abi = json.load(f)

tranche_manager = web3.eth.contract(address=contract_address, abi=contract_abi)

def create_tranche(tranche_id, risk_level):
    try:
        tx_hash = tranche_manager.functions.createTranche(tranche_id, risk_level).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Tranche {tranche_id} created successfully.")
    except Exception as e:
        print(f"Error creating tranche: {e}")

def deposit_to_tranche(tranche_id, amount):
    try:
        tx_hash = tranche_manager.functions.deposit(tranche_id, amount).transact()
        web3.eth.waitForTransactionReceipt(tx_hash)
        print(f"Deposited {amount} to tranche {tranche_id}.")
    except Exception as e:
        print(f"Error depositing to tranche: {e}")

# Example usage
create_tranche(1, 5)
deposit_to_tranche(1, 1000)

