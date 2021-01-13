import requests

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


def get_variation_pct(symbol, api_key="X3T9RIKSB7XJAC26"):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&interval=5min&apikey={api_key}"
    res = requests.get(url)

    if res.json().get("Note"):
        return {symbol[:-4]: res.json().get("Global Quote", "APIKEYDEAD")}

    # Remove o .SAO
    return {
        symbol[:-4]: res.json()
        .get("Global Quote", "NotFound")
        .get("10. change percent", "NotFound")
    }


def get_current_variations(enum):
    current_values = {}
    keys = API_KEYS
    for paper in enum:
        api_key, keys = solve_api_key(keys)
        current_values.update(get_variation_pct(f"{paper.name}.SAO", api_key))
    return current_values


def calculate_variation_average(all_variations):
    """

    :param all_variations: Dict {paper:variation}
    :return:
    """
    f = 0.0
    from monetus_FIA_composition import MonetusFiaComposition

    for paper_pct in MonetusFiaComposition:
        f = f + (
            paper_pct.value
            * parse_response_pct_to_float(all_variations.get(paper_pct.name, 0))
        )
    return f / 100


def parse_response_pct_to_float(response_pct):
    if not response_pct in ["APIKEYDEAD", "NotFound"]:
        return float(response_pct[:-1])
    return 0
