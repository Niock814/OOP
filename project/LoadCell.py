import random
import datetime

class LoadCell:
   def __init__(self, model, carrying, sensitivity, voltage, accuracy_class):
      self.__model =model
      self.__carrying = carrying
      self.__sensitivity = sensitivity
      self.__voltage = voltage
      self.__accuracy_class =accuracy_class
      self.__current_load = 0.0
      self.__timestamp = datetime.datetime.now()
      

   @property
   def current_load(self):
         return self.__current_load
   @property
   def model(self):
         return self.__model
   
   @property
   def carrying(self):
      return self.__carrying
   
   @carrying.setter
   def carrying(self,carrying):
       if carrying < 0:
           self.__carrying = carrying
       else:
           return ValueError("carrying ValueError")
   
   @property
   def sensitivity(self):
      return self.__sensitivity
   
   @sensitivity.setter
   def sensitivity(self,sensitivity):
       if sensitivity < 0:
           self.__sensitivity = sensitivity
       else:
           return ValueError("Sensitivity ValueError") 
   
   @property
   def voltage(self):
      return self.__voltage
   
   @voltage.setter
   def voltage(self,voltage):
       if voltage < 0:
           self.__voltage = voltage
       else:
           return ValueError("Voltage ValueError") 
       
   @property
   def accuracy_class(self):
      return self.__accuracy_class

   @voltage.setter
   def accuracy_class(self,accuracy_class):
       if accuracy_class == "C1" or accuracy_class == "C2" or accuracy_class == "C3" or accuracy_class == "C4" or accuracy_class == "C5" or accuracy_class == "C6":
           self.__accuracy_class = accuracy_class
       else:
           ValueError("Accuracy_class ValueError") 

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
        return(f"Модель: {self.__model}\nГрузоподъемность: {self.__carrying} Кг\nЧувствительность: {self.__sensitivity} мВ/В\nНапряжение: {self.__voltage}В\nКласс точности: {self.__accuracy_class}\nТочность: {self.accuracy()}\nМаксимальный выход:{self.max_output()} мВ\n")
   
   def __repr__(self):
        return (f"LoadCell(model={self.__model!r}, "
        f"carrying={self.__carrying}, "
        f"sensitivity={self.__sensitivity}, "
        f"voltage={self.__voltage}, "
        f"accuracy_class={self.__accuracy_class!r})")
   
   def to_dict(self):
    return {
    "model": self.__model,
    "carrying": self.__carrying,
    "sensitivity": self.__sensitivity,
    "voltage": self.__voltage,
    "accuracy_class": self.__accuracy_class,
    "time": self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')}
   
   def __eq__(self, other):
       if not isinstance(other, LoadCell): return NotImplemented

       return self.model==other.model
   

   def __add__(self, other):
       if not isinstance(other, LoadCell): return NotImplemented

       return LoadCell(
           self.model, 
           self.carrying + other.carrying,
           self.sensitivity + other.sensitivity,
           self.voltage + other.voltage,
           self.accuracy_class
       )
   
   def max_output(self):
       return round(self.__sensitivity*self.voltage,2)
   
   def accuracy(self):
       if self.__accuracy_class== "C1": return 0.05
       if self.__accuracy_class== "C2": return 0.03
       if self.__accuracy_class== "C3": return 0.02
       if self.__accuracy_class== "C4": return 0.015
       if self.__accuracy_class== "C5": return 0.012
       if self.__accuracy_class== "C6": return 0.008
       else: return ValueError("Accuracy ValueError")


   def add_load(self, Load):

        if Load < 0:
            return ValueError("Load ValueError")
        
        new_load = self.__current_load + Load
        if new_load > self.__carrying:
            return ValueError("more than load capacity")
        else:
            self.__current_load = new_load      

   def weight(self):
       measured_value = self.__current_load
       return measured_value
   
   def tare(self):

        self.__current_load = 0.0   
       

tenzor2 = LoadCell("Консольный", 100, 0.5, 12,"C1")

tenzor2.add_load(20)
tenzor2.add_load(60)

print(tenzor2.weight)