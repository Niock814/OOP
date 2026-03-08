import json
import csv
from LoadCell import LoadCell


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