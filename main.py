import requests
import pprint

res={1:('https://api.github.com/', {'q':'html'},'get'),
    2:('https://jsonplaceholder.typicode.com/posts', {'userId':1},'get'),
    3:('https://jsonplaceholder.typicode.com/posts',  {'title': 'foo', 'body': 'bar', 'userId': 1},'post')}

while n := int(input('Введите номер задания (0 для выхода): ')):
    response = eval(f'requests.{res[n][2]}(res[n][0], {"params" if res[n][2]=="get" else "json"}=res[n][1])')
    print(response.status_code)  # Вывод статус-кода

    response_json = response.json()
    pprint.pprint(response_json)
