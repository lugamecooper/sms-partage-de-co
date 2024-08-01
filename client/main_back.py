import socket
import _thread
import json
import os
import os.path
from re import findall
from ip.main import IP

class back_end:
    def __init__(self) -> None:
        #get the configuration
        self.json = open(os.path.join(os.path.split(__file__)[0],"config_back.json"))
        self.config = json.load(self.json)

        #define default boolean
        self.validate_deafault_ip = False
    
    def check_ip(self,ip : str):
        try:
            self.json.close()
            Ip = IP(ip)
            self.config["target ip"] = Ip.ipv4
            self.config["first use"] = False

            json.dump(self.config,open(os.path.join(os.path.split(__file__)[0],"config_back.json"),"w"))
            self.json = open(os.path.join(os.path.split(__file__)[0],"config_back.json"))

            return True
        except Exception as er:
            print(er)
            return ["#00#",er]