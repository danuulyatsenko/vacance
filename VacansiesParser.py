import requests
import json


def get_areas(text):
    params = {
        'text': text,
    }
    req = requests.get('https://api.hh.ru/suggests/areas/', params)
    data = req.content.decode()
    req.close()
    return data


def get_areas_id(areas_request):
    areas_request = json.loads(areas_request)
    areas_id = []
    if areas_request['items']:
        for item in areas_request['items']:
            if item['id']:
                areas_id.append(item['id'])
    return areas_id


def get_page(text="", text_location="", area=1, page=0, per_page=100):
    params = {
        'text': '{}:{}'.format(text_location, text),
        'area': area,
        'page': page,
        'per_page': per_page
    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


def analyse(page_request):
    page_request = json.loads(page_request)
    items = page_request['items'] if page_request['items'] else []
    salary = {
        'start_min': items[0]['salary']['from'],
        'start_max': items[0]['salary']['from'],
        'end_min': items[0]['salary']['to'],
        'end_max': items[0]['salary']['to'],
        'average_start': 0,
        'average_end': 0,
        'median_start': 0,
        'median_end': 0,
    }
    start_salaries = []
    end_salaries = []
    if items:
        for item in items:
            if item['salary']:
                if item['salary']['from']:
                    start_salaries.append(item['salary']['from'])
                if item['salary']['to']:
                    end_salaries.append(item['salary']['to'])
        salary['start_min'] = min(start_salaries)
        salary['start_max'] = max(start_salaries)
        salary['end_min'] = min(end_salaries)
        salary['end_max'] = max(end_salaries)
        salary['average_start'] = sum(start_salaries) / len(start_salaries)
        salary['average_end'] = sum(end_salaries) / len(end_salaries)
        salary['median_start'] = (start_salaries[int(len(start_salaries) / 2)] + start_salaries[int(len(start_salaries) / 2 + 1)]) / 2 if len(start_salaries) % 2 == 0 else start_salaries[int(len(start_salaries) / 2 + 1)]
        salary['median_end'] = (end_salaries[int(len(end_salaries) / 2)] + end_salaries[int(len(end_salaries) / 2 + 1)]) / 2 if len(end_salaries) % 2 == 0 else end_salaries[int(len(end_salaries) / 2 + 1)]
    return salary
