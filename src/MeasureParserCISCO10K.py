__author__ = 'thomas'

usedIp_file = open('/home/thomasg/NAS_test/tln_numUsedIPaddVPN.out', 'r')
out_file = open('/home/thomasg/NAS_test/vpn.out', 'w')


def usedIpTotal(used_Ip_file):
    usedIp_list = usedIp_file.readlines()

    i = 0
    separator = 'Use'
    useful_line = -1
    tokens = []
    usedIp = 0
    for token in usedIp_list:
        line = token
        if (i == useful_line):
            tokens = line.split()
            print(tokens)
            usedIp = usedIp + int(tokens[-1])
            print('Used IP found:' + tokens[-1])

        if separator in line:
            useful_line = i + 4

        i = i + 1
    print('Used Ip Total:' + str(usedIp))

def LocalPool(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'numUsedIPAdd'
    measure2 = 'numFreeIPAdd'

    print('Measure - ' + measure1 + ' ' + measure2)
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()

    tokens = []

    numUsedIPAdd = 'ND'
    numFreeIPAdd ='ND'

    used = 0
    free = 0

    for line in command_output:
        tokens = line.split()
        if (tokens[0] != 'Pool'):
            if (len(tokens)>4):
                free = free + int(tokens[3])
                used = used + int(tokens[4])
            else:
                if (len(line) > 3):
                    free = free + int(tokens[2])
                    used = used + int(tokens[3])
    numFreeIPAdd = str(free)
    numUsedIPAdd = str(used)

    print(measure1+'='+numUsedIPAdd+' '+measure2+'='+numFreeIPAdd)



def IDB(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'IDBInUse'
    measure2 = 'IDBMax'

    print('Measure - ' + measure1 + ' ' + measure2)
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()
    tokens = []
    tokens = command_output[0].split()
    IDB_in_use = tokens[3]
    IDB_max = tokens[2]
    print(measure1+'='+IDB_in_use+' '+measure2+'='+IDB_max)

def PPPSession(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'numPPPoEactUsers'
    measure2 = 'numPPPoAactUsers'
    measure3 = 'numPPPactUser'

    print('Measure - ' + measure1 + ' ' + measure2 + ' ' + measure3)
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()
    tokens = []

    numPPPoAactUsers = 'ND'
    numPPPoEactUsers ='ND'
    numPPPactUser = 'ND'

    for line in command_output:
        tokens = line.split()
        if (tokens[1] == 'PPPoA'):
            numPPPoAactUsers = tokens[0]
        else:
            if (tokens[1] == 'PPPoE'):
                numPPPoEactUsers = tokens[0]
            else:
                if (tokens[1] == 'Total'):
                    numPPPactUser = tokens[0]


    print(measure1+'='+numPPPoEactUsers+' '+measure2+'='+numPPPoAactUsers+' '+measure3+'='+numPPPactUser)

def RejectedSession(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'rejected sessions'
    measure2 = 'accepted sessions'


    print('Measure - ' + measure1 + ' ' + measure2)
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()
    tokens = []

    rejected= 'ND'
    accepted ='ND'

    for line in command_output:
        tokens = line.split()
        if (tokens[2] == 'rejected'):
            rejected = tokens[3]
        if (tokens[4] == 'accepted'):
            accepted = tokens[5]



    print(measure1+'='+rejected+' '+measure2+'='+accepted)

def VPN(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'numVPN'
    measure2 = 'VPNnames'


    print('Measure - ' + measure1 + ' ' + measure2)
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()
    tokens = []
    numVPN = len(command_output) - 1

    VPNNames = []

    for line in command_output:
        tokens = line.split()
        if (tokens[0] != 'VRF'):
            VPNNames.append(tokens[0])

    print(measure1+'='+str(numVPN)+' '+measure2+'='+str(VPNNames))

def StaticPVC(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'numStaticPVC'

    print('Measure - ' + measure1 )
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()
    tokens = []
    numStaticPVC = len(command_output)



    print(measure1+'='+str(numStaticPVC))

def TotalATMif(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'numATM'

    print('Measure - ' + measure1 )
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()
    tokens = []
    numATM = 'ND'

    VPNNames = []

    for line in command_output:
        tokens = line.split()
        if (len(tokens) > 3):
            if (tokens[1] == 'ATM' and tokens[2] == 'network'):
                numATM = tokens[0]

    print(measure1+'='+numATM)

def showATMif(command,output_command):

    file_command = open(command, 'r')
    file_output_command = open(output_command, 'r')
    measure1 = 'totalPVC'
    measure2 = 'locIfInBitsSecTEL'
    measure3 = 'locIFOutBitsSecTEL'

    print('Measure - ' + measure1 + ' ' + measure2 + ' ' + measure3)
    command_list = file_command.readlines()

    print('Command: ')
    for line in command_list:
        print(line)

    command_output = file_output_command.readlines()
    tokens = []
    totalPVC = 'ND'
    locIfInBitsSecTEL = 'ND'
    locIFOutBitsSecTEL ='ND'

    VPNNames = []

    for line in command_output:
        tokens = line.split()
        if (len(tokens) > 6):
            if (tokens[5] == 'current' and tokens[6] == 'VCCs'):
                totalPVC = tokens[4]
            if (tokens[0] == '5' and tokens[1] == 'minute' and tokens[2] == 'input' and tokens[3] == 'rate'):
                locIfInBitsSecTEL = tokens[4]
            if (tokens[0] == '5' and tokens[1] == 'minute' and tokens[2] == 'output' and tokens[3] == 'rate'):
                locIFOutBitsSecTEL = tokens[4]

    print(measure1+'='+totalPVC+' '+measure2+'='+locIfInBitsSecTEL+' '+measure3+'='+locIFOutBitsSecTEL)

IDB('/home/thomasg/NAS_test/1_IDB_in_use.in','/home/thomasg/NAS_test/1_IDB_in_use.out')
PPPSession('/home/thomasg/NAS_test/3_Sessioni_PPP.in','/home/thomasg/NAS_test/3_Sessioni_PPP.out')
RejectedSession('/home/thomasg/NAS_test/4_Sessioni_rigettate.in','/home/thomasg/NAS_test/4_Sessioni_rigettate.out')
VPN('/home/thomasg/NAS_test/6_VPN.in','/home/thomasg/NAS_test/6_VPN.out')
StaticPVC('/home/thomasg/NAS_test/7_PVC_statici.in','/home/thomasg/NAS_test/7_PVC_statici.out')
TotalATMif('/home/thomasg/NAS_test/8_Interfacce_ATM_ver.in','/home/thomasg/NAS_test/8_Interfacce_ATM_ver.out')
showATMif('/home/thomasg/NAS_test/8_Interfacce_ATM_show_interface.in','/home/thomasg/NAS_test/8_Interfacce_ATM_show_interface.out')
LocalPool('/home/thomasg/NAS_test/2_Local_Pool.in','/home/thomasg/NAS_test/2_Local_Pool.out')
