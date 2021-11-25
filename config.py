TOKEN = "2142561030:AAHGIl0or_rhTyP9GddIJR0Hh0bZP0nFvFU"
from string import Template
def getRegData(user, title, name):
    t = Template('$title *$name* \n ФИО: *$fullname* \n Телефон: *$phone* ')

    return t.substitute({
        'title': title,
        'name': name,
        'fullname': user.fullname,
        'phone': user.phone
    })

