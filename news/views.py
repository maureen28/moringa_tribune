from django.http import HttpResponse, Http404
from django.shortcuts import render
import datetime as dt
from .models import Article
from .forms import NewsLetterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    date = dt.date.today()
    news = Article.todays_news()

    form =NewsLetterForm(request.POST)
    if request.method =='POST':
        if form.is_valid():
            ame = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('news_today')
        else:
            form =NewsLetterForm()
    return render(request ,'news/today.html',{'date': date, 'news': news, 'letterForm':form})

def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render(request, 'news/today.html',{"date": date,"news":news})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'news/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def article(request,article_id):
    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result
        article = Article.objects.get(id = article_id)

    return render(request,"news/article.html", {"article":article})