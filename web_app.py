import os
from flask import Flask
from db_connector import get_user
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    try:
        data = get_user(user_id)
        user_name = data[0][1]
        if user_name:
            return (f"""
                    <html>
                    <body>
                        <h1 id='user'>{user_name}</h1>
                    </body>
                    </html>
                    """)
        else:
            return (f"""
                    <html>
                    <body>
                        <h1 id='error'>No such user: {user_id}</h1>
                    </body>
                    </html>
                    """)
    except IndexError:
        return (f"""
                <html>
                <body>
                    <h1 id='error'>No such user: {user_id}</h1>
                </body>
                </html>
                """)


if __name__ == '__main__':
    app.run(host=os.getenv("HOST"), port=os.getenv("WEB_PORT"), debug=True)
