import math

class ControlValve:
    def __init__(self, model, diameter, pressure_nominal, Kv, actuator_type):
        self.__model = model
        self.__diameter = diameter
        self.__pressure_nominal = pressure_nominal
        self.__Kv = Kv
        self.__actuator_type = actuator_type

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

    def get_flow_coefficient(self):
        flow_rate = self.__Kv * math.sqrt(2)
        return flow_rate
    
    def get__diameter(self):
        return self.__diameter
    def get_model(self):
        return self.__model
    def get_actuator_type(self):
        return self.__actuator_type
    

    def __str__(self):
        return(f"Клапан {self.__model}, DN = {self.__diameter} мм, PN = {self.__pressure_nominal} Бар, Kv = {self.__Kv}, Привод {self.__actuator_type}, Коэффцициент потока = {self.get_flow_coefficient()}")
    
    def __repr__(self):
        return(f"Class: ControlValve, model = {self.__model}, diameter = {self.__diameter}, pressure_nominal = {self.__pressure_nominal}, Kv = {self.__Kv}, actuator_type = {self.__actuator_type}, flow_rate = {self.get_flow_coefficient()}")

    def __eq__(self,other,):
        if not isinstance(other, ControlValve):
            return False
            
        return self.get_model() == other.get_model()

    def __lt__(self, other):
         if not isinstance(other, ControlValve):
            return False
         
         return self.get__diameter() < other.get__diameter()
    
    def __add__(self,other):
        if not isinstance(other, ControlValve):
            return print("Другой Класс")
        if self.get_model() == other.get_model() and self.get_actuator_type() == other.get_actuator_type():
            model =  self.get_model()
            actuator_type = self.get_actuator_type()
            diameter = self.get__diameter() +  other.get__diameter()
            pressure_nominal = self.pressure + other.pressure
            Kv = (self.Kv/2) + (other.Kv/2)
            return ControlValve(model, diameter,pressure_nominal,Kv,actuator_type)

        else: print("Ошибка, разные модели или приводы")
       
       


valve1 = ControlValve("Мембранный", 50, 10, 0.9, "Гидравлический")
valve2 = ControlValve("Мембранный", 30, 5, 0.70, "Гидравлический")
valve3 = ControlValve("Клетчатый", 10, 100, 0.89, "Электрический")

print(valve3)

print(repr(valve2))

print(valve1 == valve2)

print(valve1 == valve3)

print(valve1+valve2)