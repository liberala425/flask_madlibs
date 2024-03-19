from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/homepage')
def show_form():
    return render_template("form.html")

@app.route('/story')
def Madlibs():
    pl = request.args['place']
    n = request.args['noun']
    v = request.args['verb']
    adj = request.args['adjective']
    plural = request.args['plural_noun']

    return render_template("story.html", 
                           place=pl,
                           noun=n,
                           verb=v,
                           adjective=adj,
                           plural_noun=plural)
