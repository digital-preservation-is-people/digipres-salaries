#!/usr/bin/env python3
# coding: UTF-8

"""Transform Vacancies.

Take the vacancies pages downloaded from the DPC website and convert into a
salaries listing CSV.
"""

import datetime
import os

from bs4 import BeautifulSoup, element


data = []


def convert_date(date):
    """Convert the date to something sortable.

    Example from web site: "23 August 2017" will become 2017-08-23.
    """
    return datetime.datetime.strptime(date, "%d %B %Y").date()


def make_csv(job):
    """Construct a line for a CSV."""
    title = None
    date = "Not listed"
    location = "Not listed"
    salary = "Not listed"
    for x in job.contents:
        if isinstance(x, element.Tag):
            for y in x.contents:
                if isinstance(y, element.Tag):
                    if y.name == "a" and not y.get("class"):
                        title = y.text.strip()
                    if y.name == "p":
                        if "date" in y.attrs.get("class"):
                            date = convert_date(y.text.strip())
                        if "location" in y.attrs.get("class"):
                            location = y.text.strip()
                        if "salary" in y.attrs.get("class"):
                            salary = y.text.strip()
    csv_out = '"{}","{}","{}","{}"\n'.format(date, title, location, salary)
    data.append(csv_out)


def main():
    """Primary entry point for script."""
    csv_out = '"Date","Title","Location","Salary"\n'
    data.append(csv_out)
    pages_dir = "pages"
    data_dir = "data"
    data_csv = "digital_preservation_salaries.csv"
    for file in os.listdir(pages_dir):
        path_ = os.path.join(pages_dir, file)
        with open(path_, "rb") as htm:
            source_code = htm.read()
            soup = BeautifulSoup(source_code, features="lxml")
            jobs = soup.find_all("div", {"class": "news listing"})
            for job in jobs:
                make_csv(job)
    salaries_file = os.path.join(data_dir, data_csv)
    with open(salaries_file, "w") as csv_file:
        for count, datum in enumerate(data):
            csv_file.write(datum)
        print("{} lines of data output".format(count))


if __name__ == "__main__":
    main()
