class LoadCell:
   def __init__(self, model, carrying, sensitivity, voltage, accuracy_class):
      self.__model =model
      self.__carrying = carrying
      self.__sensitivity = sensitivity
      self.__voltage = voltage
      self.__accuracy_class =accuracy_class
      
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
           print("carrying ValueError")
   
   @property
   def sensitivity(self):
      return self.__sensitivity
   
   @sensitivity.setter
   def sensitivity(self,sensitivity):
       if sensitivity < 0 or sensitivity > 1:
           self.__sensitivity = sensitivity
       else:
           print("Sensitivity ValueError") 
   
   @property
   def voltage(self):
      return self.__voltage
   
   @voltage.setter
   def voltage(self,voltage):
       if voltage < 0:
           self.__voltage = voltage
       else:
           print("Voltage ValueError") 
       
   @property
   def accuracy_class(self):
      return self.__accuracy_class

   @voltage.setter
   def accuracy_class(self,accuracy_class):
       if accuracy_class == "A" or accuracy_class == "B" or accuracy_class == "C" or accuracy_class == "D":
           self.__accuracy_class = accuracy_class
       else:
           print("Accuracy_class ValueError") 

   def __str__(self):
        return(f"Модель: {self.__model}\nГрузоподъемность: {self.__carrying} Кг\nЧувствительность: {self.__sensitivity}\nНапряжение: {self.__voltage}В\nКласс точности: {self.__accuracy_class}")

tenzor1 = LoadCell("Консольный", 100, 0.5, 12,"B")
print(tenzor1)