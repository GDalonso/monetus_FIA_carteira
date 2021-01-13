from flask import jsonify, abort

# [START functions_get_variation]
from get_variation_pct import calculate_variation_average
from monetus_FIA_composition import MonetusFiaComposition


def get_variation(request):
    if request.method == "GET":
        return jsonify(MonetusFiaComposition.get_current_quotations())

    return abort(404)

# [END functions_get_variation]

# [START get_consolidated_variation]

def get_consolidated_variation(request):
    if request.method == "GET":

        return jsonify({"total_variation": calculate_variation_average(MonetusFiaComposition.get_current_quotations())})
    return abort(404)

# [END get_consolidated_variation]