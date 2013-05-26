
import random
import datetime
# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Time_Reponse :
    
    timer = 0 
    port = "" 
    def __init__(self , port):
        self.port = port
    
    def get_time(self):
        #random_time = 0
        random_time = random.randint(1,100)
        #print "random" ,random.randint(1,100)
        ##val = 2
        return random_time
    def get_date(srandom_timeelf):        
        now = datetime.datetime.now()
        var = now.strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        print "Current date and time using str method of datetime object:"
        return var
    
        
