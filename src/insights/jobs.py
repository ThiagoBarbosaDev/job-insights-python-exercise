from functools import lru_cache
from typing import List, Dict
import csv


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
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = reader
            people = list()
            for person in data:
                job = dict()
                for index, heading in enumerate(header):
                    job[heading] = person[index]
                people.append(job)
            return people
    except ValueError:
        raise NotImplementedError


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    try:
        data = read(path)
        uniqueJobs = list(set(job['job_type'] for job in data))
        return uniqueJobs
    except ValueError:
        raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    try:
        return list(job for job in jobs if job['job_type'] == job_type)
    except ValueError:
        raise ValueError
