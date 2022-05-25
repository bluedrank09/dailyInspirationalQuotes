import sys
import inspect 
import logging as logger
import dd_content
import datetime
import ssl
from email.message import EmailMessage
import smtplib


class dailyDigestEmail:

    def __init__(self):
        self.content = {'quote': {'include': True, 'content': dd_content.get_random_quote()},
                        'weather': {'include': True, 'content': dd_content.get_weather_forecast()},
                        'wikipedia': {'include': True, 'content': dd_content.get_wikipedia_article()}}

        self.recipients_list = ['mayababu73@gmail.com']

        self.sender_credentials = ['email' : 'yeetusbro09@gmail.com'
                                    'password' : 'J0tunh#im']

    def send_the_email(self):
        msg = EmailMessage()
        today = datetime.date.today()
        msg['Subject'] = f"DAILY DIGEST "
        msg["From"] = self.sender_credentials['email']
        msg['To'] = ','.join(self.recipients_list)

        



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
                {forecast['timestamp'].today:%B, %d, %Y}
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
        return {'text': text, 'html': html}

if __name__ == "__main__":
    try:
        email = dailyDigestEmail()

        ##### test format_message() #####
        print('Testing email body generation : ')
        message = email.format_message()

        # print Plaintext and HTML messages
        print('Normal text email body is...')
        print(message['text'])
        print('------------------------------------------------------------')
        print('HTML email body is : ')
        print(message['html'])

        # save Plaintext and HTML messages to file
        with open('message_text.txt', 'w', encoding='utf-8') as f:
            f.write(message['text'])
        with open('message_html.html', 'w', encoding='utf-8') as f:
            f.write(message['html'])

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":D")



        