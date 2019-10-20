import requests
import csv
import logging


def callAPI(URL, PARAMS):
    HEADERS = {'x-api-key': '28d35ce9-54e5-41d5-86b8-cb665caec3d5'}
    get_data = requests.get(url=URL, params=PARAMS, headers=HEADERS)
    data = get_data.json()
    logging.debug('call API completed')
    return data


def getBreedList(keyword):
    PARAMS = {'q': keyword}
    logging.info('selected key word: ' + str(keyword))
    URL = 'https://api.thecatapi.com/v1/breeds/search'
    data = callAPI(URL, PARAMS)
    counter = 0
    breed_list = []
    for item in data:
        single_breed = fetchSingleBreed(item)
        breed_list.append(single_breed)
        counter = counter + 1
    logging.info('getBreedList completed. Number of breeds found: ' + str(counter))
    logging.info('breed list' + str(breed_list))
    return breed_list


def fetchSingleBreed(item):
    single_breed = []
    try:
        single_breed.append(item['id'])
        single_breed.append(item['name'])
    except:
        logging.info("Error: An exception occurred")
    return single_breed


def writeToCSV(data, file_name, limit):
    str_file_name = file_name + '.csv'
    with open(str_file_name, mode='w') as file:
        file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        counter = 1
        for item in data:
            if counter > limit:
                break
            counter = counter + 1
            file.writerow(item)
    logging.info('writing csv completed, total writing to file: ' + str(counter - 1))


def readCSV(file):
    breed_list = []
    ifile = open(file, "r")
    reader = csv.reader(ifile)
    for line in reader:
        breed_list.append(line)
    logging.info('reading csv completed')
    return breed_list


def getFullDetailsById(list):
    image_list = []
    counter = 0
    for item in list:
        key = item[0]
        logging.info('working on: ' + key)
        PARAMS = {'breed_ids': key, 'limit': 100}
        URL = 'https://api.thecatapi.com/v1/images/search'
        data = callAPI(URL, PARAMS)
        for element in data:
            image = fetchSingleImage(element)
            image_list.append(image)
            counter = counter + 1
            '''try:
                image = []
                image.append(element['id'])
                image.append(element['url'])
                image.append(element['width'])
                image.append(element['height'])
                image.append(element['breeds'][0]['name'])
                image.append(element['breeds'][0]['origin'])
                image.append(element['breeds'][0]['wikipedia_url'])
                image.append(element['breeds'][0]['weight']['metric'])
                image_list.append(image)
                counter = counter + 1
            except:
                logging.info("Error: An exception occurred")
            '''
    logging.info('total images:' + str(counter))
    return image_list


def fetchSingleImage(element):
    image = []
    try:
        image.append(element['id'])
        image.append(element['url'])
        image.append(element['width'])
        image.append(element['height'])
        image.append(element['breeds'][0]['name'])
        image.append(element['breeds'][0]['origin'])
        image.append(element['breeds'][0]['wikipedia_url'])
        image.append(element['breeds'][0]['weight']['metric'])
    except:
        logging.info("Error: An exception occurred")
    return image


def main():
    logging.basicConfig(level=logging.INFO)
    breeds_results = getBreedList('char')
    writeToCSV(breeds_results, 'breeds_file', 1000)
    file = 'breeds_file.csv'
    breed_list = readCSV(file)
    images_results = getFullDetailsById(breed_list)
    writeToCSV(images_results, 'images_file', 20)


if __name__ == "__main__":
    main()
