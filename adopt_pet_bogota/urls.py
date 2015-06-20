from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # Examples:
    # url(r'^$', 'Ada_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^adopt_web/', include('adopt_pet_bogota.urls',namespace="adopt_web")),
    url(r'^ada/',include('ada.urls',namespace="ada")),
    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
