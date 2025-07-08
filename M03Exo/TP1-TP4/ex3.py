# étudiez et executez le code suivant pour le comprendre
# modifiez ensuite la fonction imbriquée pour qu'on puisse changer la température d'une station
# et qu'un subscriber puisse définir une température à partir de laquelle il est notifié

def create_weather_station(localisation):
    observers = []
    seuils = []
    current_temperature = None
    localisation = localisation

    def subscribe(observer, seuil):
        observers.append(observer)
        seuils.append(seuil)

    def change_temp(temperature):
        nonlocal current_temperature
        current_temperature = temperature

        print(f"{localisation} - Changement de température : {temperature}")

        for observer, seuil in zip(observers, seuils):
            if current_temperature >= seuil:
                print(f"Notification envoyée à {observer} : seuil {seuil} atteint")

    def notify():
        for observer in observers:
            print(f"{localisation} : envoi d'un message à {observer} pour lui indiquer la température")
    return subscribe, change_temp, notify


# quimper_subscribe, quimper_notify = create_weather_station("quimper")
# quimper_subscribe("olivier")
# quimper_subscribe("pierre")
# quimper_notify()

quimper_subscribe, quimper_change_temp, quimper_notify = create_weather_station("quimper")
quimper_subscribe("olivier", 30)
quimper_subscribe("pierre", 27)
quimper_subscribe("marie", 29)

quimper_change_temp(24)
quimper_change_temp(30)
quimper_change_temp(32)

"""
quimper_subscribe, quimper_unsubscribe, quimper_change_temp = create_weather_station("quimper")
quimper_subscribe("olivier", 30)
quimper_subscribe("pierre", 27)
quimper_subscribe("marie", 29)

quimper_change_temp(24)
# notifications envoyées

quimper_change_temp(30)
# notifications envoyées

quimper_change_temp(32)
# notifications envoyées
"""