from flask import Flask, render_template, request, redirect, url_for
import ast

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
      
   vegso = {}
   vegso["adatok"] = [(kereses["adatok"][0][0], kereses["adatok"][0][1], kereses["adatok"][0][2].replace('\n', ' <br> '), kereses["adatok"][0][2], kereses["adatok"][0][3], kereses["adatok"][0][4], kereses["adatok"][0][5], kereses["adatok"][0][6])]
   vegso["len_adatok"] = kereses["len_adatok"]
   vegso["osszetevok"] = kereses["osszetevok"]
   vegso["len_osszetevok"] = kereses["len_osszetevok"]
   vegso["alkalom"] = kereses["alkalom"]
   vegso["len_alkalom"] = kereses["len_alkalom"]
   vegso["tartalom"] = kereses["tartalom"]
   vegso["len_tartalom"] = kereses["len_tartalom"]
   return render_template('recept.html', tomb=tomb, lentomb=lentomb, tartalom = vegso)


@app.route('/tag/<tags>/<tag>/<add>')
def tag(tags, tag, add):
   """Az add az egy flag, ha True akkor hozzáadjuk az uj tag-et, ha False elvesszük a listából"""
   add = int(add)
   
   print("{}: {}".format(type(tags), tags))
   if tags == 's':
      tags = []
   else:
      tags = ast.literal_eval(tags)

   print("{}: {}".format(type(tags), tags))
   if add == 1:
      if tag not in tags:
         print("yapp")
         tags.append(tag)
   elif add == 0:
      if tag in tags:
         print("nope")
         tags.remove(tag)

   print("{}: {}".format(type(tags), tags))

   tomb = dbhandler.init_lista()
   lentomb=len(tomb)
   szurt = dbhandler.szures(tags)
   if szurt == [] or szurt == None:
      return render_template('404.html')
   lista = dbhandler.lista(szurt)
   # print(lista)
   print(tags)
   return render_template('tag.html', tomb=tomb, lentomb=lentomb, lista = lista, lenlista = len(lista), tags=tags, lentags = len(tags))



if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0")

