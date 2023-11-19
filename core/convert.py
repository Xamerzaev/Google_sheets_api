import requests
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_usd_rate():
    try:
        response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")

        if response.status_code == 200:
            root = ET.fromstring(response.text)
            usd_value = root.find("./Valute[CharCode='USD']/Value").text.replace(",", ".")
            return float(usd_value)
        else:
            logger.error(f"Failed to retrieve data. Status code: {response.status_code}")
            return None

    except ET.ParseError as e:
        logger.error(f"Error parsing XML: {str(e)}")
        return None

    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        return None


if __name__ == "__main__":
    usd_rate = get_usd_rate()

    if usd_rate is not None:
        print(f"The USD to RUB exchange rate is: {usd_rate}")
    else:
        print("Failed to retrieve the exchange rate.")
