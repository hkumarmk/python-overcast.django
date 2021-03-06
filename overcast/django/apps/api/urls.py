from django.conf.urls import include, url

from rest_framework_nested import routers

from overcast.django.apps.buildsvc import views
from overcast.django.apps.api.views import GithubLogin

router = routers.DefaultRouter()
router.register(r'repositories', views.RepositoryViewSet)
router.register(r'external_dependencies', views.ExternalDependencyViewSet, base_name='externaldependency')
router.register(r'sources', views.PackageSourceViewSet, base_name='packagesource')
router.register(r'builds', views.BuildViewSet, base_name='buildrecord')

source_router = routers.NestedSimpleRouter(router, r'sources', lookup='source')
source_router.register(r'builds', views.BuildViewSet, base_name='build')

repository_router = routers.NestedSimpleRouter(router, r'repositories', lookup='repository')
#repository_router.register(r'series', views.SeriesViewSet)
repository_router.register(r'sources', views.PackageSourceViewSet, base_name='packagesource')
repository_router.register(r'external_dependencies', views.ExternalDependencyViewSet, base_name='externaldependency')

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^v1/', include(repository_router.urls)),
    url(r'^v1/', include(source_router.urls)),
    url(r'^v1/auth/', include('rest_auth.urls')),
    url(r'^v1/auth/registration/', include('rest_auth.registration.urls')),
    url(r'^v1/auth/github/$', GithubLogin.as_view(), name='github_login')
] 
