from socket import socket,AF_INET,SOCK_STREAM
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

        #define default variable
        self.message_reciev = False
    
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
        
    def connect_server(self):
        self.connection_server = socket(AF_INET, SOCK_STREAM)
        while True:
            try:
                self.connection_server.connect()
                break
            except:
                pass
        while True:
            test = self.connection_server.recv(1024)
            if test:
                self.message_reciev = test

        
    def get_log(self):
        pass