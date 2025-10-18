import requests

def get_market_price(token):
    try:
        response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={token}&vs_currencies=usd')
        response.raise_for_status()
        return response.json()[token]['usd']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching market price: {e}")
        return None

def rebalance_tranche(tranche_id, target_allocation):
    current_price = get_market_price('ethereum')
    if current_price is None:
        return

    # Logic to determine if rebalancing is needed
    # This is a placeholder for actual rebalancing logic
    print(f"Current price of Ethereum: {current_price}. Target allocation: {target_allocation}.")

# Example usage
rebalance_tranche(1, 50)

