from django.conf import settings
import requests
import json
import os
import time
from . import on_route, plotting
from .send_to_pi import send_to_pi

'''
Handles directions from Google
'''
def Directions(*args, **kwargs):

    lat_a = kwargs.get("lat_a")
    long_a = kwargs.get("long_a")
    lat_b = kwargs.get("lat_b")
    long_b = kwargs.get("long_b")

    origin = f'{lat_a},{long_a}'
    destination = f'{lat_b},{long_b}'

    result = requests.get(
        'https://maps.googleapis.com/maps/api/directions/json?',
         params={
         'origin': origin,
         'destination': destination,
         "key": settings.GOOGLE_API_KEY
         })

    directions = result.json()

    if directions["status"] == "OK":

        route = directions["routes"][0]["legs"][0]
        origin = route["start_address"]
        destination = route["end_address"]
        distance = route["distance"]["text"]
        duration = route["duration"]["text"]

        steps = [
            [
                s["distance"]["text"],
                s["duration"]["text"],
                s["html_instructions"],

            ]
            for s in route["steps"]]

        timestr = time.strftime("%Y%m%d-%H%M%S")
        
        # save the result to a file
        filepath = os.path.join(settings.MEDIA_ROOT, f'{timestr}.json')
        with open(filepath, 'w') as f:
            json.dump(directions, f)

        #on_route.on_route(directions)
        signals_list = on_route.get_signals_on_route(directions)
        print(f"distance: {distance}, duration: {duration}, len(signals_list)")

        plotting.plot_on_map(signals_list)

        pi_dict = {"distance": distance, "duration": duration}
        pi_string = str(pi_dict)
        send_to_pi(pi_string)
        

    return {
        "origin": origin,
        "destination": destination,
        "distance": distance,
        "duration": duration,
        "steps": steps
    }
