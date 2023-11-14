from flask import Flask

from Service import create_app

app = create_app()
Flask.run(app, debug=True, port=5000)