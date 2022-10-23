# app.py
import sqlite3

from flask import Flask, render_template  # import flask

app = Flask(__name__)  # create an app instance


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("DROP TABLE IF EXISTS challenges")
    conn.execute(
        """
            CREATE TABLE challenges (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            link TEXT NOT NULL
            );
        """
    )

    conn.execute(
        "INSERT INTO challenges (title, content, link) VALUES (?, ?, ?)",
                ('First challenges', 'Content for the first post', "ozon.ru"),
    )

    conn.execute("INSERT INTO challenges (title, content, link) VALUES (?, ?, ?)",
                ('Second Post', 'Content for the second post', "ya.com")
    )

    conn.execute("INSERT INTO challenges (title, content, link) VALUES (?, ?, ?)",
                 ('Third Post', 'contest', "yandex.com")
                 )

    conn.commit()
    conn.close()


@app.route("/")  # at the end point /
def hello():  # call method hello
    conn = get_db_connection()
    challenges = conn.execute('SELECT * FROM challenges').fetchall()
    conn.close()
    return render_template("index.html", challenges=challenges)


@app.route("/<challenge_id>")  # at the end point /
def detail(challenge_id):  # call method hello
    conn = get_db_connection()
    challenge = conn.execute('SELECT * FROM challenges WHERE id = {}'.format(challenge_id)).fetchone()
    conn.close()
    return render_template("detail.html", challenge=challenge)


if __name__ == "__main__":  # on running python app.py
    init_db()
    app.run(debug=True)  # run the flask app
