#!/usr/bin/python3 
from multiprocessing import Pool, Process, Lock
import sys, traceback
from pyco.device import device
import logging
from configobj import ConfigObj, flatten_errors
import pyco
from database import Database

import localPool

TELNET_PORT = 7777

def cmd_AA(host):
    host.send("command_a_generic")
    host.send("command_a_specific")


def cmd_BB(host):
    host.send("show interfaces")
        
def cioscoios_show_ip_local_pool(host):
    out = host.send("show ip local pool")
    localPool.parse(out)

def command(host):
    try:
        print("----> [%s]" % host.driver)
        if (host.driver.name == "ciscoios"):
            cioscoios_show_ip_local_pool(host)
        elif(host.driver.name == 'juniper'):
            print("Thommy lets happen!")
        else:
            print("unknown device type %s" % host.driver)
    except Exception:
        #print("%s: interrogazione fallita, vedere file di log per i dettagli" % host.name)
        #traceback.print_exc(file=sys.stdout)
        logging.exception("interrogazione fallita")
    finally:
        pass

if __name__ == '__main__':

    indb = Database()
    
    with Pool(4) as pool:
    
        for n in indb.getall():
            print("telnetting %s" % n.name)
            host = device('telnet://%s:%s@%s:%d/ciscoios' % 
                   (n.username, n.password, 'localhost', TELNET_PORT))
            
            pool.apply(command, (host,))
    
