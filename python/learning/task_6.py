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
import re

class CpuUsage:


    def __init__(self,times):
        # Remeber times value so it can be reset any time
        self.default_times = times
        self.times = times
        self.cpu_data = []
        self.last_cpu_usage = 0


    def get_cpu_usage(self,interv):
        cmd = 'mpstat 1 '
        cmd += str(interv)
        data = os.popen(cmd).read()
        match = re.search(r'..all........', data)
        if match:
            data = match.group()[7:]
        else:
            return -1.0
        self.cpu_data = data
        # You could convert it here from string to int so return value will be number ;)
        new_cpu_data = self.cpu_data.replace(',', '.')
        new_cpu_data = float(new_cpu_data)
        #new_cpu_data = int(new_cpu_data)
        self.last_cpu_usage = new_cpu_data
        return new_cpu_data


    def times_protection(self):
        if self.default_times <= 0:
            return True

    def read_and_decrease_times(self):
        # First you read the value than you decrease it and return not decreased value
        retval = self.times
        self.times -= 1

        # You coud add protection of seting negative values
        # if self.times < 0
        #     self.times = 0
        return retval


    def reset_times(self):
        self.times = self.default_times


    # This function prints bar based on last self.get_cpu_usage value
    def print_bar_of_cpu_usage(self, bar_length):
        #self.last_cpu_usage = self.get_cpu_usage(1)
        print_bar_length = bar_length
        print_bar_front = int(self.last_cpu_usage/100*print_bar_length)
        print_bar_back = print_bar_length - print_bar_front
        retval = "["
        retval += "#"*print_bar_front + " "*print_bar_back
        retval += "]"
        return retval

def main():
    cpu_usage = CpuUsage(10)

    # This will not work correctly, as usage will be get only once and print same value 10 times
    # To do it right you need to read usage each time in loop, then print
    # It is nothing bad in using internal fields of class like cpu_usage.time, but it is not elegant
    # I would suggest function that will decrease and read times value and returns it
    # see corected while loop below
    #print('Your loop')
    #while cpu_usage.times > 0:
    #    print(usage)
    #    cpu_usage.times -= 1
    #    time.sleep(2)


    # It should be done like this
    print('My loop')
    if cpu_usage.times_protection() == True:
        print ("Program STOP. Error: Repeat value needs to be at least one.")
    else:
        cpu_usage.reset_times()
        while cpu_usage.read_and_decrease_times():
            print("\rCpu Usage: ", '{:06.2f}'.format(cpu_usage.get_cpu_usage(1)), cpu_usage.print_bar_of_cpu_usage(25),end="", flush=True)



if __name__ == "__main__":
    main()