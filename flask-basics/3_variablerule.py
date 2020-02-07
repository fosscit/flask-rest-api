from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello ' + name + '!'

@app.route('/idShow/<int:id>')
def id_show(id):
   return 'Your id is: %d ' % id

@app.route('/percent/<float:perc>')
def percent_show(perc):
   return 'Your percentage is %.2f' % perc


if __name__ == '__main__':
   app.run(debug = True)