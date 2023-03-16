import re
import urllib.parse
from recipines_master import *


def toHebUrl(query): 
    linkUrl = ""

    for letter in query:
        if re.findall("\w", letter):
            linkUrl += letter
        else: 
            lett = urllib.parse.quote(letter)
            linkUrl += lett

    return linkUrl


def toWhatsAppLink(phone, query):

    if len(str(phone)) == 9:
        phone = "972" + str(phone)

    return f"https://web.whatsapp.com/send?phone={phone}&text={toHebUrl(query)}&type=phone_number&app_absent=0"


# print(toWhatsAppLink(972585185607, """שלום שניאור, 
# בהמשך להרשמתך לתכנית המנטורים של DDoS

# מצורף כאן קישור לטופס רישום קצר,
# לאחר מילויו והשלמת התשלום
# נציג הקהילה יצור איתך קשר.

# https://docs.google.com/forms/d/e/1FAIpQLSdTazfQwNLULWcQY-iXxILWzKIqRkeVzUAe52p5zFstYCzk-A/viewform"""))