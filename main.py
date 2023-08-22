from flask import Flask, request
from flask_restful import Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app)

# conn = sqlite3.connect('payments.db')
# c = conn.cursor()
# c.execute("""CREATE TABLE IF NOT EXISTS payments
#              (id INTEGER PRIMARY KEY AUTOINCREMENT,
#               date TEXT NOT NULL,
#               amount REAL NOT NULL)""")
# conn.commit()
# conn.close()


class Payment(Resource):
    def post(self):
        data = request.get_json()
        date = data['date']
        amount = data['amount']

        conn = sqlite3.connect('payments.db')
        c = conn.cursor()
        c.execute("INSERT INTO payments (date, amount) VALUES (?, ?)", (date, amount))
        conn.commit()
        conn.close()

        return {'message': 'Платеж успешно добавлен'}

    def get(self):
        date1 = request.args.get('date1')
        date2 = request.args.get('date2')

        conn = sqlite3.connect('payments.db')
        c = conn.cursor()
        if date2:
            c.execute("SELECT * FROM payments WHERE date BETWEEN ? AND ?", (date1, date2))
        else:
            c.execute("SELECT * FROM payments WHERE date = ?", (date1,))
        rows = c.fetchall()
        conn.close()

        payments = []
        for row in rows:
            payment = {'id': row[0], 'date': row[1], 'amount': row[2]}
            payments.append(payment)

        return {'payments': payments}

    def put(self, payment_id):
        data = request.get_json()
        date = data['date']
        amount = data['amount']

        conn = sqlite3.connect('payments.db')
        c = conn.cursor()
        c.execute("UPDATE payments SET date = ?, amount = ? WHERE id = ?", (date, amount, payment_id))
        conn.commit()
        conn.close()

        return {'message': 'Платеж успешно обновлен'}


api.add_resource(Payment, '/payments', '/payments/<int:payment_id>')

if __name__ == '__main__':
    app.run(debug=True)
