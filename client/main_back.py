import socket
import _thread
import json
import os
import os.path
from psutil import net_if_addrs
from re import findall
import ipaddress
from ip.main import IP

class back_end:
    def __init__(self) -> None:
        #get the configuration
        self.json = open(os.path.join(os.path.split(__file__)[0],"config_back.json"))
        self.config = json.load(self.json)

        #define default boolean
        self.validate_deafault_ip = False

    def get_all_ip(self):
        interfaces = net_if_addrs()
        data = []
        network = {}
        for interface_name, interface_addresses in interfaces.items():
            for address in interface_addresses:
                if address.family == socket.AF_INET and address.netmask:
                    data.append(address.address)
                    network[address.address] = address.netmask
                elif address.family == socket.AF_INET6 and address.netmask:
                    data.append(address.address)
                    network[address.address] = address.netmask
        # delete the last element because it's allways "::1"
        data.pop()
        #return the data to be display and the network to have the netmask
        return data,network
    
    def check_ip_and_mask(self,ip = str(),mask = str()):
        ip = ip.split(".")
        mask = mask.split(".")
        if not len(ip) == 4 and len(mask) == 4:
            self.validate_deafault_ip = ["#00#","l'adresse ou le masque fournie n'est pas correcte"]
            return None
        result = []
        for index in range(4):
            try:
                ip_split    = bin(int(ip[index])).replace("0b","")
                mask_split  = bin(int(mask[index])).replace("0b","")
                result_split = ""
                for null in range(8-len(ip_split)):
                    ip_split += "0"
                for null in range(8-len(mask_split)):
                    mask_split += "0"
                for index_2 in range(8):
                    result_split += f"{int(ip_split[index_2]) and int(mask_split[index_2])}"
                result.append(int(result_split, base=2))
            except:
                self.validate_deafault_ip = ["#00#","l'adresse ou le masque fournie n'est pas correcte"]
                return None
        
        self.json.close()
        Ip = IP(f"{ip} /{len()}")#------------------------------------------------------------------------------------------



        self.validate_deafault_ip = True
        return None