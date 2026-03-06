from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import NearByPlace, Guest

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            'index',
            'about',
            'gallery',
            'contact',
            'booking',
            'room',
            'near_by_places',
        ]

    def location(self, item):
        return reverse(item)


class NearByPlaceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return NearByPlace.objects.all()

    def lastmod(self, obj):
        return obj.created_date

    def location(self, obj):
        return f"/near-by-places/{obj.id}/"


class GuestSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Guest.objects.all()

    def lastmod(self, obj):
        return obj.created_date