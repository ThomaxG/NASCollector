#!/usr/bin/python3
import pyco
from database import Database
import time
import transaction

if __name__ == '__main__':
    
    indb = Database()
    
    start = time.time()
    ciscoios_template = "cisco_%d"
    juniper_template = "juniper_%d"

    try:
        transaction.begin()
        #indb.create("localhost", "ciscoios", "pippo", "secret")
        
        for idx in range(0,2):
            indb.create(ciscoios_template % idx, "ciscoios", "pippo", "secret")
        for idx in range(0,0):
            indb.create(juniper_template % idx, "juniper", "pluto", "secret")
            
        transaction.commit()
    except Exception as e:
        print("insert failed: %s" % e)
        print("\nRemember to delete database before loading\n")
        
    #print("end: %f" % (time.time() - start))

         