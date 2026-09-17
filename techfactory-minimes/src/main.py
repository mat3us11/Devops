from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>TechFactory MiniMES</h1>
    <p>Sistema de Gestão da Produção</p>
    <p>Versão 0.1.0</p>
    """


if __name__ == "__main__":
    app.run(debug=True)