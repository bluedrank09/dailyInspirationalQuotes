import sys
import inspect 
import logging as logger
import dd_content
import datetime

class dailyDigestEmail:

    def __init__(self):
        self.content = {'quote': {'include': True, 'content': dd_content.get_random_quote()},
                        'weather': {'include': True, 'content': dd_content.get_weather_forecast()},
                        'wikipedia': {'include': True, 'content': dd_content.get_wikipedia_article()}}

    def send_email(self):
        pass

    def format_messgae(self):
        today = datetime.date.today()
        text = f"DAILY DIGEST - {today:%B, %d, %Y}"

        if self.content['weather']['include'] and self.content['quote']['content']:
            text += f"MARVEL QUOTE OF THE DAY : "
            text += f'"{self.content["quote"]["content"]["quote"]}" - {self.content["quote"]["content"]["author"]}'

        if self.content['weather']['include'] and self.content['weather']['content']:
            text+= f"FORECAST FOR TODAY : {self.content['weather']['content']['city']}, {self.content['weather']['content']['country']}"
            for forecast in self.content['weather']['content']['periods']:
                text+= f'{forecast["timestamp"]:%d-%B-%Y} - {forecast["temp"]}\u00B0C | {forecast["description"]}'

        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            text+= "RANDOM WIKIPEDIA ARTICLE : "
            text+= f'{self.content["wikipedia"]["content"]["title"]} {self.content["wikipedia"]["content"]["extract"]}'

            
    print(f"SUCESS")

if __name__ == "__main__":
    try:
        pass

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":D")