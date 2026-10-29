#sitemap for google indexing
from django.contrib.sitemaps import Sitemap


class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = "weekly"

    def items(self):
        return ["/"]

    def location(self, item):
        return item