class ERC20SDK:
    def __init__(self, base_url, network):
        self.base_url = base_url
        self.network = network

    def deploy_token(self, name, symbol, alias, initial_supply, gas_limit):
        url = f"{self.base_url}/erc/v1/erc20/deploy"
        payload = {
            "name": name,
            "symbol": symbol,
            "alias": alias,
            "initialSupply": initial_supply,
            "network": self.network,
            "gasLimit": gas_limit
        }
        response = requests.post(url, json=payload)
        return response.json()

    def transfer(self, contract_address, recipient, amount, gas_limit):
        url = f"{self.base_url}/erc/v1/erc20/transfer"
        payload = {
            "contractAddress": contract_address,
            "recipient": recipient,
            "network": self.network,
            "amount": amount,
            "gasLimit": gas_limit
        }
        response = requests.post(url, json=payload)
        return response.json()

    def get_token_name(self, contract_address):
        url = f"{self.base_url}/erc/v1/erc20/name"
        payload = {
            "contractAddress": contract_address,
            "network": self.network
        }
        response = requests.get(url, json=payload)
        return response.json()

    def get_token_symbol(self, contract_address):
        url = f"{self.base_url}/erc/v1/erc20/symbol"
        payload = {
            "contractAddress": contract_address,
            "network": self.network
        }
        response = requests.get(url, json=payload)
        return response.json()
