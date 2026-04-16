import requests
import logging
from utils.config import HEADERS
import time

logger = logging.getLogger(__name__)


class BaseAPI:

    def send_request(self, method, url, params=None, data=None, retries=3, timeout=5):
        attempt = 0
        while attempt < retries:
            try:
                logger.info(f"\n--- API CALL START ---")
                logger.info(f"Attempt {attempt+1}")
                logger.info(f"Method: {method}")
                logger.info(f"URL: {url}")

                if params:
                    logger.info(f"Query Params: {params}")

                if data:
                    logger.info(f"Request Body (Payload): {data}")

                response = requests.request(
                    method=method,
                    url=url,
                    headers=HEADERS,
                    params=params,
                    json=data,
                    timeout=timeout
                )

                logger.info(f"Status Code: {response.status_code}")
                logger.info(f"--- API CALL END ---\n")

                return response

            except requests.exceptions.Timeout:
                logger.error("Request timed out")
            except requests.exceptions.RequestException as e:
                logger.error(f"Request failed: {e}")

            attempt += 1
            time.sleep(1)

        raise Exception(f"Failed after {retries} attempts")