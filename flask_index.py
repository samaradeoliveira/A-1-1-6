from flask import Flask, render_template
app = Flask(__name__)
#Na função, retorne render_template(‘index.html’)
@app.route("/index")
def first_webpage():
    #Crie uma variável
    name = 'Flask'
    #Passe a variável no modelo
    return render_template('index.html', index_variable = name)
app.run(debug=True)



