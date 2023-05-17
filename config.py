import logging

LOG_FILENAME = "Netflix2TraktImportLog.log"
LOG_LEVEL = logging.INFO
VIEWING_HISTORY_FILENAME = "NetflixViewingHistory.csv"

# Set the datetime format of the csv file (default: %d.%m.%y for 05.02.21)
# Use %Y-%m-%d for 2021-02-05 (Canada, ...)
CSV_DATETIME_FORMAT = "%d.%m.%y"

TMDB_API_KEY = "dcbbfdace16650bbbe830b275416d1b0"
TMDB_LANGUAGE = "en"
TMDB_DEBUG = False
TMDB_SYNC_STRICT = True
TMDB_EPISODE_LANGUAGE_SEARCH = False # more api calls, longer waiting time, 
                                     # only useful if the tmdb language differs from en 
                                     # and episodes cannot be found in the season overview Api calls

TRAKT_API_CLIENT_ID = "9190c4074576ad19c9a7b0d6b09370a787600580f1fa6bd78c807b49e99d84c5"
TRAKT_API_CLIENT_SECRET = "ec5b154817edd671379aeeffc14eddd7972b0882e9e9c7ed696a79567cbaf47a"
TRAKT_API_DRY_RUN = False
TRAKT_API_SYNC_PAGE_SIZE = 1000
