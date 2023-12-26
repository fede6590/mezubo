from flask import Flask

app = Flask(__name__)

DB = {
    'roulettes': {},
    'bets': {}
}


@app.route('/TEST', methods=['GET'])
def test_roulette():
    print('TEST_ok')
    return 'TEST_OK'


@app.route('/roulette', methods=['POST'])
def create_roulette():
    print('create_ok')
    pass


@app.route('/roulette/<int:roulette_id>/open', methods=['POST'])
def open_roulette(roulette_id):
    print('open_ok')
    pass


@app.route('/roulette/<int:roulette_id>/bet', methods=['POST'])
def place_bet(roulette_id):
    print('bet_ok')
    pass


@app.route('/roulette/<int:roulette_id>/close', methods=['POST'])
def close_bets(roulette_id):
    print('close_ok')
    pass


if __name__ == '__main__':
    app.run(debug=True)
