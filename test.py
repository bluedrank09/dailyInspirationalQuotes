import sys
import inspect
import logging
import csv
import random

logging.basicConfig(level = logging.INFO, format = "[{asctime} : {funcName} : {lineno} : {message}]", style = '{' )
logger = logging.getLogger("EMAILBLAST")
logger.info("INITIATING LOGGER")

def get_random_quote(quotes_file = "quotes.csv"):
    try:
        logger.info("inside quote func")
        with open(quotes_file) as csvfile:
                quotes = [{'quote': line[0], 
                            'author': line[1], 
                            'movie': line[2]} for line in csv.reader(csvfile, delimiter = "|")] 

        logger.info("about to print quote")
        # print(f"Quote is {random.choice(quotes)}")
        logger.info("printed quote")
        return(random.choice(quotes))                       

    except Exception as error:
        raise error


if __name__ == "__main__":
    try:
        logger.info("going inside quote func")
        quote = get_random_quote()
        print(f'Random Quote Is {quote["quote"]}, {quote["author"]}, {quote["movie"]}')

    except Exception as error:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logger.info(f"{inspect.stack()[0][3]} : {exc_tb.tb_lineno} : {error}")

    finally:
        print(f":D")