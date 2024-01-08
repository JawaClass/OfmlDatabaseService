from flask import Flask

from Service import create_app

# gunicorn -w 2 'wsgi:app'
app = create_app()

if __name__ == '__main__':
    Flask.run(app, debug=True, port=5000, host='0.0.0.0')
