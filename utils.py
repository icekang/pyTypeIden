import pickle
from datetime import datetime, timedelta


def dictToFile(dictionary: dict, filename=datetime.now().strftime('%Y/%m/%d-%H:%M:%S')) -> None:
    with open('./data/{filename}'.format(filename=filename), 'wb') as f:
        pickle.dump(dictionary, f)


def fileToDict(filename: str) -> dict:
    with open('./data/{filename}'.format(filename=filename), 'rb') as f:
        d = pickle.load(f)
    return d


def timedeltaToMs(td: timedelta) -> float:
    secs = td.seconds
    microsecs = td.microseconds
    return microsecs*1000 + secs/1000
