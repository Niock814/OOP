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
        return self.get_actuator_type
    
    def info(self):
        print(f"Клапан {self.__model}, DN = {self.__diameter} мм, PN = {self.__pressure_nominal} Бар, Kv = {self.__Kv}, Привод {self.__actuator_type}, Коэффцициент потока = {self.get_flow_coefficient()}")

    
valve1 = ControlValve("Мембранный", 50, 10, 0.9, "Гидравлический")

valve1.pressure = 200
valve1.Kv = 2

valve1.info()