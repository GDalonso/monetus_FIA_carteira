from flask import jsonify, abort

# [START functions_get_variation]
from monetus_FIA_composition import MonetusFiaComposition


def get_variation(request):
    if request.method == "GET":
        return jsonify(MonetusFiaComposition.get_current_quotations())

    return abort(404)


# [END functions_get_variation]
