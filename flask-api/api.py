from flask import Flask, jsonify
import random

app = Flask(__name__)

DB = {
    'roulettes': {}
}

WALLET = 10000


@app.route('/DB', methods=['GET'])
def show_DB():
    return DB


@app.route('/roulette', methods=['POST'])
def create_roulette():
    roulette_id = len(DB['roulettes']) + 1
    DB['roulettes'][roulette_id] = {'status': 'closed'}
    return jsonify({'roulette_id': roulette_id})


@app.route('/roulette/<int:roulette_id>/open', methods=['PUT'])
def open_roulette(roulette_id):
    if roulette_id not in DB['roulettes']:
        return jsonify({'error': 'Roulette not found'}), 404
    if DB['roulettes'][roulette_id]['status'] == 'opened':
        return jsonify({'error': 'already opened'})
    DB['roulettes'][roulette_id]['status'] = 'opened'
    return jsonify({'status': 'success'})


@app.route('/roulette/<int:roulette_id>/<bet>-<int:amount>', methods=['POST'])
def place_bet(roulette_id, bet, amount):
    if roulette_id not in DB['roulettes'] or DB['roulettes'][roulette_id]['status'] != 'opened':
        return jsonify({'error': 'The roulette is closed'}), 400
    global WALLET
    bets = list(range(37)) + ['black', 'red']
    if bet not in bets:
        return jsonify({'error': 'Chose a number between 0 and 36, or choose a color (black or red)'})
    elif amount > 10000:
        return jsonify({'error': 'Chose an amount between 1 and 10000'})
    elif amount > WALLET:
        return jsonify({'error': 'Not enough credits'})
    else:
        bet_id = len(DB['roulettes'][roulette_id])  # +1 - 1 because of the 'status' key-value
        DB['roulettes'][roulette_id][bet_id] = {0: bet, 1: amount}
        WALLET -= amount
        return jsonify({'success': 'bet placed successfully'})


@app.route('/roulette/<int:roulette_id>/close', methods=['POST'])
def close_bets(roulette_id):
    if roulette_id not in list(DB['roulettes'].keys()):
        return jsonify({'error': 'roulette not opened'})
    if DB['roulettes'][roulette_id]['status'] != 'opened':
        return jsonify({'error': 'roulette already closed'})
    if len(DB['roulettes'][roulette_id]) == 1:
        return jsonify({'status': 'closing without any bet'})

    global WALLET
    win_num = random.randint(0, 36)
    print(win_num)
    for b in DB['roulettes'][roulette_id]:
        if b == 'status':
            continue
        bet = DB['roulettes'][roulette_id][b][0]
        amount = DB['roulettes'][roulette_id][b][1]
        if bet.isdigit():
            if int(bet) == win_num:
                pot = amount * 5
                WALLET += pot
                print(f'You won {pot} (x 5 on your bet)')
        elif bet == 'black':
            if win_num in range(1, 37, 2):
                pot = amount * 1.8
                WALLET += pot
                print(f'You won {pot} (x 1.8 on your bet)')
        elif bet == 'red':
            if win_num in range(0, 37, 2):
                pot = amount * 1.8
                WALLET += pot
                print(f'You won {pot} (x 1.8 on your bet)')
        del b
    DB['roulettes'][roulette_id]['status'] = 'closed'
    return jsonify({'status': f' you have {WALLET} left'})


if __name__ == '__main__':
    app.run(debug=True)
