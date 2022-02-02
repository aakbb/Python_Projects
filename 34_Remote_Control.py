import random
import time

class Remote_Control:
    def __init__(self , tv_state = "Off" , volume = 0 , channel_list= ["TRT"] , channel = "TRT"):
        print("Remote Control is creating...")
        self.tv_state = tv_state
        self.volume = volume
        self.channel_list = channel_list
        self.channel = channel
        
    def open_tv(self):
        if self.tv_state == "On":
            print("TV is already on")
        else:
            print("TV opening ...")
            self.tv_state = "On"
    
    def close_tv(self):
        if self.tv_state == "Off":
            print("TV is already off")
        else:
            print("TV closing ...")
            self.tv_state = "Off"
            
    def set_the_sound(self):
        
        while True:
            answer =input( """
                Turn down the volume = <
                Turn up the volume = >
                For Quit = exit
                Your Transaction: """)
            
            if answer == "<":
                if self.volume != 0:
                    self.volume -= 1
                    print("Volume: " , self.volume)
            elif answer == ">":
                if self.volume != 32:
                    self.volume += 1
                    print("Volume: " , self.volume)
            else:
                print("Volume updated: " , self.volume)
                break
            
    def add_channel(self , channel_name):
        print("Channel is adding ...")
        time.sleep(1)
        self.channel_list.append(channel_name)
        print("{} added.".format(channel_name))
        
    def random_channel(self):
        randomc = random.randint(0, len(self.channel_list) -1)
        self.channel = self.channel_list[randomc]
        print("Current Channel: " , self.channel)
    
    def __len__(self):
        return len(self.channel_list)
    
    def __str__(self):
        return """
            TV State: {}
            TV Volume: {}
            Channel List: {}
            Current Channel: {}""".format(self.tv_state , self.volume , self.channel_list , self.channel)
            


remote_control = Remote_Control()
print("""
      ***********************************
                Welcome to TV App
      ***********************************
      Options:
      1.Open the Tv
      2.Close the Tv
      3.Set the Volume
      4.Adding a Channel
      5.Learn the Channels' Count
      6.Goes a Random Channel
      7.Show the TV's Information
      Q.For Quiting
      """)

while True:
    choose = input("Option's Number: ")
    if choose == "1":
        remote_control.open_tv()
        
    elif choose == "2":
        remote_control.close_tv()
        
    elif choose == "3":
        remote_control.set_the_sound()
        
    elif choose == "4":
        channel_name = input("Kanal isimlerini ',' ile ayırarak girin:")
        channel_list = channel_name.split(",")
        for will_add in channel_list:
            remote_control.add_channel(will_add)
            
    elif choose == "5":
        print("Channel's Count: " , len(remote_control))
        
    elif choose == "6":
        remote_control.random_channel()
        
    elif choose == "7":
        print(remote_control)
    elif choose == "Q":
        print("Quiting the App...")
        time.sleep(1)
        break
    else:
        print("Invalid Option Number.Please Try Again.")