import random
import datetime
import csv
import json
from abc import ABC, abstractmethod


class equipment:
    def __init__(self, model):
        self.__model = model
        self.__timestamp = datetime.datetime.now()
    
    @property
    def model(self):
        return self.__model
    
    @property
    def timestamp(self):
        return self.__timestamp
    
    @timestamp.setter
    def timestamp(self, value):
        """Сеттер для timestamp"""
        if isinstance(value, datetime.datetime):
            self._timestamp = value
        else:
            raise ValueError("Timestamp must be datetime object")
        
    @abstractmethod
    def read_value(self):
        pass
        
    @property
    @abstractmethod
    def unit(self):       
        pass
    
    def __eq__(self, other):
       if not isinstance(other, equipment): return NotImplemented

       return self.model==other.model
    

    def to_dict(self):
        
        return {
            "model": self.__model,
            "time": self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }

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

    def __str__(self):
        return f"Модель: {self.__model}"
    
    def description(self):

        return f"{self.__class__.__name__}: {self.__model}, единица измерения: {self.unit}"