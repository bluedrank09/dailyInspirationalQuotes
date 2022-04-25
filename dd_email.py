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

    def format_message(self):
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

        today = datetime.date.today()
        html = f"""<html>
        <body>
        <center>
            <h1>Daily Digest - {today:%B, %d, %Y}</h1>
            """

        if self.content['quote']['include'] and self.content['quote']['content']:
            html += f"""
        <h2>Quote of the Day</h2>
        <i>"{self.content['quote']['content']['quote']}"</i> - {self.content['quote']['content']['author']}
        """

        if self.content['weather']['include'] and self.content['weather']['content']:
            html += f"""
        <h2>Forecast for {self.content['weather']['content']['city']}, {self.content['weather']['content']['country']}</h2> 
        <table>
                    """

        for forecast in self.content['weather']['content']['periods']:
            html += f"""
        <tr>
            <td>
                {forecast['timestamp'].strftime('%d %b %H%M')}
            </td>
            <td>
                <img src="{forecast['icon']}">
            </td>
            <td>
                {forecast['temp']}\u00B0C | {forecast['description']}
            </td>
        </tr>
                    """               

        html += """
        </table>
                """

        if self.content['wikipedia']['include'] and self.content['wikipedia']['content']:
            html += f"""
        <h2>Daily Random Learning</h2>
        <h3><a href="{self.content['wikipedia']['content']['url']}">{self.content['wikipedia']['content']['title']}</a></h3>
        <table width="800">
            <tr>
                <td>{self.content['wikipedia']['content']['extract']}</td>
            </tr>
        </table>
                    """
                    
        html += """
    </center>
    </body>
</html>
                """


if __name__ == "__main__":
    try:
        pass

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":D")



        