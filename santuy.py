import os
import sys
import time
import random
import cookielib
import mechanize
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib
from multiprocessing.pool import ThreadPool

def tik():
    titik = [
     '\033[1;31m[\033[1;37m################\033[1;31m]  \033[1;35m0% ', '\033[1;31m[\033[1;34m####\033[1;37m############\033[1;31m] \033[1;35m40% ', '\033[1;31m[\033[1;34m#########\033[1;37m#######\033[1;31m] \033[1;35m60% ', '\033[1;31m[\033[1;34m##########\033[1;37m######\033[1;31m] \033[1;35m70% ', '\033[1;31m[\033[1;34m############\033[1;37m####\033[1;31m] \033[1;35m80% ', '\033[1;31m[\033[1;34m##############\033[1;37m##\033[1;31m] \033[1;35m90% ', '\033[1;31m[\033[1;34m################\033[1;31m] \033[1;35m100%', '\033[1;31m[\033[1;34m#####\033[1;37mSUKSES\033[1;34m#####\033[1;31m] \033[1;35m100%']
    for o in titik:
        print '\r\x1b[1;37m    [\033[1;32m+\033[1;37m] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)
tik()


