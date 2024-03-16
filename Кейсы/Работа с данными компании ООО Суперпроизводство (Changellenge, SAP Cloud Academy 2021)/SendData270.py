# Вводим библиотеки
import requests
import argparse
import pandas as pd
from deep_translator import GoogleTranslator

# Создаем ссылку для входа в SAP Data Intelligence
url = "https://vsystem.ingress.dh-j1diumsjpjfe.di-xmj.shoot.live.k8s-hana.ondemand.com/app/pipeline-modeler/openapi/service/untitled/test"

# Настраиваем cellid, user и pwd для дальнейшего входа в SAP Data Intelligence
parser = argparse.ArgumentParser(description='Sending device data to SAP Data Intelligence.')
parser.add_argument('--cellid', type = int, help = "device identifier")
parser.add_argument('--user',  type = str ,help = "user")
parser.add_argument('--pwd',  type = str , help = "password")
args = parser.parse_args()

# Загружаем csv-файл из Google Drive: файл с очищенными данными 
url1="https://drive.google.com/file/d/1lnqY2LNabFqC4VQtFHg5syXeSGvtYf0b/view?usp=sharing"
url2='https://drive.google.com/uc?id=' + url1.split('/')[-2]
df = pd.read_csv(url2)

# Загружаем csv-файл из Google Drive: файл с переводами субъектов РФ на английский язык
url3='https://drive.google.com/file/d/1GY5lQC-MGPMHd1EKkCX3wWlNxboESaPx/view?usp=sharing'
url4='https://drive.google.com/uc?id=' + url3.split('/')[-2]
df_region = pd.read_csv(url4).iloc[:,1:]

# Создаем команду для ввода ID клиента
print('Введите ID клиента:')
my_input = input()

# Занимаемся поиском контактных данных клиента с конкретным ID
find_id = df[df['id'] == int(my_input)]

# Формируем контактную информацию на базе заданного ID
key1 = find_id['login'].values[0]
key2 = find_id['user'].values[0]
translated_key2 = GoogleTranslator(source='auto', target='en').translate(key2)
key3 = find_id['email'].values[0]
key4 = find_id['phone'].values[0]
key5 = find_id['region'].values[0]
translated_key5 = df_region[df_region['ru']==key5].values[0][1]

# Создаем текст для отражения информации
data_text = ', '.join(['login: ' + key1,'user: ' + translated_key2,
                       'email: ' + key3,'phone: ' + key4,'region: ' + translated_key5])
# JSON-версия
# data_json = {'login': key1, 'user': translated_key2, 'email': key3, 
# 'phone': key4,'region': translated_key5}

# Выводим получившийся текст
print('Send data: ', data_text)

# Отсылаем запрос
auth = ('default\\' + args.user,args.pwd)
headers = {'X-Requested-With': 'XMLHttpRequest'}
resp = requests.post(url, data=data_text, auth=auth, headers=headers)

# JSON-версия
# resp = requests.post(url, json = data_json,auth=auth,headers=headers)

# Выводим отклик
print(resp)
