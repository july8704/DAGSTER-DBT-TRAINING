import requests
import csv
from dagster import execute_pipeline, pipeline, solid

@solid(config_schema={"url": str})
def download_csv(context):
    response = requests.get(context.solid_config["url"])
    lines = response.text.split("\n")
    return [row for row in csv.DictReader(lines)]

@solid
def find_sugariest (context, cereals):
    sorted_by_sugar = sorted(cereals, key=lambda cereal: cereal["sugars"])
    context.log.info (f'{sorted_by_sugar[-1]["name"]} is the sugariest cereal')

@solid
def find_highest_calorie_cereal(cereals):
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["calories"])
    )
    return sorted_cereals[-1]["name"]

@solid
def find_highest_protein_cereal(cereals):
    sorted_cereals = list(
        sorted(cereals, key=lambda cereal: cereal["protein"])
    )
    return sorted_cereals[-1]["name"]

@solid
def sort_by_calories(context, cereals):
    sorted_cereals = sorted(
        cereals, key=lambda cereal: int(cereal["calories"])
    )

    context.log.info(f'Most caloric cereal: {sorted_cereals[-1]["name"]}')

@solid
def display_results(context, most_calories, most_protein):
    context.log.info(f"Most caloric cereal: {most_calories}")
    context.log.info(f"Most protein-rich cereal: {most_protein}")


@pipeline
def configurable_pipeline():
    sort_by_calories(download_csv())

### end_pipeline_marker

if __name__ == "__main__":
    #start_run_config_marker
    run_config = {
        "solids": {
            "download_csv": {
                "config": {"url": "https://docs.dagster.io/assets/cereal.csv"}
            }
        }
    }
    # end_run_config_marker
    # start_execute_marker
    result = execute_pipeline(configurable_pipeline, run_config=run_config)
    # end_execute_marker
    assert result.success