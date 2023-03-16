import requests
import json

# DDos
# response = requests.get('https://opensheet.elk.sh/1pzSm50r9OuUgwOcfDrLwLfbQLnos2nJHRNp0XsQgpiU/exports')

# test
# response = requests.get('https://opensheet.elk.sh/1r9lqmEZnFtPzLELfG-GVg4OnHSl4SRjKfrWq20vfa2I/exports')

# pushcoins to failed doners
# response = requests.get('https://opensheet.elk.sh/1oXLeXvDebZiXtuH_UJQY1gk9sCClmY4SCdL9hviNdeE/exports')

# pushcoins flyers to orgs
response = requests.get('https://opensheet.elk.sh/1VkPd-KMnme0PgZBE0rFLVmTzyYz_6bE_0RHYk5SvmC8/exports')
recipines = json.loads(response.text)





# print(response.status_code)
# print(recipines[1])

