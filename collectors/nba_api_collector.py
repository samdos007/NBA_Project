from nba_api.stats.endpoints import (
    leaguegamefinder,
    teamgamelogs,
    leaguestandings,
    teamestimatedmetrics,
    boxscoretraditionalv2,
    boxscoreadvancedv2
)

from nba_api.stats.static import teams, players
import pandas as pd
import time
from datetime import datetime
from typing import Optional, List, Dict