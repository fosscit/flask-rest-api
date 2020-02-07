from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)

# READ JSON FILE
def readData():
    with open('data.json') as fp:
        d = json.load(fp)
    return d

# WRITE JSON FILE
def writeData(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)



# LIST ALL USERS
@app.route('/list', methods=['GET'])
def list():
    data = readData()
    return jsonify(data)




# SHOWING, ADDING, DELETING PARTICULAR DATA
@app.route('/usr/<name>', methods=['GET', 'PUT', 'DELETE'])
def getDetails(name):
    data = readData()

    # GET PARTICULAR DATA
    if request.method == 'GET':
        record = data[name]
        return jsonify(record)

    # ADD DATA
    elif request.method == 'PUT':
        newData = {
            "name":name,
            "role":request.json["role"]
        }
        data[name] = newData
        writeData(data)
        return jsonify({"msg":"Data added successfully"})

    # DELETE DATA
    elif request.method == 'DELETE':
        try:
            del data[name]
            writeData(data)
            return jsonify({"msg":"Data deleted successfully"})
        except:
            abort(404)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)