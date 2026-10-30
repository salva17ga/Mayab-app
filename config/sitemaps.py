# sitemap for Google indexing

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from apps.portal.models import Mueble, Arte, Decoracion


class StaticSitemap(Sitemap):
    """Static pages of Mayab."""

    protocol = "https"
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "index",
            "about",
            "furnitures",
            "art",
            "decoration",
            "exhibitions",
            "interior_design",
        ]
    
    def location(self, item):
        return reverse(item)


class ProductSitemap(Sitemap):
    """Individual product detail pages."""

    protocol = "https"
    priority = 0.7
    changefreq = "weekly"

    model = None
    tipo = None

    def items(self):
        return self.model.objects.all()

    def location(self, item):
        return reverse(
            "product_detail",
            kwargs={
                "tipo": self.tipo,
                "id": item.pk,
            }
        )

    def lastmod(self, item):
        return item.Fecha_actualizacion


class MuebleSitemap(ProductSitemap):
    model = Mueble
    tipo = "Mueble"


class ArteSitemap(ProductSitemap):
    model = Arte
    tipo = "Arte"


class DecoracionSitemap(ProductSitemap):
    model = Decoracion
    tipo = "Decoracion"