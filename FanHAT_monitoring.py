#!/usr/bin/env python
from __future__ import division
from subprocess import PIPE, Popen
import psutil


def getCPUtemperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    CPUtemp = float(output[output.index('=') + 1:output.rindex("'")])
    return CPUtemp

def getCPUuse():
    cpu_usage = psutil.cpu_percent()
    return cpu_usage

def getRAMinfo():    
    ram_used = (psutil.virtual_memory().total - psutil.virtual_memory().available)
    ram_total = psutil.virtual_memory().total
    ram_free = (psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    ram_percent_used = psutil.virtual_memory().percent
    return ram_total,ram_used,ram_free,ram_percent_used

def getDiskSpace():
    disk = psutil.disk_usage('/')
    disk_total = disk.total / 2**30     # GiB.
    disk_used = disk.used / 2**30
    disk_free = disk.free / 2**30
    disk_percent_used = disk.percent
    return disk_total,disk_used,disk_free,disk_percent_used
    
def VirtualRAM():
    # 
    # Print top five processes in terms of virtual memory usage.
    # 
    processes = sorted(
        ((p.get_memory_info().vms, p) for p in psutil.process_iter()),
        reverse=True
    )
    for virtual_memory, process in processes[:5]:
        print (virtual_memory // 2**20, process.pid, process.name)
