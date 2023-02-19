from typing import Union, List, Dict
from src.insights.jobs import read
# from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    try:
        return max(list(
                    int(job['max_salary'])
                    for job in read(path)
                    if job['max_salary'].isnumeric()
                    ))
    except TypeError:
        raise TypeError
    except ValueError:
        raise ValueError


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    try:
        return min(list(
                    int(job['min_salary'])
                    for job in read(path)
                    if job['min_salary'].isnumeric()
                    ))
    except TypeError:
        raise TypeError
    except ValueError:
        raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        is_not_valid = any([
            job.get('min_salary') is None,
            job.get('max_salary') is None,
            salary is None,
            not str(job.get('min_salary')).isdigit(),
            not str(job.get('max_salary')).isdigit(),
            not str(salary).isdigit() and not isinstance(salary, int),
        ])
        # pergunta: se eu elevo essa comparação me lança um erro de tipo, o any
        # não deveria ser um short circuit?
        # pergunta2: um or não deveria aumentar complexidade? não aumenta
        if is_not_valid or job['min_salary'] > job['max_salary']:
            raise ValueError
        elif int(salary) in range(job['min_salary'], job['max_salary'] + 1):
            return True

        return False

    except ValueError:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError


job = {'max_salary': 1500, 'min_salary': 0}


salary = -1


print(matches_salary_range(job, salary))
