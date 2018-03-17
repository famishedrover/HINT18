from django.conf.urls import url,include
from . import views

urlpatterns=[
	url(r'^letter',views.LetterView.as_view()),
	url(r'^letter_response',views.LetterResponse.as_view()),
	url(r'^word',views.WordView.as_view()),
	url(r'^analytics',views.AnalyticsView.as_view()),
]