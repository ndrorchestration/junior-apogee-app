from __future__ import annotations

from flask import Flask, jsonify, request, abort

from .config_loader import load_full_config
from .logging_config import configure_logging
from .settings import Settings
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST, Counter


# simple prometheus counter example
REQUEST_COUNTER = Counter("ja_requests_total", "Total HTTP requests received")


def create_app() -> Flask:
    """Construct and return a Flask application for the dashboard."""
    configure_logging()
    app = Flask(__name__)

    @app.before_request
    def before():
        REQUEST_COUNTER.inc()
        # token authentication
        settings = Settings()
        token = settings.api_key
        if token and request.headers.get("Authorization") != f"Bearer {token}":
            abort(401)

    @app.route("/health")
    def health() -> Any:  # type: ignore[return-value]
        return jsonify(status="ok")

    @app.route("/metrics")
    def metrics() -> Any:  # type: ignore[return-value]
        # reload config each call for hot-reload
        config = load_full_config()
        return jsonify(metrics=config.metrics.dict() if config.metrics else {})

    @app.route("/openapi.json")
    def openapi() -> Any:  # type: ignore[return-value]
        # simple manual schema
        schema = {
            "openapi": "3.0.0",
            "info": {"title": "Junior Apogee API", "version": "0.1.0"},
            "paths": {
                "/health": {"get": {"responses": {"200": {"description": "OK"}}}},
                "/metrics": {"get": {"responses": {"200": {"description": "Metrics"}}}},
            },
        }
        return jsonify(schema)

    @app.route("/prometheus")
    def prometheus_metrics():
        return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}

    return app
