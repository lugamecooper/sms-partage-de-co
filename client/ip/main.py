import re
class IP:
    """
    this class can return
        the ipv4, 
        the binary mask, 
        the mask, 
        the wilcard mask, 
        the network ip
    """
    def __init__(self, ip="ex: 192.168.0.1 optional[/24]"):
        self.test = re.findall(r"(\d{1,3})[.](\d{1,3})[.](\d{1,3})[.](\d{1,3}) ?.?(\d{1,2})?",ip)
        if self.test:
            self.test = self.test[0]
            self.test_ip()
            self.ipv4 = f"{self.test[0]}.{self.test[1]}.{self.test[2]}.{self.test[3]}"
            self.mask_cidr = f"{self.test[4]}"
            self.make_bin_ip()
            self.define_class_adress()
            self.type_adress_ip()
            if self.mask_cidr and self.test[4]:
                self.mask()
                self.network()
                self.broadcast()
            else:
                self.mask_bin = None
                self.mask_cidr = None
                self.wilcard_mask = None
                self.ipv4_network = None
                self.ipv4_network_bin = None
                self.type_adress = None
        else:
            print(self.test)
            raise Exception(f"specify an ip")
        
    def test_ip(self):
        i = 0
        for t in self.test:
            i +=1
            try:
                int(t)
                t = int(t)
            except:
                raise TypeError(f"{i} isn't a valid number")
            if t > 255 or t < 0 :
                raise ValueError(f"invalid ip at the position {i}")
            if i == 4:
                break
        if self.test[4]:
            if int(self.test[4]) < 0 or int(self.test[4]) > 32:
                raise ValueError(f"invalid mask")
        else:
            self.test = list(self.test)
            self.test[4] = False
            

    def type_adress_ip(self):
        tempo = {
            "adresse de bouclage":False,
            "classe a":8,
            "classe b":16,
            "classe c":24,
            "classe d":False,
            "classe e":False,
        }
        if not self.test[4]:
            self.test[4] = tempo[self.adress_class]
            self.mask_cidr = tempo[self.adress_class]
        if self.test[0] == "10":
            self.type_adress = "privée"
        elif self.test[0] == "172" and (int(self.test[1]) < 32 and int(self.test[1]) > 15):
            self.type_adress = "privée"
        elif self.test[0] == "192" and self.test[1] == "168":
            self.type_adress = "privée"
        elif self.adress_class == "classe d":
            self.type_adress = "multicast"
        else:
            self.type_adress = "publique"

    def define_class_adress(self):
        if int(self.test[0]) == 127:
            self.adress_class = "adresse de bouclage"
        elif int(self.test[0]) < 127:
            self.adress_class = "classe a"
        elif int(self.test[0]) < 192:
            self.adress_class = "classe b"
        elif int(self.test[0]) < 224:
            self.adress_class = "classe c"
        elif int(self.test[0]) < 240:
            self.adress_class = "classe d"
        else:
            self.adress_class = "classe e"

    def make_bin_ip(self):
        self.ipv4_bin = ""
        for i in range(4):
            tempo = bin(int(self.test[i])).replace("0b","")
            for a in range(8-len(tempo)):
                tempo = "0" + tempo
            self.ipv4_bin += f"{tempo}."
        self.ipv4_bin = self.ipv4_bin.removesuffix(".")

    def mask(self):
        self.mask_cidr = int(self.mask_cidr)
        self.wilcard_mask = 32 - self.mask_cidr
        dif_tempo = self.wilcard_mask
        self.mask_bin = ""
        while dif_tempo:
            self.mask_bin = self.mask_bin + "0"
            dif_tempo -= 1
        mask_cidr = self.mask_cidr 
        while mask_cidr:
            self.mask_bin = "1" + self.mask_bin 
            mask_cidr -= 1
        i = 0
        tempo = ""
        for t in self.mask_bin:
            i += 1
            tempo = tempo + t 
            if i == 8:
                tempo = tempo + "."
                i = 0
        tempo = tempo + " "
        tempo = tempo.replace(". ","")
        self.mask_bin = tempo

    def network(self):
        self.ipv4_network_bin = ""
        self.ipv4_network = ""
        tempo = ""
        for i in range(len(self.ipv4_bin)):
            if self.ipv4_bin[i] == "1" and self.mask_bin[i] == "1":
                tempo += "1"
            elif self.ipv4_bin[i] == "." and self.mask_bin[i] == ".":
                self.ipv4_network += f"{int(tempo,2)}."
                self.ipv4_network_bin += f"{tempo}."
                tempo = ""
            else:
                tempo += "0"
        self.ipv4_network += f"{int(tempo,2)}"
        self.ipv4_network_bin += f"{tempo}"

    def broadcast(self):
        self.ipv4_broadcast_bin = ""
        for index in range(len(self.mask_bin)):
            try:
                if int(self.mask_bin[index]) and int(self.ipv4_network_bin[index]):
                    self.ipv4_broadcast_bin += "1"
                elif int(self.mask_bin[index]) and not int(self.ipv4_network_bin[index]):
                    self.ipv4_broadcast_bin += "0"
                elif int(self.mask_bin[index]) == 0:
                    self.ipv4_broadcast_bin += "1"
            except Exception as er:
                if self.mask_bin[index] == ".":
                    self.ipv4_broadcast_bin += "."
        ipv4_broadcast = self.ipv4_broadcast_bin.split(".")
        for index in range(len(ipv4_broadcast)):
            ipv4_broadcast[index] = f"{int(ipv4_broadcast[index],base=2)}"
        self.ipv4_broadcast = ".".join(ipv4_broadcast)