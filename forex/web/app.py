from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from forex_python.converter import CurrencyRates
import bcrypt
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

#docker Client:
#Version:           18.06.1-ce
#API version:       1.38


client = MongoClient("mongodb://db:27017")# Mongo version 3.6.7
db = client.aNewDB
users = db["Users"]
UserNum = db["UserNum"]



UserNum.insert_one({
    'num_of_users':1
})

# Simple counter for route /visitors |||| git practising for git bettering ||||
class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user " + str(new_num))


def UserExist(username):
    #### Previous Version: if db.users.find({"username":username}).count() == 0:
    if users.count_documents({"username":username}) == 0:
        return False
    else:
        return True


def generateReturnDictionary(status, msg):
    rbMap = {
        "status": status,
        "msg": msg
    }
    return rbMap

# Register a user
class Register(Resource):
    def post(self):
        #get data from user
        postedData = request.get_json()
        #get data from user like this
        username = postedData["username"] #mits
        password = postedData["password"] #123

        if UserExist(username):

            return jsonify(generateReturnDictionary(301, "Invalid Username"))

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        #Store username and pw into the database
        users.insert_one({
            "username": username,
            "password": hashed_pw,
            "tokens":5
        })

        return jsonify(generateReturnDictionary(200, "You successfully signed up for the API"))

# pw check allready (for db.version 3.6.7)
def verifyPw(username, password):
    if not UserExist(username):
        return False

    hashed_pw = users.find({
        "username":username
    })[0]["password"]

    if bcrypt.hashpw(password.encode('utf8'), hashed_pw) == hashed_pw:
        return True
    else:
        return False

# pw check allready (for db.version 3.6.7)
def verifyCredentials(username, password):
    if not UserExist(username):
        return generateReturnDictionary(301, "Invalid Username"), True

    correct_pw = verifyPw(username, password)

    if not correct_pw:
        return generateReturnDictionary(302, "Incorrect Password"), True

    return None, False

# More tokens
class Refill(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["admin_pw"]
        amount = postedData["amount"]

        if not UserExist(username):
            return jsonify(generateReturnDictionary(301, "Invalid Username"))

        correct_pw = "abc123"
        if not password == correct_pw:
            return jsonify(generateReturnDictionary(302, "Incorrect Password"))

        users.update({
            "username": username
        },{
            "$set":{
                "tokens": amount
            }
        })
        return jsonify(generateReturnDictionary(200, "Refilled"))

# Verify validity of posted data
def DataCheck(posted, function):
    if (function == "usdtoeuro" or function == "usdtogbp"):
        if "x" not in posted:
            return 301 # Missing posteddata
        else:
            return 200 # 200 is good


class usdtoeuro(Resource):
    def post(self):

        postedData = request.get_json()

        # Verify validity of posted data
        status_code = DataCheck(postedData, "usdtoeuro")
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        # If i am here, then status_code == 200
        username = postedData["username"]
        password = postedData["password"]
        x = postedData["x"]
        x = int(x)

        # verifyCredentials
        retJson, error = verifyCredentials(username, password)
        if error:
            return jsonify(retJson)

        # Finding tokens
        tokens = users.find({
            "username":username
        })[0]["tokens"]

        # Verify token existance
        if tokens<=0:
            return jsonify(generateReturnDictionary(303, "Not Enough Tokens"))

        # Convert the posted data since tokens exist using CurrencyRates module
        c = CurrencyRates()
        rb = c.convert('USD', 'EUR', x)

        # Conversion is ready, next step   ---->   Tokens = Tokens-1
        users.update_one({"username": username}, {"$set":{"tokens":tokens-1}})# version 3.6.7 https://docs.mongodb.com/manual/reference/method/db.collection.updateOne/

        return jsonify(generateReturnDictionary(200, rb))



class usdtogbp(Resource):
    def post(self):

        postedData = request.get_json()

        # Verify validity of posted data
        status_code = DataCheck(postedData, "usdtogbp")
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        # If i am here, then status_code == 200
        username = postedData["username"]
        password = postedData["password"]
        x = postedData["x"]
        x = int(x)

        # verifyCredentials
        retJson, error = verifyCredentials(username, password)
        if error:
            return jsonify(retJson)

        # Finding tokens
        tokens = users.find({
            "username":username
        })[0]["tokens"]

        # Verify token existance
        if tokens<=0:
            return jsonify(generateReturnDictionary(303, "Not Enough Tokens"))

        # Convert the posted data since tokens exist using CurrencyRates module
        c = CurrencyRates()
        rb = c.convert('USD', 'GBP', x)
        # Conversion is ready, next step   ---->   Tokens = Tokens-1
        users.update_one({"username": username}, {"$set":{"tokens":tokens-1}})
        return jsonify(generateReturnDictionary(200, rb))


api.add_resource(Register, '/register')
api.add_resource(usdtoeuro, "/usdtoeuro")
api.add_resource(usdtogbp, "/usdtogbp")
api.add_resource(Visit, "/visitors")
api.add_resource(Refill, '/refill')


@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="__main__":
    app.run(host='0.0.0.0')
