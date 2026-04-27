
import os
import json
import click
from datetime import datetime
from usgs import api


def to_coordinates(bounds):
    pass


def to_geojson_feature(entry):

    # TODO: This key may not be present in all datasets.
    pass


def to_geojson(result):
    pass


def explode(coords):
    pass

def get_bbox(f):
    pass


api_key_opt = click.option("--api-key", help="API key returned from USGS servers after logging in.", default=None)
catalog_opt = click.option("--catalog", help="The catalog corresponding to the dataset. One of EE or HDDS).", default=None, type=click.Choice(['EE', 'HDDS']))
dataset_opt = click.option("--dataset", help="The name of a dataset, e.g. landsat_8_c1")
start_date_opt = click.option("--start-date", default=None, help="The start date of a dataset or acquisition")
end_date_opt = click.option("--end-date", default=None, help="The start date of a dataset or acquisition")

@click.group()
def usgs():
    pass

@click.command()
@click.argument("username", envvar='USGS_USERNAME')
@click.argument("token", envvar='USGS_TOKEN')
def cycle_token(username, token):

    pass


@click.command()
@click.argument("dataset")
def dataset_filters(dataset):
    pass


@click.command()
@catalog_opt
@dataset_opt
@start_date_opt
@end_date_opt
def dataset_search(catalog, dataset, start_date, end_date):
    pass


@click.command()
@click.argument("dataset")
@click.argument("scene-ids", nargs=-1)
@api_key_opt
def download_options(dataset, scene_ids, api_key):
    data = api.download_options(dataset, scene_ids)
    click.echo(json.dumps(data))


@click.command()
@click.argument("dataset")
@click.argument("entity_id")
@click.option("--product-id", required=True)
@api_key_opt
def download_request(dataset, entity_id, product_id, api_key):
    pass


@click.command()
@click.argument("username", envvar='USGS_USERNAME')
@click.argument("token", envvar='USGS_TOKEN')
def login(username, token):
    click.echo(api.login(username, token))


@click.command()
def logout():
    click.echo(api.logout())


@click.command()
@click.argument("dataset")
@click.argument("scene-id", nargs=1)
@click.option('--geojson', is_flag=True)
@api_key_opt
def scene_metadata(dataset, scene_id, geojson, api_key):
    pass


@click.command()
@click.argument("dataset")
@click.argument("aoi", default="-", required=False)
@click.option('--max-results', default=5000, type=int)
@click.option('--metadata-type', type=click.Choice(['summary', 'full']))
@click.option("--start-date")
@click.option("--end-date")
@click.option("--lower-left", nargs=2, help="Longitude/latitude specifying the lower left of the search window")
@click.option("--upper-right", nargs=2, help="Longitude/latitude specifying the lower left of the search window")
@click.option("--longitude", type=float)
@click.option("--latitude", type=float)
@click.option("--distance", type=float, help="Radius - in units of meters - used to search around the specified longitude/latitude.", default=100)
@click.option("--where", nargs=2, multiple=True, help="Supply additional search criteria.")
@api_key_opt
def scene_search(
    dataset, aoi, max_results, metadata_type,
    start_date, end_date, lower_left, upper_right,
    longitude, latitude, distance,
    where, api_key):

    pass


usgs.add_command(cycle_token, "cycle-token")
usgs.add_command(dataset_filters, "dataset-filters")
usgs.add_command(download_options, "download-options")
usgs.add_command(download_request, "download-request")
usgs.add_command(dataset_search, "dataset-search")
usgs.add_command(login)
usgs.add_command(logout)
usgs.add_command(scene_metadata, "scene-metadata")
usgs.add_command(scene_search, "scene-search")