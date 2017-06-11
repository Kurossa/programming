#!/usr/bin/python3

#CpuUsage
#self.cpu_usage
#GetCpuUsage ->should return number value of CPU usage
#PrintCpuUsage

#PrintCpuUsageBar [#.........]

#private function that will extract cpu usage
# def _name(self)

#def main():
    #data = os.system("mpstat")
    #print(data)
    #cpu_usage = CpuUsage
    #while(10 times)
      #data = cpu_usage.GetCpuUsage()
      #print (data)
      #cpu_usage.PrintCpuUsageBar(data)

import os
import time

class CpuUsage:

    def __init__ (self):
        self.getcpuusage()


    def getcpuusage(self):
        data = os.popen("mpstat").read()
        cpu = data[183:189]
        times = 10
        while times > 0:
            #print("CPU Usage = " + cpuusage)
            times = times - 1
            time.sleep(2)
        return cpu



def main():
    usage = CpuUsage.getcpuusage()
    print(usage)

if __name__ == "__main__":
    main()