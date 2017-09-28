from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/print_username')
def testGetStringQuery():
    if 'username' in request.args:
        username = request.args.get('username')
        print "This is user's input : %s" % username
        return "Hello, %s" % username
    else:
        return "No username argument found."

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)