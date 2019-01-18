from collections import namedtuple

__version__ = "0.1.0"

BASE_API_URL = 'https://igdbcom-internet-game-database-v1.p.mashape.com/{}'

GAMES_URL = BASE_API_URL.format('games/')
COMPANIES_URL = BASE_API_URL.format('companies/')
FRANCHISES_URL = BASE_API_URL.format('franchises/')
GENRES_URL = BASE_API_URL.format('genres/')
KEYWORDS_URL = BASE_API_URL.format('keywords/')
PEOPLE_URL = BASE_API_URL.format('people/')
PLATFORMS_URL = BASE_API_URL.format('platforms/')
PLAYER_PERSPECTIVES_URL = BASE_API_URL.format('player_perspectives/')
PULSES_URL = BASE_API_URL.format('pulses/')
SERIES_URL = BASE_API_URL.format('collections/')
THEMES_URL = BASE_API_URL.format('themes/')


class Filter(namedtuple('filter', 'field, operator, value')):

    def as_dict(self):
        return {'filter[{}][{}]'.format(self.field, self.operator): self.value}
