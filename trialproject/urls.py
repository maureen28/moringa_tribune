"""trialproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from blog.views import home_view
from news.views import welcome, news_of_day, past_days_news, search_results, article

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'welcome/',welcome, name='welcome'),
    url(r'^search/', search_results, name='search_results'),
    url(r'today/', news_of_day, name='news_of_day'),
    url(r'^article/(\d+)', article, name ='article'),
    url(r'',home_view, name='home'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
