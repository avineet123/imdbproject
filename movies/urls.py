from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework.routers import DefaultRouter

from movies.views import MovieViewSet, SearchAPIView

admin.autodiscover()
# set up rest router

router = DefaultRouter()
router.register('movie', MovieViewSet)
# set up of rest router ends here

urlpatterns = patterns('',
                       url(r'^', include(router.urls)),
                       url('^search/(?P<movie_name>\w+)/$',
                           SearchAPIView.as_view())
                       )
