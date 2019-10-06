from flask import Flask
from my_app.views import conta_bp

app = Flask(__name__)
app.register_blueprint(conta_bp)

if __name__ == '__main__':
    app.run()