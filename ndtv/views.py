# standard library

# third-party
import feedparser

# Django
from django.shortcuts import render

# local Django


# def get_news():



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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)


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
        return render(request, 'news/home.html', context)
