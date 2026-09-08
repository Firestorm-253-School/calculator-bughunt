import os

from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS

from .calculator import OPERATIONS, CalculationError
from .service import CalculatorService

api = Blueprint("api", __name__, url_prefix="/api")


def _service() -> CalculatorService:
    from flask import current_app

    return current_app.config["CALCULATOR_SERVICE"]


@api.get("/health")
def health():
    return jsonify(status="ok", environment=os.getenv("APP_ENV", "development"))


@api.get("/operations")
def operations():
    return jsonify(operations=sorted(OPERATIONS.keys()))


@api.post("/calculate")
def calculate_endpoint():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify(error="Request-Body muss ein JSON-Objekt sein"), 400

    operation = payload.get("operation")
    if not isinstance(operation, str):
        return jsonify(error="Feld 'operation' fehlt oder ist kein Text"), 400

    try:
        a = float(payload["a"])
        b = float(payload["b"])
    except (KeyError, TypeError, ValueError):
        return jsonify(error="Felder 'a' und 'b' muessen Zahlen sein"), 400

    try:
        result = _service().perform(operation, a, b)
    except CalculationError as exc:
        return jsonify(error=str(exc)), 400

    return jsonify(operation=operation, a=a, b=b, result=result)


def create_app(service: CalculatorService | None = None) -> Flask:
    app = Flask(__name__)
    app.config["CALCULATOR_SERVICE"] = service or CalculatorService()

    allowed = os.getenv("ALLOWED_ORIGINS", "*")
    CORS(app, resources={r"/api/*": {"origins": allowed.split(",")}})

    app.register_blueprint(api)

    @app.errorhandler(404)
    def not_found(_):
        return jsonify(error="Endpunkt nicht gefunden"), 404

    @app.errorhandler(405)
    def not_allowed(_):
        return jsonify(error="Methode nicht erlaubt"), 405

    return app
