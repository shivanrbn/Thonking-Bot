import requests
import json

from igdb import (GAMES_URL,
                  COMPANIES_URL,
                  FRANCHISES_URL,
                  GENRES_URL,
                  KEYWORDS_URL,
                  PEOPLE_URL,
                  PLATFORMS_URL,
                  PLAYER_PERSPECTIVES_URL,
                  PULSES_URL,
                  SERIES_URL,
                  THEMES_URL,
                  )


class CouldNotRetrieveJSONException(Exception):
    pass


def retrieve_from_igdb(get_function):
    def inner_func(*args, **kwargs):
        response = get_function(*args, **kwargs)
        if response.status_code != 200:
            raise CouldNotRetrieveJSONException(response.text)
        return json.loads(response.text)
    return inner_func


class Requester(object):

    def __init__(self, api_key):
        self._headers = {
            'Accept': 'application/json',
            'X-Mashape-Key': api_key
        }

    @retrieve_from_igdb
    def _request_json(self, url, **params):
        self._update_params_with_filters(params)
        return requests.get(url, params=params, headers=self._headers)

    def _update_params_with_filters(self, params):
        filters = params.pop('filters', [])
        if filters:
            try:
                for _filter in filters:
                    params.update(_filter.as_dict())
            except Exception as e:
                raise ValueError("The filters objects must be an instance of igdb.Filter: {}".format(e))

    def get_games(self, fields='*', limit=10, offset=0,
                  order='release_dates.date:desc', search=None, filters=None):
        return self._request_json(GAMES_URL, fields=fields,
                                  limit=limit, offset=offset,
                                  order=order, search=search, filters=filters)

    def get_companies(self, fields='*', limit=10, offset=0, filters=None):
        return self._request_json(COMPANIES_URL, fields=fields,
                                  limit=limit, offset=offset, filters=filters)

    def get_franchises(self, fields='*', filters=None):
        return self._request_json(FRANCHISES_URL, fields=fields, filters=filters)

    def get_genres(self, fields='*', limit=40, filters=None):
        return self._request_json(GENRES_URL, fields=fields, limit=limit, filters=filters)

    def get_keywords(self, fields='*', limit=50, offset=0, filters=None):
        return self._request_json(KEYWORDS_URL, fields=fields,
                                  limit=limit, offset=offset, filters=filters)

    def get_people(self, fields='*', filters=None):
        return self._request_json(PEOPLE_URL, fields=fields, filters=filters)

    def get_platforms(self, fields='*', limit=50, offset=0, filters=None):
        return self._request_json(PLATFORMS_URL, fields=fields,
                                  limit=limit, offset=offset, filters=filters)

    def get_player_perspectives(self, fields='*', filters=None):
        return self._request_json(PLAYER_PERSPECTIVES_URL, fields=fields, filters=filters)

    def get_pulses(self, fields='*', filters=None):
        return self._request_json(PULSES_URL, fields=fields, filters=filters)

    def get_series(self, fields='*', filters=None):
        return self._request_json(SERIES_URL, fields=fields, filters=filters)

    def get_themes(self, fields='*', limit=40, filters=None):
        return self._request_json(THEMES_URL, fields=fields, limit=limit, filters=filters)
