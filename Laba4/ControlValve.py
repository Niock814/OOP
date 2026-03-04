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