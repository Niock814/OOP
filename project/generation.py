from LoadCell import LoadCell
import datetime
import random



def  generate_test_data (n, **kwargs):
        data_list = []
        models = ["Балочный","S-образный","Мембранный","Колонный","Одноточечный"]
        accuracys = ["C1", "C2", "C3","C4","C5","C6"]
        c_min, c_max = kwargs.get('c_range', (10, 400))
        s_min, s_max = kwargs.get('s_range', (0.1, 10))
        v_min, v_max = kwargs.get('v_range', (5, 24))
        start_time =  datetime.datetime.now()
        delta = datetime.timedelta(seconds=10)

        for i in range(n):
            carrying = random.randint(c_min, c_max)
            sensivity = round(random.uniform(s_min, s_max),1)
            voltage = random.randint(v_min, v_max)
            model = random.choice(models)
            accuracy_class = random.choice(accuracys)
            obj = LoadCell(model, carrying, sensivity, voltage, accuracy_class)
            obj.timestamp = start_time + (delta * i)
            data_list.append(obj)

        return data_list