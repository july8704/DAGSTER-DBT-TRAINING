import csv

import requests
from dagster import (
    DagsterType,
    InputDefinition,
    OutputDefinition,
    pipeline,
    solid,
)


# start_custom_types_marker_0
def is_list_of_dicts(_, value):
    return isinstance(value, list) and all(
        isinstance(element, dict) for element in value
    )


SimpleDataFrame = DagsterType(
    name="SimpleDataFrame",
    type_check_fn=is_list_of_dicts,
    description="A naive representation of a data frame, e.g., as returned by csv.DictReader.",
)

def download_csv():
    response = requests.get("https://docs.dagster.io/assets/cereal.csv")
    lines = response.text.split("\n")
    print("Read {n_lines} lines".format(n_lines=len(lines)))
    return [row for row in csv.DictReader(lines)]

def sort_by_calories(cereals):
    sorted_cereals = sorted(cereals, key=lambda cereal: cereal["calories"])
    print((f'Most caloric cereal: {sorted_cereals[-1]["name"]}'))

def custom_type_pipeline():
    sort_by_calories(download_csv())

custom_type_pipeline()