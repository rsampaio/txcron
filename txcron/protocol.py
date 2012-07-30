from twisted.internet import reactor
from txscheduling.cron import CronSchedule
from collections import deque
from datetime import datetime

tasks = deque()

def task(cronformat):
    cron = CronSchedule(cronformat)
    delay_sec = (cron.getNextEntry() - datetime.now()).seconds
    print "on decorator", cron.getNextEntry()
    def decorator(f):
        gargs = []
        gkargs = {}
        def wrapper(*args, **kargs):
            gargs = args
            gkargs = kargs
        print delay_sec, gargs, gkargs
        reactor.callLater(delay_sec, wrapper, gargs, gkargs)
        return wrapper
    return decorator

def cron_start():
    reactor.run()
