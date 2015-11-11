def parse(output):

    measure1 = 'numUsedIPAdd'
    measure2 = 'numFreeIPAdd'

    print('Measure - ' + measure1 + ' ' + measure2)

    command_output = output.split('\n')

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

