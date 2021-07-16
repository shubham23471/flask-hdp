from flask import Blueprint, jsonify

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(500)
def hand_error(error):
    status_code = 500
    success = False
    print(error.args)
    message = [str(x) for x in error.args]

    response = {
        "success": success,
        "error": {"type": error.__class__.__name__, "message": message},
    }


@errors.app_errorhandler(404)
def hand_error(error):
    status_code = 404
    success = False
    print(error.args)
    message = ["Requested URL unavaiable."]

    response = {
        "success": success,
        "error": {"type": error.__class__.__name__, "message": message},
    }


@errors.app_errorhandler(Exception)
def handle_unexpected_error(error):
    "To handle Exception in the app"
    status_code = 500
    success = False
    response = {
        "success": success,
        "error": {
            "type": "UnexpectedExceptionFromApp",
            "message": "An unexcepted error has occurred",
        },
    }
    return jsonify(response), status_code
