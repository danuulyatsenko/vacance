from VacansiesParser import *

OUTPUT_SEPARATOR = '=================================================================================================='

if __name__ == '__main__':
    try:
        areas_request = get_areas('Невский район')
        print(areas_request)
        print(OUTPUT_SEPARATOR)
        areas_id = get_areas_id(get_areas('asdsa'))
        print(areas_id)
        print(OUTPUT_SEPARATOR)
        searching_text = input('Текст для поиска: ')
        searching_page_number = input('Индекс страницы поиска: ')
        searching_per_page = input('Кол-во записей на 1 странице поиска: ')
        page_request = get_page(searching_text, 'name', areas_id, searching_page_number, searching_per_page)
        print(page_request)
        print(OUTPUT_SEPARATOR)
        print(analyse(page_request))
    except Exception as error:
        print("Ошибка, некорректный запрос, либо отсутствует подключение к интернету: {}".format(error))
