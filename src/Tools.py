# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.


class Tools :
    
    @staticmethod
    def int2String(integer):
        return str(integer)
    @staticmethod
    def get_date():        
        now = datetime.datetime.now()
        var = now.strftime("%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        print "Current date and time using str method of datetime object:"
        return var