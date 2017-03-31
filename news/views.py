# standard library

# third-party
import feedparser

# Django
from django.shortcuts import render

# local Django


def home(request):
    try:
        news_list = []
        news_list_top_stories = feedparser.parse(
            'http://feeds.feedburner.com/ndtvnews-top-stories'
        )
        news_list.append([news_list_top_stories, 'Top Stories'])
        news_list_world = feedparser.parse(
            'http://feeds.feedburner.com/ndtvnews-world-news'
        )
        news_list.append([news_list_world, 'World'])
        news_list_business = feedparser.parse(
            'http://feeds.feedburner.com/ndtvprofit-latest'
        )
        news_list.append([news_list_business, 'Business'])
        news_list_cricket = feedparser.parse(
            'http://feeds.feedburner.com/ndtvsports-cricket'
        )
        news_list.append([news_list_cricket, 'Cricket'])
        news_list_tech = feedparser.parse(
            'http://feeds.feedburner.com/gadgets360-latest'
        )
        news_list.append([news_list_tech, 'Tech'])

    except AttributeError:
        news_list = None

    context = {
        'news_list': news_list,
        'title': 'News From Everywhere',
    }

    return render(request, 'news/home.html', context)


def latest_stories(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvnews-latest'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Latest Stories',
        }
        return render(request, 'news/stories.html', context)


def top_stories(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvnews-top-stories'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Top Stories',
        }
        return render(request, 'news/stories.html', context)


def india(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvnews-india-news'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'India',
        }
        return render(request, 'news/stories.html', context)


def world(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvnews-world-news'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'World',
        }
        return render(request, 'news/stories.html', context)


def business(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvprofit-latest'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Business',
        }
        return render(request, 'news/stories.html', context)


def cricket(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvsports-cricket'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Cricket',
        }
        return render(request, 'news/stories.html', context)


def sports(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvsports-latest'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Sports',
        }
        return render(request, 'news/stories.html', context)


def tech(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/gadgets360-latest'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Tech',
        }
        return render(request, 'news/stories.html', context)


def movies(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/ndtvmovies-latest'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Movies',
        }
        return render(request, 'news/stories.html', context)


def auto(request):
    try:
        news_list = feedparser.parse(
            'http://feeds.feedburner.com/carandbike-latest'
        )
    except AttributeError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Auto',
        }
        return render(request, 'news/stories.html', context)
