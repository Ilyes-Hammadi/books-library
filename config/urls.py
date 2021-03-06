# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from graphene_django.views import GraphQLView
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from books_library.books.apis.views import BookViewSet, BookSimilarViewSet,CommentViewSet, CategoryViewSet, BookSearchViewSet, book_like, book_dislike, book_bookmark, add_comment
from books_library.recomendation.views import suggestion
from books_library.graphql_api.schema import schema
from books_library.graphql_api.views import PrivateGraphQLView
from books_library.users.apis.views import UserViewSet

from books_library.users.views import is_logged_in



# Define DRF API routers
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'categoris', CategoryViewSet)
router.register(r'comments', CommentViewSet)




urlpatterns = [
    url(r'^$',is_logged_in, name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(settings.ADMIN_URL, admin.site.urls),

    # User management
    url(r'^users/', include('books_library.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # GraphQL
    url(r'^graphql', GraphQLView.as_view(graphiql=True, schema=schema)),


    # Books
    url(r'^books/', include('books_library.books.urls', namespace='books')),
    url(r'^suggestions$', suggestion, name="suggestion"),

    # Navigations
    url(r'^navigation/', include('books_library.navigation.urls', namespace="navigation")),

    # Search API
    url(r'^api/search/$', BookSearchViewSet.as_view({'get': 'list'}), name='search_api'),

    # Book action API
    url(r'api/book/like/(?P<id>\d+)/$', view=book_like, name='api_book_like'),
    url(r'api/book/dislike/(?P<id>\d+)/$', view=book_dislike, name='api_book_dislike'),
    url(r'api/book/bookmark/(?P<id>\d+)/$', view=book_bookmark, name='api_book_bookmark'),
    url(r'api/book/comment/$', view=add_comment, name='api_add_comment'),
    url(r'api/book/similar/$', view=BookSimilarViewSet.as_view({'get': 'list'}), name='api_book_similar'),


    # DRF API
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns += [
            url(r'^__debug__/', include(debug_toolbar.urls)),
        ]
