sdk = ERC20SDK(base_url='https://api.ejemplo.com', network=43113)

# Desplegar un token
response = sdk.deploy_token("MyToken", "MTK", "My first token", 1000000, 6000000)
print(response)

# Transferir tokens
transfer_response = sdk.transfer("0xContractAddress", "0xRecipientAddress", 100, 6000000)
print(transfer_response)

# Obtener nombre del token
name_response = sdk.get_token_name("0xContractAddress")
print(name_response)

# Obtener símbolo del token
symbol_response = sdk.get_token_symbol("0xContractAddress")
print(symbol_response)
