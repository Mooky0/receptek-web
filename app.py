from flask import Flask, render_template, request, redirect, url_for

import dbhandler

app = Flask(__name__)

@app.route('/index/')
def index():
   tomb = dbhandler.init_lista()
   lentomb=len(tomb)
   return render_template('index.html', tomb=tomb, lentomb=lentomb)

@app.route('/kereso/', methods=['POST', 'GET'])
def index_post():
   if request.method == "POST":
      keres = request.form['kereso']
      print(keres)
      return redirect(url_for('kereses', keres = keres))
   else:
      pass

@app.route('/kereses/<keres>')
def kereses(keres):
   tomb = dbhandler.init_lista()
   lentomb=len(tomb)
   keresett = dbhandler.kereso(keres)
   return render_template('index.html', tomb=tomb, lentomb=lentomb, tartalom = keresett)
   ## return 'A keresett érték: %s' % keres

if __name__ == '__main__':
   app.run()

