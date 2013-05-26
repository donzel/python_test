# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from threading import Thread
import redis
import time
import threading
from  Time_Reponse import Time_Reponse 
from datetime import datetime

class Stockage_time (threading.Thread): 
 
   
    port_listen =""
    
    #construteur
    def __init__(self,redis, port, size) :        
        threading.Thread.__init__(self)
        #super(StoppableThread, self).__init__()
        self.connect = redis
        self.port_listen = port
        self.size = size
        #hset =  self.connect.hgetall('result') 
        #suppression toute lignes
        #print hset
        #if len(hset) > 0 :
        #    print len(hset)
            #data = self.connect.hgetall('result')
            #for ligne in data :
               # self.connect.hdel('result', ligne)

    def stop(self):
        self.running = False

    # strat thread demarage de la collecte
    def run (self):
        
        self.running = True
        time_total = 0
        while self.running:
            time_total = 0
           #recuperation liste adr IP
            list =  self.connect.lrange("ip", 0, -1)
            for adr_ip in list :
                #print 'adr IP', adr_ip
           #Test get time and value time
                time_rep = Time_Reponse(self.port_listen)
                value  = time_rep.get_time()
                date  = time_rep.get_date()
                #temp totale des appel socket
                time_total = time_total + value
            #Thread  Prise de connaissance total  du temp en ms

                print "a l'heure ",date,"le temp est de ", value, "adresse ip = ",adr_ip
               
            #ajout du resultat dans la base de donnees
            self.saveResultBdd(time_total)
            #reset value time_total
            time_total = 0
            time.sleep(2)
            # test boucle avec un integer
            #increment = increment + 1
            
    
    def saveResultBdd (self,temptotal):
        #affichage du temp total
        
        print "temp_total", temptotal
        now = time.time()
        self.cleanResult()
        self.connect.hmset('result', {now:temptotal})   
        
    def show_result (self)  :
        dateList = []
        #self.connect.zrange("result", 0, -1)
        list = self.connect.hgetall('result') 
        # for data in list :
        print "all value",len(list)
       
        for var in list :
            
            help = time.localtime(float(var))
            datett = datetime(*help[:6])
            help2 = datett.strftime("%H:%M:%S")
            #f = float(help);
            dateList.append(help2)
           #dateList.
      
        #print range value
        
        sortedKeys=list.keys()
        print  sortedKeys
 
        sortedKeys.sort()
        list_b = {}
        print sortedKeys
        for va in sortedKeys :
            print "valeur ",va
            list_b[va] = self.connect.hget('result',va)
        
        #sorted(dateList, reverse = True)
        
        return list_b
    
        

    def setsize(self,new_size):
        self.size = new_size
    def cleanResult (self) :
        
       list = self.connect.hgetall('result') 
       print len(list) 
       
       if len(list) > self.size :
           nbr_supprimer = len(list) - self.size
           print nbr_supprimer
           i = 0
           while i <  nbr_supprimer :              
               sortedKeys=list.keys()
               sortedKeys.sort()
               key_a = sortedKeys[i]
               print "remove",key_a
               self.connect.hdel('result', key_a)
               i = i + 1
      # list_2 = self.connect.hgetall('result')  
      # print len(list_2)     
           
           
           
           
"""      @classmethod     
    def query(self,key, a, b):
        return read(key, max(a, b)) - read(key, min(a, b))
    @classmethod 
    def read(self,key, event):
        ixs = []
        while event > 0:
            ixs.append(event)
            event = event & (event - 1)
        return sum(self.redis.hmget(key, *ixs))
    @classmethod 
    def write (self, temptotal) :
        now = int(time.time())
        
        print "now = ",now
        expires = now + (10 * 60) + 10
        print "expires = ",expires
        all_users_key = 'online-users/%d' % (now // 60)
        print "all_users_key = ",all_users_key
        user_key = 'user-activity/%s' % temptotal
        print "user_key = ",user_key
        
    @classmethod    
    def get_user_last_activity(user_id):
        last_active = redis.get('user-activity/%s' % user_id)
        if last_active is None:
            return None
        return datetime.utcfromtimestamp(int(last_active))

    def get_online_users():
        current = int(time.time()) // 60
        minutes = xrange(app.config['ONLINE_LAST_MINUTES'])
        return redis.sunion(['online-users/%d' % (current - x)
                         for x in minutes])   
"""    