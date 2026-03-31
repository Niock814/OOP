import math
import random
import datetime
from Base import equipment




class ControlValve(equipment):
    def __init__(self, model, diameter, pressure_nominal, Kv, actuator_type):
        super().__init__(model) 
        self.__diameter = diameter
        self.__pressure_nominal = pressure_nominal
        self.__Kv = Kv
        self.__actuator_type = actuator_type
        

    @property
    def unit(self):
        
        return "бар"
    
    def read_value(self):

        return self.__pressure_nominal


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
    def flow_rate(self):

        return self.__Kv * math.sqrt(2)
    
    @property
    def diameter(self):
        return self.__diameter
      
    @property
    def actuator_type(self):
        return self.__actuator_type
    

    def __str__(self):
        return(super().__str__()+f"\nDN = {self.__diameter} мм\n PN = {self.__pressure_nominal} {self.unit}\n Kv = {self.__Kv}\n Привод {self.__actuator_type}")
    
    def __repr__(self):
        return(f"Class: ControlValve, model = {self.__model}, diameter = {self.__diameter}, pressure_nominal = {self.__pressure_nominal}, Kv = {self.__Kv}, actuator_type = {self.__actuator_type}")

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
        data = super().to_dict()

        data.update( {
        "diameter": self.__diameter,
        "pressure": self.__pressure_nominal,
        "kv": self.__Kv,
        "actuator_type": self.__actuator_type,
        "unit": self.unit})
        return data
    

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