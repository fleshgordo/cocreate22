# some helper functions for panda wrangling

from datetime import datetime
pd.set_option("display.max_colwidth", None)
pd.set_option('display.max_rows', None, 'display.max_columns', None)

def fetchURL(url, outputfile, html=False):
    """Fetches url and writes result into outputfile

    Keyword arguments:
    :param str url: api url
    :param str outputfile: folder/file.json
    :param bool html: set to True if expected response is html 

    Return:
    :return dict JSON response
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 7.1.1; Android SDK built for x86_64 Build/NYC; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36",
        "x-at-application": "Android;25;11081",
        "content-type": "application/vnd.api+json; charset=utf-8",
        "host": "animaltracker.app",
        "x-requested-with": "com.mpio.movebank",
        "accept": "application/vnd.api+json; charset=utf-8",
    }
    if html != True:
        response = requests.get(url, headers=headers)
        data = response.json()
        print(json.dumps(data, indent=2))
        with open(outputfile, "w+") as f:
            json.dump(data, f)
        return data
    else:
        response = requests.get(url, headers=headers)
        with open(outputfile, "w+") as f:
            f.write(response.text)
        return response

def dump_json_to_pd(_file):
    print("loading file: " + _file)
    with open(_file) as json_data:
        data = json.load(json_data)
        df = pd.json_normalize(data["data"])
        return df