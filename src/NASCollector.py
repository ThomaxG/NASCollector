__author__ = 'thomas'

import sqlite3
class Device :
    name = ''
    user =''
    password=''
    type=''
    collection_timestamp=''

    def __init__(self,n,u,p,t):
        self.name = n
        self.user = u
        self.password = p
        self.type = t


class DeviceList:
    devices = []
    def add_device(self,name,user,password,type):
        device = Device(name,user,password,type)
        device.name=name
        device.user=user
        device.password=password
        device.type=type

        self.devices.append(device)

    #def add_device(self,device):
    #   self.devices.append(device)


    def get_device_by_name(self,name):
        catched =''
        for dev in self.devices:
            if dev.name == name:
                catched = dev
                break
        return catched

class NASC:
    import_file =''
    NAS = DeviceList()
    db = sqlite3.connect('/home/thomasg/NASCollector/NASC.db')

    def init_DB(self):
        cursor = self.db.cursor()
        cursor.execute('''SELECT device_name, user, password, type FROM devices''')
        all_rows = cursor.fetchall()
        for row in all_rows:
            self.NAS.add_device(row[0], row[1], row[2], row[3])
        self.db.close()

    def print_NAS(self):
        for dev in self.NAS.devices:
            print(dev.name+' '+dev.user+' '+dev.password+' '+ dev.type)

    def import_NAS(self,file):
        import_file = open(file, 'r')
        import_lines = import_file.readlines()
        tokens = []

        cursor = self.db.cursor()
        cursor.execute('''DELETE FROM devices''')
        self.db.close()

        for line in import_lines:
            tokens = line.split(',')
            if (len(tokens) > 3):
                self.NAS.add_device(tokens[0],tokens[1],tokens[2],tokens[3])
        import_file.close()


def test_DB():
    nascI = NASC()
    nascI.import_NAS('/home/thomasg/NAS_test/NAS_import.csv')
    nascI.init_DB()
    nascI.print_NAS()

test_DB()






