import sys 
import inspect
import logging 
import csv # comma seperated value
import random
from urllib import request # opens the url from the api request
import json # what is used for gettting the info from the url 
import datetime 
import ssl

logging.basicConfig(level = logging.INFO, format = "[{asctime} : {funcName} : {lineno} : {message}]", style = '{' ) # configuring logger
logger = logging.getLogger("EMAILBLAST") # making object called emailblast
logger.info("INITIATING LOGGER") # initiating and checking logger

#getting a random quote from csv file of marvel quotes
def get_random_quote(quotes_file = "quotes.csv"): # telling the code to use the quotes.csv file with marvel quotes
    try:
        logger.info("inside quote func") 
        with open(quotes_file) as csvfile: # using the csv file to get quote and storing it as a key value pair (dictionaries)
                quotes = [{"quote": line[0], # finding quote
                            "author": line[1], # finding author
                            "movie": line[2]} for line in csv.reader(csvfile, delimiter = "|") ] # finding movie and changing the delimiter to a |

        logger.info("about to print quote")
        print(f"Quote is {random.choice(quotes)}") 
        logger.info("printed quote")
        return(random.choice(quotes))    # sending chose quote back                   

    except Exception as error:
        raise error


def get_weather_forecast(coords = {'lat': -36.848461, 'lon': 174.763336}): # auklands geographical coordinates
    try:
        api_key = '8d06b1d290a4f3a70e5d67975695bfd6' # api key
        url = f'https://api.openweathermap.org/data/2.5/forecast?lat={coords["lat"]}&lon={coords["lon"]}&appid={api_key}&units=metric' #url json file is using
        data = json.load(request.urlopen(url)) # getting the info fro the url and stroing it in data - json.load parses json text into a python dictionary

        forecast = {'city': data['city']['name'], # city name
                    'country': data['city']['country'],  # country name
                    'periods': list()} # list to hold forecast data for future periods of time

        for period in data['list'][0:9]:
            forecast['periods'].append({'timestamp': datetime.datetime.fromtimestamp(period['dt']),
                                        'temp': round(period['main']['temp']),
                                        'description': period['weather'][0]['description'].title(),
                                        'icon': f'http://openweathermap.org/img/wn/{period["weather"][0]["icon"]}'})

        return(forecast)

    except Exception as error:
        raise error

def get_twitter_trend():
    pass

def get_wikipedia_article():
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        data = json.load(request.urlopen('https://en.wikipedia.org/api/rest_v1/page/random/summary'))

        return {'title': data['title'],
                'extract': data['extract'],
                'url': data['content_urls']['desktop']['page']}


    except Exception as error:
        raise error

if __name__ == "__main__":
    try:
        print(f"Daily quote")
        logger.info("going inside quote func")
        quote = get_random_quote()

        forecast = get_weather_forecast()

        if forecast:
            print(f'Weather forecast for {forecast["city"]}, {forecast["country"]} is : ')
            for period in forecast['periods']:
                print(f'{period["timestamp"]} | {period["temp"]}°C, | {period["description"]}')

        sydney = {'lat': 33.8688, 'lon': 151.2093}
        forecast = get_weather_forecast(coords = sydney)
        if forecast:
            print(f'Weather forecast for {forecast["city"]}, {forecast["country"]} is : ')
            for period in forecast['periods']:
                print(f'{period["timestamp"]} | {period["temp"]}°C, | {period["description"]}')  

        article = get_wikipedia_article()

        if article:
            print(f'{article["title"]}, {article["url"]}, {article["extract"]}')


    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":D")