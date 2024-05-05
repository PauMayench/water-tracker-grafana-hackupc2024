import serial.tools.list_ports
import math
import pprint
import random

def treat_data(data):
    returnData = {}


    conversion_name = {
        "Sensor_temperatura:" : "temperature",
        "Sensor_humitat:" : "humidity",
        "Potenciometre1:" : "level_lake1",
        "Potenciometre2:" : "level_lake2",
        "Potenciometre3:" : "level_lake3",
        "Potenciometre4:" : "level_lake4",
        "Potenciometre5:" : "level_lake5",
        "Sensor_de_llum:" : "lightness",
        "consumint_molt:" : "consum",
        }


    for key, value in data.items():
        try:
            if "lake" in conversion_name[key]:
                returnData[conversion_name[key]] = get_percentage_volume_lake(value, conversion_name[key]) 
            elif "lightness" == conversion_name[key]:
                returnData[conversion_name[key]] = 100 - round(float(value)*100, 1)
            elif "consum" == conversion_name[key]:
                print("c ->" + value)
                if int(value) == 1:
                    returnData[conversion_name[key]] = random.randint(10,20)
                else:   
                    returnData[conversion_name[key]] = random.randint(3,10)

            else:
                returnData[conversion_name[key]] = float(value)

        except:
            print(key + "not found")

    return returnData






def select_port(): 
    ports = serial.tools.list_ports.comports()
    print("Choose the port (input 1 for the firrst port)")
    for i, port in enumerate(ports):
        print(f"{i+1}: {port.device}")
    index = int(input(""))-1
    return ports[index].device

#/dev/ttyUSB0


def get_percentage_volume_lake(percent_depth, lake_name):
    # we assume that a lake has a conical form
    percent_depth = float(percent_depth)
    radius = 100 # default lake
    depth = 30   #default lake
    if lake_name == "level_lake1": #"pantà de sau "
        radius = 1.32  # meters
        depth = 83    # meters
    elif lake_name == "level_lake2": # "Pantà de la Baells"
        radius = 1.01
        depth = 102.35    
    elif lake_name == "level_lake3": #"pantà de Rialb"
        radius = 1.95
        depth = 101    
    elif lake_name == "level_lake4": #"pantà de Canelles"
        radius = 2.08
        depth = 150    
    elif lake_name == "level_lake5": #"pantà de Susqueda"
        radius = 1.284
        depth = 135    


    h_new = percent_depth * depth
    r_new = percent_depth * radius
    volume_new = 0.33333 * 3.1415 * r_new *r_new * h_new
    volume_total = 0.33333 * 3.1415 * radius *radius * depth

    return round(volume_new*100/volume_total,1)



