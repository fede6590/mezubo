from flask import Flask, jsonify

app = Flask(__name__)

DB = {
    'roulettes': {},
    'bets': {}
}


@app.route('/TEST', methods=['GET'])
def test_roulette():
    return 'TEST_OK'

@app.route('/DB', methods=['GET'])
def show_DB():
    return DB


@app.route('/roulette', methods=['POST'])
def create_roulette():
    roulette_id = len(DB['roulettes']) + 1
    DB['roulettes'][roulette_id] = {'status': 'closed'}
    return jsonify({'id': roulette_id})


@app.route('/roulette/<int:roulette_id>/open', methods=['POST'])
def open_roulette(roulette_id):
    if roulette_id not in DB['roulettes']:
        return jsonify({'error': 'Roulette not found'}), 404
    DB['roulettes'][roulette_id] = {'status': 'open'}
    return f'Roulette {roulette_id} is now open'


@app.route('/roulette/<int:roulette_id>/bet', methods=['POST'])
def place_bet(roulette_id):
    return 'bet_ok'


@app.route('/roulette/<int:roulette_id>/close', methods=['POST'])
def close_bets(roulette_id):
    return 'close_ok'


if __name__ == '__main__':
    app.run(debug=True)
