import requests
from time import sleep as time_sleep

# Consegue processar 20 requests por minuto
# 5 requests por minuto/ 500 por dia por chave
API_KEYS = {
    "PG7BNACI60Q16CDU": 0,
    "WVNT1ONIXJY05PZS": 0,
    "ELGP8AP0BURDB785": 0,
    "X3T9RIKSB7XJAC26": 0,
}


def solve_api_key(keys):
    def filterTheDict(dictObj, callback):
        newDict = dict()
        # Iterate over all the items in dictionary
        for (key, value) in dictObj.items():
            # Check if item satisfies the given condition then add to new dict
            if callback((key, value)):
                newDict[key] = value
        return newDict

    usable_keys = filterTheDict(keys, lambda elem: elem[1] <= 5)
    for key in usable_keys:
        keys.update({key: keys.get(key) + 1})
        return key, keys

    # Se não tiver usable keys, retorna qlqr uma
    for key in keys:
        keys.update({key: keys.get(key) + 1})
        return key, keys


def get_quote_symbol(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&interval=5min&apikey={api_key}"
    res = requests.get(url)

    # Limite de 5 requests por minuto
    if res.json().get("Note"):
        time_sleep(60)
        return get_quote_symbol(symbol, api_key)

    # Remove o .SAO
    return {
        symbol[:-4]: res.json()
        .get("Global Quote", "NotFound")
        .get("05. price", "NotFound")
    }


def get_current_quotations(enum):
    current_values = {}
    keys = API_KEYS
    for paper in enum:
        api_key, keys = solve_api_key(keys)
        current_values.update(get_quote_symbol(f"{paper.name}.SAO", api_key))
    return current_values
