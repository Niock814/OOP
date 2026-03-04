import math
import random
import datetime
import csv
import json
import os

class ControlValve:
    def __init__(self, model, diameter, pressure_nominal, Kv, actuator_type):
        self.__model = model
        self.__diameter = diameter
        self.__pressure_nominal = pressure_nominal
        self.__Kv = Kv
        self.__actuator_type = actuator_type
        self.__timestamp = datetime.datetime.now()

    @property
    def pressure(self):
        return self.__pressure_nominal

    @pressure.setter
    def pressure(self,pressure_nominal):
        if 0 < pressure_nominal:
             self.__pressure_nominal = pressure_nominal
        else:
             print("Pressure ValueError")

    @property
    def Kv(self):
        return self.__Kv

    @Kv.setter
    def Kv(self,Kv):
        if 0 < Kv and Kv < 1:
             self.__Kv = Kv
        else:
             print("Kv ValueError")

    @property
    def flow_coefficient(self):
        flow_rate = self.__Kv * math.sqrt(2)
        return flow_rate
    
    @property
    def diameter(self):
        return self.__diameter
    
    @property
    def model(self):
        return self.__model
    
    @property
    def actuator_type(self):
        return self.__actuator_type
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @timestamp.setter
    def timestamp(self, value):
        if isinstance(value, datetime.datetime):
            self.__timestamp = value
        else:
            print("Timestamp must be datetime object")
    

    def __str__(self):
        return(f"Клапан {self.__model}, DN = {self.__diameter} мм, PN = {self.__pressure_nominal} Бар, Kv = {self.__Kv}, Привод {self.__actuator_type}, Коэффцициент потока = {self.flow_coefficient}")
    
    def __repr__(self):
        return(f"Class: ControlValve, model = {self.__model}, diameter = {self.__diameter}, pressure_nominal = {self.__pressure_nominal}, Kv = {self.__Kv}, actuator_type = {self.__actuator_type}, flow_rate = {self.flow_coefficient}")

    def __eq__(self,other,):
        if not isinstance(other, ControlValve):
            return False
            
        return self.model == other.model

    def __lt__(self, other):
         if not isinstance(other, ControlValve):
            return False
         
         return self.diameter < other.diameter
    
    def __add__(self,other):
        if not isinstance(other, ControlValve):
            return False
        if self.model == other.model and self.actuator_type == other.actuator_type:
            model =  self.model
            actuator_type = self.actuator_type
            diameter = self.diameter +  other.diameter
            pressure_nominal = self.pressure + other.pressure
            Kv = (self.Kv/2) + (other.Kv/2)
            return ControlValve(model, diameter,pressure_nominal,Kv,actuator_type)

        else: False
        
    def to_dict(self):
        return {
        "model": self.__model,
        "diameter": self.__diameter,
        "pressure": self.__pressure_nominal,
        "kv": self.__Kv,
        "actuator_type": self.__actuator_type,
        "time": self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')}
    

def  generate_test_data (n, **kwargs):
        data_list = []
        models = ["Односедельный","Двухседельный","Клеточный","Мембранный","Золотниковый"]
        actuators = ["Ручной", "Электрический", "Электромагнитный","Пневматический","Гидравлический"]
        d_min, d_max = kwargs.get('d_range', (5, 150))
        p_min, p_max = kwargs.get('p_range', (10, 100))
        start_time =  datetime.datetime.now()
        delta = datetime.timedelta(seconds=5)

        for i in range(n):
            diameter = random.randint(d_min, d_max)
            pressure = random.randint(p_min, p_max)
            Kv = round(random.random(), 2)
            model = random.choice(models)
            actuator_type = random.choice(actuators)
            obj = ControlValve(model, diameter, pressure, Kv, actuator_type)
            obj.timestamp = start_time + (delta * i)
            data_list.append(obj)

        return data_list
    
def save_to_csv(filename, data):
    dicts = [obj.to_dict() for obj in data]
    

    with open(filename, 'w', newline='', encoding='utf-8') as f:
       
        writer = csv.DictWriter(f, fieldnames=dicts[0].keys(), delimiter=';')
        writer.writeheader()        
        writer.writerows(dicts)    
 

def save_to_json(filename, objects):
    dicts = [obj.to_dict() for obj in objects]
    with open(filename, 'w', encoding='utf-8') as f:
      
        json.dump(dicts, f, indent=2, ensure_ascii=False)


    
    
data = generate_test_data(100, d_range=(10, 20), p_range=(1, 2))

save_to_csv("data.csv", data)
save_to_json("data.json", data)

for item in data[:5]:
        
     print(item.to_dict())