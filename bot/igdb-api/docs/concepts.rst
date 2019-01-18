========
Concepts
========

Extract of https://market.mashape.com/igdbcom/internet-game-database/overview

Fields
------
Fields are properties of an entity. For example, a Game field would be rating or release_dates. Some fields have properties of their own, for example, the esrb field has the property synopsis.
Fields are requested in a comma separated list. For example, to get some information for some Games, Genres, Themes or anything else, you could request it like this::

    fields = 'name,release_dates,esrb.synopsis,rating'

Note the synopsis property of esrb can be accessed directly with a dot.

The timestamps/dates is always measured in nanoseconds since unix epoch.

A full list of fields can be obtained by passing a * as a field.

Filters
-------
Filters are used to sift through results to get what you want. You can exclude and include results based on their properties. For example you could remove all Games where the rating was below 80 (filter[rating][gte]=80).
::

    >> from igdb import Filter
    >> from igdb.operators import GTE, GT
    >> filter = Filter(field='rating', operator=GTE, value=80)
    >> filter = Filter(field='release_dates.date', operator=operators.GT, value='2016-02-21')

The filter itself comprises of 2 parts; The field and the postfix. Fields are described in the section on the left, postfixes are described below.

Available Postfixes:

* eq: Exact match equal.
* gt: Greater than works only on numbers.
* gte: Greater than or equal to works only on numbers.
* lt: Less than works only on numbers.
* lte: Less than or equal to works only on numbers.
* prefix: Prefix of a value only works on strings.
* exists: The value is not null.

Text search
-----------
search: This parameter is not like other filters. It is an independant parameter that performs a full text search.

Ordering
--------
Ordering (Sorting) is used to order results by a specific field.
You can order results like this::

    order = 'release_dates.date:desc'

Notice the appended :desc which could also be :asc if required.
