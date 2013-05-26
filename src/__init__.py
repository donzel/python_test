__author__="mister"
__date__ ="$25 mai 2013 18:56:36$"

#Flask  et import 
from flask import Flask, render_template, request, redirect, url_for, abort, session
from flask_assets import Bundle
from flask.ext.assets import Environment, Bundle
import flask_sijax
import os
import redis 
import time
from Stockage_time import Stockage_time
import datetime
from Service_Adresse import Service_Adresse
from werkzeug.routing import Rule
app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';
assets = Environment(app)
assets.init_app(app)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
list_a = []
list_b = []
nbr_donne = 10 
thread = Stockage_time(r,"55", nbr_donne) 
#
#app.url_map.add(Rule('/addIP_adr', endpoint='addIP_adrs'))
js = Bundle('js/highcharts.js','js/jquery-1.8.2.min.js','js/highcharts-convert.js','js/highcharts-more.js',  output='js/highcharts.js')
assets.register('js_all', js)

@app.route('/')
def home():
    
    list_a = []
    list_b = []
    
           
    list = thread.show_result()
    data = ""
    sortedKeys=list.keys()
    sortedKeys.sort()
    for adr_ip in sortedKeys :
        data = adr_ip
        list_b.append(list.get(data))
        help = time.localtime(float(data))
        datett = datetime.datetime(*help[:6])
        help2 = datett.strftime("%H:%M:%S")
        list_a.append(help2)
        # Regular non-Sijax request) - render the page template
    
   # help = datetime.datetime.strptime(data, "%Y%m%d%H%M%S")
    return render_template('index.html',list_time =list_a ,list_value = list_b)
@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
@app.route('/serviceSonde')
def sonde_service():
   # r = redis.StrictRedis(host='localhost', port=6379, db=0)
    
    #var  = list_ip [0]
    return render_template('serviceSonde.html')
@app.route('/serviceIP')
def ip_service():
   # r = redis.StrictRedis(host='localhost', port=6379, db=0)
    service_ip = Service_Adresse(r)    
    list_ip  = service_ip.getAll_adresse_IP()
    #var  = list_ip [0]
    return render_template('srvIP.html',list=list_ip)
@app.route('/addIPadr', methods=[ 'POST'])
def add_ip():
    if request.method == 'POST':
        ip = request.form['adrip']
        if not ip:
            return 'la variable est vide', 404
        else :
            if 'add' in request.form:
                service_ip = Service_Adresse(r)    
                service_ip.add_ip_adress(ip)
                return render_template('addIPadr.html',ip=ip) 
            elif 'remove' in request.form:
                service_ip = Service_Adresse(r)    
                service_ip.remove_ip_adress(ip)
                return render_template('delIPadr.html',ip=ip)
    else:
        return  ip_service()
    #return render_template('addIPadr.html')

@app.route('/actionSonde', methods=[ 'POST'])
def serviceSonde():
    if request.method == 'POST':   
        if 'start' in request.form :
            #tifhread = Stockage_time(r,"55", nbr_donne) 
            if not thread.isAlive()  :
                thread.start()
            
            valeur = "sonde demarre"
            return render_template('etat.html',valeur = valeur)
        elif 'stop' in request.form : 
            
            thread.stop()
            thread.join()
            valeur = "sonde arrete"
            return render_template('etat.html',valeur = valeur)
        elif 'update' in request.form :
            new_size = request.form['new_size']            
            if not new_size:
                return 'la variable est vide', 404
            else :            
                thread.setsize(new_size)
                valeur = "mise a jour du nombre enregistrement "+ new_size
                return render_template('etat.html',valeur = valeur)
    else :       
        return  ip_service()
    #return render_template('addIPadr.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
    