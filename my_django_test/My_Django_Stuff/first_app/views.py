from django.shortcuts import render
from first_app.models import Topic, AccessRecord, Webpage, UserInfo

# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Hello I am from views.py'}
    return render(request, 'first_app/index.html', context=my_dict)


def help_page(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record': webpages_list}
    return render(request, 'first_app/help.html', date_dict)

def user_page(request):
    users_list = UserInfo.objects.order_by('name')
    users_dict = {'users_info': users_list}
    return render(request, 'first_app/user.html', users_dict)


