

import redis 
import time
from  Time_Reponse import Time_Reponse 
from Stockage_time import Stockage_time
from Service_Adresse import Service_Adresse
import sys
import threading

__author__="luc"
__date__ ="$25 mai 2013 11:39:30$"


if __name__ == "__main__":
    print "Demaragge de la collecte d'information"
  
r = redis.StrictRedis(host='localhost', port=6379, db=0)

#Test BDD
test  =r.get('foo')
#redis.disconnect()
print 'return value ', test

#Test recuperation heure + date
time_rep = Time_Reponse("55")
value  = time_rep.get_time()
date  = time_rep.get_date()
print "a l'heure ",date,"le temp est de ", value

adresse_ip_1 = "toto@toto.fr"
adress_ip_2  = "0.0.0.0.0"
if r.llen("ip") == 0 :
    print "nbr ip =",r.llen("clesliste")
    print "ajout adr IP "
    r.rpush("ip", adresse_ip_1)
    r.rpush("ip", adress_ip_2)

else :
    print "nbr ip =",r.llen("ip")
    list =  r.lrange("ip", 0, -1)    
    # print list[1]
    #r.ltrim(list[1],"ip")
    
    #print "nbr ip =",r.llen("ip")
    #r.ltrim("ip", 0, 2)
# En mode thread le stockage des donnees
num_port = "3333"
print "Starting the threads"
size = 6
#demarage du stockage des donnees heure + date
thread = Stockage_time(r,num_port,size)
#time(r,num_port)
thread.start()

#arret du thread
#time.sleep(4)
#thread.stop()
#thread.show_result()
thread.cleanResult()
"""
print "fin du thread"
service_ip = Service_Adresse(r)    
list_ip  = service_ip.getAll_adresse_IP()
var  = list_ip [0]
print "nbr ip =",list
service_ip.remove_ip_adress("lol")
"""

