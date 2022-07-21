import requests
import xml.etree.ElementTree as ET

# получаем курс рубля из цб РФ

usd_rate = float(
    ET.fromstring(
        requests.get('https://www.cbr.ru/scripts/XML_daily.asp').text)
    .find("./Valute[CharCode='USD']/Value")
    .text.replace(",", ".")  # заменяем запятые на точки
)
