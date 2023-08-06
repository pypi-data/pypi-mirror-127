# -*- coding: utf-8 -*-
"""
Scraper for Pennsylvania Superior Court
CourtID: pasup
Court Short Name: pasup
Author: Andrei Chelaru
Reviewer: mlr
Date created: 21 July 2014
"""

from juriscraper.opinions.united_states.state import pa


class Site(pa.Site):
    def __init__(self, *args, **kwargs):
        super(Site, self).__init__(*args, **kwargs)
        self.court_id = self.__module__
        self.url = "https://www.pacourts.us/Rss/Opinions/Superior/"
