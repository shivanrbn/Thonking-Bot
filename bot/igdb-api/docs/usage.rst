=====
Usage and Examples
=====
First you need an api key. Please visit https://market.mashape.com/igdbcom/internet-game-database to get it.

To use igdb-api::

    >> from igdb.requester import Requester
    >> api_key = 'sk2aWPgu1SmshudWmsdsdsfsgfsdfsH4gb9Hp1pWaUEjsnSl1Wo4SIsYri'
    >> req = Requester(api_key)

Games
--------------
::

    >> req.get_games(fields='*', limit=10, offset=0, order='release_dates.date:desc', search='Crysis')[1]
    >> {'aggregated_rating': 73.55555555555556,
        'category': 0,
        'collection': 36,
        'cover': {'cloudinary_id': 'ql2wkpjr0wr8s42qnd9o',
                  'height': 1964,
                  'width': 1530},
        'created_at': 1345474459983,
        'developers': [122, 158],
        'esrb': {'rating': 6,
                 'synopsis': 'This is a first-person shooter in which players assume '
                             'the role of a soldier who battles an evil corporation '
                             'and must defend Earth from alien invasion. Players use '
                             'handguns, machine guns, rocket launchers, and '
                             'futuristic weapons to kill Ceph aliens and human '
                             'soldiers. Players can also engage in close-up '
                             "hand-to-hand combat: slicing enemies' throats, breaking "
                             'their necks. The frenetic combat includes realistic '
                             'gunfire, screams of pain, and frequent explosions. '
                             'Characters emit large splashes of blood when shot or '
                             'stabbed; bloodstains can be seen on the ground. The '
                             'words “f**k” and “sh*t” can be heard in the dialogue.'},
        'game_engines': [25],
        'genres': [5, 31],
        'id': 1268,
        'keywords': [132, 453, 466, 1025, 1917, 2210],
        'name': 'Crysis 3',
        'pegi': {'rating': 4,
                 'synopsis': 'The content of this game is suitable for persons aged '
                             '16 years and over only.\n'
                             'It contains: Realistic looking violence - - Strong '
                             'language\n'
                             'This game allows the player to interact with other '
                             'players ONLINE'},
        'publishers': [1],
        'rating': 78.43730001427213,
        'rating_count': 42,
        'release_dates': [{'category': 0, 'date': 1361232000000, 'platform': 6},
                          {'category': 0, 'date': 1361232000000, 'platform': 12},
                          {'category': 0, 'date': 1361232000000, 'platform': 9}],
        'screenshots': [{'cloudinary_id': 'w4wtnrsi7adlgqdrcquh',
                         'height': 360,
                         'width': 640},
                        {'cloudinary_id': 'vdc5hsctsutblkjbdhux',
                         'height': 1080,
                         'width': 1920},
                        {'cloudinary_id': 'hb9udiacxii5dezi2jsa',
                         'height': 360,
                         'width': 640},
                        {'cloudinary_id': 'ldrntvvj3rn6snpke6bd',
                         'height': 360,
                         'width': 640},
                        {'cloudinary_id': 'ria78seajdtfopxhlkjr',
                         'height': 360,
                         'width': 640}],
        'slug': 'crysis-3',
        'storyline': 'Return to the fight as Prophet, the Nanosuit soldier on a quest '
                     'to rediscover his humanity. Adapt on the fly with the stealth '
                     'and armor abilities of your unique Nanosuit as you battle '
                     'through the seven wonders of New York’s Liberty Dome. Unleash '
                     'the firepower of your all-new, Predator bow and alien weaponry '
                     'to hunt both human and alien enemies.',
        'summary': 'The award-winning developer Crytek is back with Crysis 3, the '
                   'first blockbuster shooter of 2013! Crysis 3 is the ultimate '
                   'sandbox shooter, realized in the stunning visuals only Crytek and '
                   'the latest version of CryENGINE can deliver. Available now on '
                   'Xbox 360, PlayStation 3, and PC.',
        'themes': [23, 18],
        'updated_at': 1470897659310,
        'url': 'https://www.igdb.com/games/crysis-3',
        'videos': [{'name': 'The Hunt Is On Trailer', 'video_id': 'lAOaKmuavsQ'}]}

Companies
--------------
::

    >> req.get_companies(fields='*', limit=10, offset=0)[1]
    >> {'change_date_category': 7,
        'created_at': 1466618242964,
        'developed': [13046],
        'id': 10172,
        'name': 'Source the Software House',
        'slug': 'source-the-software-house',
        'start_date_category': 7,
        'updated_at': 1466630360982,
        'url': 'https://www.igdb.com/companies/source-the-software-house'}

Franchises
--------------
::

    >> req.get_franchises(fields='*')[1]
    >> {'created_at': 1470735085952,
        'games': [22388, 22389, 22390],
        'id': 844,
        'name': 'Death Note',
        'slug': 'death-note',
        'updated_at': 1470735085952,
        'url': 'https://www.igdb.com/franchises/death-note'}

Genres
--------------
::

    >> req.get_genres(fields='*', limit=40)[1]
    >> {'created_at': 1341431954666,
        'games': [1031,
           22381,
           22383,
           22386,
           22387,
           18148,
           18981,
           22403,
           22409,
           22414,
           22417],
        'id': 32,
        'name': 'Indie',
        'slug': 'indie',
        'updated_at': 1341431954666,
        'url': 'https://www.igdb.com/genres/indie'}

Keywords
--------------
::

    >> req.get_keywords(fields='*', limit=50, offset=0)[1]
    >> {'created_at': 1401296058552,
        'games': [4838, 7060, 8862],
        'id': 1081,
        'name': 'masked wrestling',
        'slug': 'masked-wrestling',
        'updated_at': 1401296058552,
        'url': 'https://www.igdb.com/categories/masked-wrestling'}

People
--------------
::

    >> req.get_people(fields='*')
    >> {'created_at': 1412519219083,
        'games': [8223, 3025],
        'gender': 0,
        'id': 32377,
        'name': 'Kristianne Bilodeau',
        'slug': 'kristianne-bilodeau',
        'updated_at': 1467293030099,
        'url': 'https://www.igdb.com/people/kristianne-bilodeau'}

Platforms
--------------
::

    >> req.get_platforms(fields='*', limit=50, offset=0)[1]
    >> {'alternative_name': 'Nintendo Super Disc',
        'created_at': 1468482761733,
        'id': 131,
        'name': 'Nintendo PlayStation',
        'slug': 'nintendo-playstation',
        'updated_at': 1468574267550,
        'url': 'https://www.igdb.com/platforms/nintendo-playstation',
        'versions': [{'name': 'Initial version',
                      'slug': 'initial-version',
                      'url': 'https://www.igdb.com/platforms/nintendo-playstation/version/initial-version'}]}

Player Perspectives
--------------
::

    >> req.get_player_perspectives(fields='*')[1]
    >> {'created_at': 1413209511809,
        'games': [9076,
                  2629,
                  7698,
                  8597,
                  8662,
                  8612,
                  18981],
        'id': 6,
        'name': 'Aural',
        'slug': 'aural',
        'updated_at': 1413209511809,
        'url': 'https://www.igdb.com/player_perspectives/aural'}

Pulses
--------------
::

    >> req.get_pulses(fields='*')[1]
    >> {'author': 'MaGuishi',
        'category': 1,
        'id': 6711,
        'image': 'http://b.thumbs.redditmedia.com/L-KfQC4sT0Y5AuYMUhn3w_8p0sfnjMW2eZrhsleA5Lk.jpg',
        'published_at': 1456151397000,
        'title': 'Los Santos@Minecraft',
        'uid': '4711ju',
        'url': '/r/gaming/comments/4711ju/los_santosminecraft/'}

Series
--------------
::

    >> req.get_series(fields='*')[1]
    >> {'created_at': 1422487135147,
        'games': [8817],
        'id': 1192,
        'name': 'Smugglers',
        'slug': 'smugglers',
        'updated_at': 1422487135147,
        'url': 'https://www.igdb.com/collections/smugglers'}

Themes
--------------
::

    >> req.get_themes(fields='*', limit=40)[1]
    >> {'created_at': 1356889401895,
        'games': [1712,
                  8567,
                  22408,
                  19930,
                  22417],
        'id': 40,
        'name': 'Party',
        'slug': 'party',
        'updated_at': 1356889401895,
        'url': 'https://www.igdb.com/themes/party'}

Examples with filters
---------------------
::

    >> from igdb import Filter
    >> from igdb.operators import EQ
    >> filter_name = Filter(field='name', operator=EQ, value='Crysis 3')
    >> req.get_games(fields='*', limit=10, offset=0, order='release_dates.date:desc', filters=[filter_name])

