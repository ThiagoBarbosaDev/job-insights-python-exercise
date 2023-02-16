from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    jobs = open(path, mode="r")
    print(jobs.read())
    print("entrei")
    jobs.close()
    raise NotImplementedError


read("data/jobs.csv")

