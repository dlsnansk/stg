#!/usr/bin/env python3
# stg.py
# Tag generator, like in video games and military themes
import random as r
import sys, os
verb=('Shadow', 'Ghost', 'Void', 'Zero', 'Dark', 'Neon', 'Cyber', 'Pulse', 'Flame', 'Steel', 'Rust', 'Echo', 'Storm', 'Canon', 'Alpha', 'Bravo', 'Charlie', 'Delta', 'Gamma', 'Midnight')
noun=('Packet', 'Route', 'Node', 'Trace', 'Walker', 'Vector', 'Relay', 'Signal', 'Cipher', 'Drift', 'Chrome', 'Dogma', 'Sphere')
numbers='0123456789'
cut='''
=========================
'''
def cl():
    os.system('cls'if os.name=='nt'else 'clear')
def hello():
    cl()
    print(f'''
===== W E L C O M E =====
========== T O ==========
========= S T G =========

the__serial_tag_generator 
''')
    input(f'\nPress ENTER to continue... ')
def main():
    try:
        hello()
        while True:
            cl()
            while True:
                t=0
                tag=''
                try:
                    usr_nmb=int(input(f'Enter the NUMBER of the TAGs [1-9999]: '))
                    if 0<usr_nmb<=9999:
                        pass
                    else:
                        break
                except Exception:
                    break
                print(cut)
                while True:
                    nma=r.choice(numbers)
                    nmb=r.choice(numbers)
                    vv=r.choice(verb)
                    nn=r.choice(noun)
                    tag=f'{t+1}. {vv}{nn}_{nma}{nmb}'
                    print(tag)
                    t+=1
                    tag=''
                    if t==usr_nmb:
                        print(cut)
                        break
                usr_cnt=input(f'\n[A]gain / [Q]uit ? ').strip().lower()
                if usr_cnt=='a':
                    cl()
                    continue
                else:
                    cl()
                    sys.exit()
    except KeyboardInterrupt:
        print(f'\nSTG has been stopped... ')
        sys.exit()
main()