from flask import Flask, render_template

import dbhandler

app = Flask(__name__)

@app.route('/')
def index():
   tomb = dbhandler.init_lista()
   lentomb=len(tomb)
   return render_template('index.html', tomb=tomb, lentomb=lentomb)

if __name__ == '__main__':
   app.run()

