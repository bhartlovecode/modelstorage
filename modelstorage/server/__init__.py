from modelstorage.server.app import create_app

def _run_server():
    app = create_app()

    app.run(debug=True, port=8000)