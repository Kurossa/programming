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


def main():
    data = os.popen("mpstat").read()
    cpuusage = data[183:189]
    times = 10
    while times > 0:
        print("CPU Usage = " + cpuusage)
        times-=1
        time.sleep(2)

if __name__ == "__main__":
    main()