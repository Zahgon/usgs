import json
import math
from collections import defaultdict
from usgs import CATALOG_NODES, USGSDependencyRequired


def dataset_filters(dataset):
    """
    This request is used to return the metadata filter fields for the specified
    dataset. These values can be used as additional criteria when submitting search
    and hit queries.

    :param str dataset:
    """
    pass

def download_options(dataset, entity_ids):
    """
    The download options request is used to discover downloadable products for
    each dataset. If a download is marked as not available, an order must be
    placed to generate that product.

    :param str dataset:
    :param str entity_ids:
    """

    payload = {
        "datasetName": dataset,
        "entityIds": entity_ids
    }

    return json.dumps(payload)

def dataset_download_options(dataset):
    """
    The dataset download options request is used to discover downloadable
    products for a specified dataset. Unlike the `download_options` request,
    this does not check product availability.

    :param str dataset: Used to identify the which dataset to return results for.
    """
    pass

def download_request(dataset, entity_id, product_id):
    """
    The use of this request will be to obtain valid data download URLs.

    :param str dataset:
    :param str entity_id:
    :param str product_id:
    """
    pass

def dataset_search(dataset, catalog, start_date=None, end_date=None, ll=None, ur=None):
    """
    This method is used to find datasets available for searching. By passing only
    an API Key, all available datasets are returned. Additional parameters such
    as temporal range and spatial bounding box can be used to find datasets that
    provide more specific data. The dataset name parameter can be used to limit
    the results based on matching the supplied value against the public dataset
    name with assumed wildcards at the beginning and end.

    :param str dataset:
    :param str catalog:
    :param start_date:
        Used for searching scene acquisition - will accept anything
        that the PHP strtotime function can understand

    :param end_date:
        Used for searching scene acquisition - will accept anything
        that the PHP strtotime function can understand

    :param ll:
        Lower left corner of an AOI bounding box - in decimal form
        Longitude/Latitude dictionary

        e.g. { "longitude": 0.0, "latitude": 0.0 }

    :param ur:
        Upper right corner of an AOI bounding box - in decimal form
        Longitude/Latitude dictionary

        e.g. { "longitude": 0.0, "latitude": 0.0 }
    """
    pass

def login(username, token):
    """
    Upon a successful login, an API key will be returned. This key will be active
    for two hours and should be destroyed upon final use of the service by calling
    the logout method.

    :param str username:
    :param str token:
    """
    payload = {
        "username": username,
        "token": token
    }

    return json.dumps(payload)


def scene_metadata(dataset, entity_id):
    """
    The use of the metadata request is intended for those who have
    acquired scene IDs from a different source. It will return the
    same metadata that is available via the search request.

    :param dataset:
    :param entity_id:
    """
    pass


def great_circle_dist(lat, lng, dist):
    pass

def scene_search(
    dataset, max_results=None, metadata_type=None, start_date=None,
    end_date=None, ll=None, ur=None,
    lat=None, lng=None, distance=100,
    where=None, starting_number=None):

    pass
