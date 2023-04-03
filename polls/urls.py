from django.urls import path

from polls.views import homepage, questions_list, question_detail, question_vote, question_add

app_name = 'polls'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('questions/', questions_list, name='questions_list'),
    path('questions/<int:question_id>/', question_detail, name='question_detail'),
    path('questions/<int:question_id>/vote/', question_vote, name='question_vote'),
    path('questions/add/', question_add, name='question_add'),
]
