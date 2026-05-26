import requests
import logging
from tenacity import retry, stop_after_attempt, wait_exponential

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

BASE_URL = "https://archive-api.open-meteo.com/v1/archive"

# Retry decorator with exponential backoff
@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, max=10))
def ingest_weather_data(start_date: str, end_date:str ) -> dict:

    params = {
        "latitude": 32.7765,
        "longitude": -79.9311,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch",
        "timezone": "America/New_York",
    }

    response = requests.get(BASE_URL, params=params, timeout=240)
    response.raise_for_status()

    data = response.json()

    return data['daily']

