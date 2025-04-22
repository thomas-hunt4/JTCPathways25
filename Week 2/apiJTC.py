# ***********************Class Notes******************************

# *****protocols****
# SOAP, GraphQL, RPC, WebSocket, REST


# *******************************Mock request to an api
# JSON placeholder


# SDK software development kit   


# import requests


# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.json())


# headers = {'Content-type': 'application/json; charset=UTF-8'}
# body = {
#     'title': 'Yo'
# }

# name this file server.py***********************************************************************
# pip3 install flask
# pip3 install stripe
# pip3 install flask_cors
# pip3 install dotenv

from flask import Flask, jsonify
import stripe
from flask_cors import CORS
from dotenv import load_dotenv



load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*":{"origins":
["http://localhost:3000", "http://127.0.0.1:3000"]}})

stripe.api_key = os.getenv("Stripe_Secret_Key")

@app.route{"/products", methods=["GET"]}



if __name__ == "__main__":
    app.run(debug=True, port=8000)



