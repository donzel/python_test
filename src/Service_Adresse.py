# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

#Constructeur 
class Service_Adresse () :
    
    def __init__(self,redis) :
        self.connect = redis
        

    def getAll_adresse_IP(self):
        list =  self.connect.lrange("ip", 0, -1)
        return list
        
    def add_ip_adress(self,ipAdress):
        
        var_init =""
        var_init = ipAdress
        
        self.connect.rpush("ip", var_init)
    
    def remove_ip_adress(self,ipAdress) :
        var_init =""
        var_init = ipAdress
        self.connect.lrem( "ip",0,var_init )