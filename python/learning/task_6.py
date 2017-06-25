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
    def __init__(self, time):
        self.time = time
        self.cpu_data = []

    def cpu_usage_return(self):
        data = os.popen('mpstat').read()
        self.cpu_data = data[183:189]
        return self.cpu_data

    def cpu_usage_print(self):
        while self.time > 0:
            self.time -= 1
            return self.cpu_data


def main():
    usage = CpuUsage(10)
    usaged = usage.cpu_usage_print()
    print(usaged)


if __name__ == "__main__":
    main()