from flask import Flask, render_template, request, redirect, url_for

import dbhandler

app = Flask(__name__)

@app.route('/index/')
def index():
   tomb = dbhandler.init_lista()
   lentomb=len(tomb)
   return render_template('index.html', tomb=tomb, lentomb=lentomb, lentartalom = 0)

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
   vegso = [(i[0], i[1], i[2].replace('\n', ' <br> '), i[3], i[4], i[5], i[6], i[7]) for i in keresett]
   #print(vegso)
   return render_template('index.html', tomb=tomb, lentomb=lentomb, tartalom = vegso, lentartalom = len(vegso), szo = keres)
   ## return 'A keresett érték: %s' % keres

@app.route('/recept/<id>')
def recept(id):
   tomb = dbhandler.init_lista()
   lentomb=len(tomb)
   kereses = dbhandler.receptById(id)
   if kereses == None:
      return render_template('404.html')
   vegso = (kereses[0], kereses[1], kereses[2].replace('\n', ' <br> '), kereses[3], kereses[4], kereses[5], kereses[6], kereses[7], kereses[8])
   return render_template('recept.html', tomb=tomb, lentomb=lentomb, tartalom = vegso)

if __name__ == '__main__':
   app.run()

