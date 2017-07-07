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

#!/usr/bin/python3

import os
import time

class CpuUsage:


    def __init__(self,times):
        # Remeber times value so it can be reset any time
        self.default_times = times
        self.times = times
        self.cpu_data = []
        self.print_bar = self.get_cpu_usage()


    def get_cpu_usage(self):
        data = os.popen('mpstat').read()
        self.cpu_data = data[183:189]
        # You could convert it here from string to int so return value will be number ;)
        new_cpu_data = self.cpu_data.replace(',', '.')
        new_cpu_data = float(new_cpu_data)
        #new_cpu_data = int(new_cpu_data)
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

    def print_bar_of_cpu_usage(self):
        self.print_bar = int(self.print_bar)
        print_bar_length = 10
        print_bar_rest = print_bar_length - self.print_bar
        retval = "#"*self.print_bar + " "*print_bar_rest
        return retval

def main():
    cpu_usage = CpuUsage(100)
    usage = cpu_usage.get_cpu_usage()
    print(usage)

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
            print("Cpu Usage: ", cpu_usage.get_cpu_usage(),"[ ", cpu_usage.print_bar_of_cpu_usage()," ]")
            time.sleep(2)


if __name__ == "__main__":
    main()