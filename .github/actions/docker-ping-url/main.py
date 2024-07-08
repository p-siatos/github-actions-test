import requests as req
from time import sleep
import os

def run():
    url = os.getenv("INPUT_URL")
    delay = int(os.getenv("INPUT_DELAY"))
    max_trials = int(os.getenv("INPUT_MAX_TRIALS"))
    url_reachable = ping_url(url, delay, max_trials)
    
    if not url_reachable:
        raise Exception(f"Website {url} is malformed or unreachable")
    
    print(f"website {url} is reachable")


def ping_url(url, delay, max_trials):
    num_of_trials = 0
    while num_of_trials < max_trials:
        try:
            res = req.get(url)
            if res.status_code == 200:
                print(f"Site {url} is reachable")
                return True
        except req.ConnectionError:
            print(f'Website {url} is  unreachable. Retrying in {delay} seconds...')
            sleep(delay)
            num_of_trials += 1
        except req.exceptions.MissingSchema:
            print(f"Invalid Url format {url}")
            return False

    return False


if __name__ == "__main__":
    run()