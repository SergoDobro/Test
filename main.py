import sqlite3
from fastapi import FastAPI, Body
from fastapi.responses import PlainTextResponse
import uvicorn

app = FastAPI()
con = sqlite3.connect('db.splite')


@app.on_event('startup')
def create_db():
    cursor = con.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        );
    ''')
    con.commit()
    cursor.execute('''
        INSERT INTO users (username, password) VALUES (?, ?);
    ''', ('admin', 'admin'))
    con.commit()
    cursor.close()


@app.get('/')
def index():
    return PlainTextResponse('Hi ;)')


@app.post('/login')
def login(username: str = Body(...), password: str = Body(...)):
    con = sqlite3.connect('db.splite')
    cursor = con.cursor()
    cursor.execute('''
        SELECT id FROM users WHERE username = ? AND password = ?
    ''', (username, password))
    user = cursor.fetchone()

    if user:
        return PlainTextResponse('Ok ;)')
    else:
        return PlainTextResponse('Error with login or password')


if __name__ == '__main__':
    uvicorn.run(app)
