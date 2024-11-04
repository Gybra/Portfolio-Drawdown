from flask import Flask, request
from inc.drawdown import calculate_max_drawdown

app = Flask(__name__)

@app.route('/')
def home():
    tickers = request.args.get('tickers').split('|')
    dict = {pair.split(':')[0]: pair.split(':')[1] for pair in tickers}
    return calculate_max_drawdown(dict)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3031)