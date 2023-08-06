import numpy as np
import pandas as pd
import os
import pathlib
import subprocess
from subprocess import PIPE
import h5py
from sshtunnel import SSHTunnelForwarder
import sys
import socket
from pexpect import pxssh
import time
from collections import OrderedDict
from itertools import product
from icecream import ic
import fileinput
ic.enable()
class multiple_simulations:
    def __init__(self,
                 n_avail_proc = 20,
                 n_pps = 10
                 ):
        self.sim_list=[]
        self.n_avail_proc = n_avail_proc
        self.n_pps = n_pps #number of processors per simulation
    def run_serial(self):
        #create pandas table of simulations
        #while loop to run in sequence
        return 0
    def run_parallel(self):
        #create pandas table of simulations
        # sim_index | sim_name | sim_runs | status | list of parameters
        #While loop which check the status of simulations
        return 0
class simulation:
    def __init__(self,
                 proc_num = 2,
                 tmp_log_name = 'tmp.log',
                 run_command = 'mpirun'
                 ):
        #Default variables
        self.proc_num = 2
        self.tmp_log_file_name = 'tmp.log'
        self.tmp_log_file = None
        self.PARTIESINP = "parties.inp"
        self.sim_folder = None
        self.ssh_login = None
        self.exec_folder = None
        self.parties = None #process variable - to start/stop simulation
        self.run_status = False
        self.vars = None
        self.stop_flag = False
        self.run_command = run_command
        os.system('rm '+ self.tmp_log_file_name)
    def run(self):
        self.tmp_log_file = open(self.tmp_log_file_name,'a')
        if self.proc_num > 1:
            self.parties = subprocess.Popen([self.run_command,'-np', str(self.proc_num), './parties'],stdout=self.tmp_log_file)
        if self.proc_num == 1:
            self.parties = subprocess.Popen(['./parties'],stdout=self.tmp_log_file)
        self.status = True
    def stop(self):
        self.parties.kill()
        self.status = False
        self.stop_flag = False
        os.system('rm tmp.log')
    def set_vars(self,vars):
        od = OrderedDict(sorted(vars.items()))
        cart = list(product(*od.values()))
        self.vars = pd.DataFrame(cart,columns=od.keys())
    def change_line(self, file_name, line_keyword, value):
        for line in fileinput.input([file_name], inplace=True):
            if line.strip().startswith(line_keyword):
                new_line = line_keyword + str(value) + '\n'
                line = new_line
            sys.stdout.write(line)
    def change_parties_inp(self,cols,row):
        for comp in range(len(cols)):
            line_keyword = cols[comp]
            value = row[cols[comp]]
            self.change_line(self.PARTIESINP,line_keyword,value)
    def make(self):
        os.system('make clean')
        os.system('make')
        print('make')
    def ssh_connect(self):
        print('not implemented yet')
        try:
            conn = pxssh.pxssh()
            conn.login('134.169.62.45','metelkin','lwi')
            conn.sendline('metelkin && ls')
            conn.prompt()
            print(conn.before)
        except:
            print('smth went wrong')