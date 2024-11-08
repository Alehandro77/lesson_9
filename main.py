from flask import Flask, render_template
import random

app = Flask(__name__)

facts_list = ['Социальные сети имеют как позитивные, так и негативные стороны, и мы должны быть более осознанными в использовании этих платформ.'
         ,'Илон Маск утверждает, что социальные сети созданы для того, чтобы удерживать нас внутри платформы, чтобы мы тратили как можно больше времени на просмотр контента.']

mone = ['Орёл', 'Решко']


@app.route("/")
def hello():
    return render_template('base.html')


@app.route("/random_fact")
def fackt():
    return f'<p>{random.choice(facts_list)}</p>'
    

@app.route("/mone")
def dengi():
    return f'<p>{random.choice(mone)}</p>'


app.run(debug=True)
