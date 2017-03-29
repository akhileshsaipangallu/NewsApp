# standard library
import json
import urllib2
import xmltodict

# third-party
from bs4 import BeautifulSoup

# Django
from django.shortcuts import render

# local Django


def convert_to_json(xml_str, xml_attribs=True):
    d = xmltodict.parse(xml_str, xml_attribs=xml_attribs)
    return json.dumps(d, indent=4)


def latest_stories(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvnews-latest')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Latest Stories',
        }
        return render(request, 'news/stories.html', context)


def top_stories(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvnews-top-stories')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Top Stories',
        }
        return render(request, 'news/stories.html', context)


def india(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvnews-india-news')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'India',
        }
        return render(request, 'news/stories.html', context)


def world(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvnews-world-news')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'World',
        }
        return render(request, 'news/stories.html', context)


def business(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvprofit-latest')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))
    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Business',
        }
        return render(request, 'news/stories.html', context)


def cricket(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvsports-cricket')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Cricket',
        }
        return render(request, 'news/stories.html', context)


def sports(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvsports-latest')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Sports',
        }
        return render(request, 'news/stories.html', context)


def tech(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/gadgets360-latest')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Tech',
        }
        return render(request, 'news/stories.html', context)


def movies(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/ndtvmovies-latest')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Movies',
        }
        return render(request, 'news/stories.html', context)


def auto(request):
    data_file = urllib2.urlopen('http://feeds.feedburner.com/carandbike-latest')
    soup = BeautifulSoup(data_file, 'xml')
    json_data = json.loads(convert_to_json(str(soup)))

    try:
        news_list = json_data['rss']['channel']['item']
    except KeyError:
        news_list = None
    finally:
        context = {
            'news_list': news_list,
            'title': 'Auto',
        }
        return render(request, 'news/stories.html', context)
