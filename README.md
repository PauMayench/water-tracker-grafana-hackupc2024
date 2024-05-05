<h1>
  <img src="https://github.com/PauMayench/water-tracker-grafana-hackupc2024/assets/120923489/242ac4e3-1302-46a7-a907-ca4a3c5e1640" alt="Logo" style="height:50px; vertical-align:middle;">
  HackUPC 2024 -- Water Tracker
</h1>



## Introduction


This Water Tracker project aims to raise awareness about the water consumption of the population. 
Our system uses the microcontroller ESP23 connected to many sensors to monitor the water levels of five lakes and personal water usage, displaying the data through Grafana for easy visualization and monitoring. The system also alerts users based on predefined consumption and drought conditions.

<img src="https://github.com/PauMayench/water-tracker-grafana-hackupc2024/assets/120923489/6d01d61f-aee7-4ef5-8d9b-a7359a84c24c" width="100%" alt="diagram_readme">

## Features

### Lake Water Level Monitoring
- Real-time tracking of water levels in five major lakes using ESP32 equipped with (water level sensors) in this case were represented by 5 potentiometers.
- Data visualization for easy understanding of water trends and immediate status.

### Personal Water Consumption Tracking
- Automated monitoring of your home water usage to promote responsible water consumption.
- Notifications for excessive use, like the one the government establishes that is recommended on drought seasons (100 liters per day per person).

### Weather Monitoring
- Integration of a home meteorological station to provide real-time data on local weather conditions.
- Helps users understand the impact of weather on water levels and personal water usage.

### Alerts and Notifications
- Customizable alerts for low lake levels, indicating potential drought conditions.
- Usage alerts to inform users when they exceed specified water consumption thresholds.

### Data Visualization with Grafana
- Customizable Grafana dashboards to display all collected data coherently.
- Features like graphing, zooming, and time range adjustments for detailed analysis.




## Project Build

### Materials used for the project

- ESP32 microcontroller 
- Sensors for water level detection (we used potentiometers for the simulation)
- Sensors for humidity, temperature, and a photoreceptor
- Grafana environment

<img src="https://github.com/PauMayench/water-tracker-grafana-hackupc2024/assets/120923489/f2009250-5632-4395-944e-a9ca09d4972f" width="70%" alt="diagram_readme">

## How it works

The ESP32 represents several different microcontrollers, as we had only access to one. 
We can separate it in two main parts, the first one is that we have a microcontroller for each lake that we wish to keep track, in our case they were these five:

- Pantà de sau     
- Pantà de la Baells 
- Pantà de Rialb       
- Pantà de Canelles  
- Pantà de Susqueda  

The second main part consists of a microcontroller on the user's home that tracks and displays temperature humidity and light information. The main feature is that it also tracks the user's water consumption habits, and it displays it to them.

Each of these microcontrollers send through real time data to the server where they get processed, ideally by Wi-Fi. In reality, we connected our microcontroller to the laptop through cable, talking with the serial port with python and then communicating through the API, on our p.

We represent the users' consumption as some normal value, when we press the button, it represents the user wasting water than it should and that is the increment that can be seen on the consumption graphic. The main goal is to war the user of its habits and also raise awareness about our precious resource.


### Connections ESP32-PC, PC-GrafanaCloud

The ESP32 is connected to our computer through a USB cable, using serial communication. All the
computer-side programming is done in python3. Our main routine reads the serial port from the ESP32
and converts the data to a json format. To push the data to the Grafana Cloud Dashboard, we have built
a class that handles the data parsing and POST requests to the HTTP API.



## Execution

    For the small version of this ambitious project we need to first load the program_esp32.ino into the ESP23.
    Then we need to make all the connections to the ESP23:
        P4  ->   Potentiometer 1
        P2  ->   Potentiometer 2
        P34 ->   Potentiometer 3
        P35 ->   Potentiometer 4
        P32 ->   Potentiometer 4
        P33 ->  Photosensor
        P26 ->  button      
        P16 ->  Blue led   (optional)
        P17 ->  Red led   (optional)
    After that we can connect the ESP23 through USB to the computer

    Make sure to create a .credentials.json file with the contents:

    {
    "API_ID": 1111111,
    "API_TOKEN": "EXAMPLEdojc398c4nu92384ur...0c29n029un4t0923unt0vnu42t5==",
    }

    And also add your endpoint to the ENDPOINT variable of the main.py

    Make sure you have all the dependencies listed on requirements.txt
    Then you can execute the main script with:
    `python3 main.py`

    At this point all the data should be flowing on real tie to the Grafana dashboard, displaying all the info in real time


## Improvements
We could add the feature of sending a message to the ESP23 from the dashboard when an aletr happens and alerting the user.

We could also implement the project with more Microcontrolers and test it out creating a more robust way to test and see the viability of the abitious big project.

    

## Authors 
Pau Mayench, Xavi Medina, Ferriol Falip & Jordi Otal

