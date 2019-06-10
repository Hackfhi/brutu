import sys
from threading import RLock


lock = RLock()

def get_input(value):
    if sys.version[0] == '3':
        return input(value)
    else:
        return raw_input(value)

def colors(value):
    patterns = {
        '  ' : '',
        'CC' : '\033[0m',
        'BB' : '\033[1m',
        'D1' : '\033[30;1m',
        'D2' : '\033[30;2m',
        'R1' : '\033[31;1m',
        'R2' : '\033[31;2m',
        'G1' : '\033[32;1m',
        'G2' : '\033[32;2m',
        'Y1' : '\033[33;1m',
        'Y2' : '\033[33;2m',
        'B1' : '\033[34;1m',
        'B2' : '\033[34;2m',
        'P1' : '\033[35;1m',
        'P2' : '\033[35;2m',
        'C1' : '\033[36;1m',
        'C2' : '\033[36;2m',
        'W1' : '\033[37;1m',
        'W2' : '\033[37;2m',
        'MM' : '\033[31;4m'
    }
    for i in patterns:
        value = value.replace('[{}]'.format(i), '{}'.format(patterns[i]))
    return value

def lol(value=''):
    with lock:
        print(colors('[D1]{}[C2]'.format(value)))

def lol_replace(value):
    with lock:
        sys.stdout.write('{}\r'.format(colors('[P1]{}[CC]'.format(value))))
        sys.stdout.flush()

def str_input(value, validate=True, enter=False):
    with lock:
        while True:
            result = str(get_input(colors('[D1]{} [R1]: [Y1]'.format(value))))
            if result and result != None or validate == False:
                if enter: print('')
                return result

def opt_input(value, options = [], enter=False):
    with lock:
        while True:
            result = str(get_input(colors('[D1]{} [R1]: [Y1]'.format(value))))
            if result.lower() in [x.lower() for x in options]:
                if enter: print('')
                return result

def exit(value='[R1]> Keluar', confirm=True, front_enter=False, back_enter=True):    
    with lock:
        if front_enter: print('')
        if confirm:
            if opt_input('> KELUAR? y/n', ['n','y']) == 'y':
                if back_enter: print('')
                lol(value)
                sys.exit()
            if back_enter: print('')
        else:
            lol(value)
            sys.exit()

