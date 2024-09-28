from tkinter import *
import requests
from bs4 import BeautifulSoup

URL='https://opentdb.com/api_config.php'
response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
categories = soup.select(selector='select[name="trivia_category"]>option')

category_options = {}
params = {}


for category in categories:
        if category.getText() != 'Any Category' and category.getText() != 'Entertainment: Musicals & Theatres' and category.getText() != 'Entertainment: Board Games' and category.getText() != 'Art' and category.getText() != 'Celebrities' and category.getText() != 'Entertainment: Comics' and category.getText() != 'Science: Gadgets':
            category_text = category.getText()
            category_value = category.get('value')
            category_options[f'{category_text}'] = category_value
print(category_options)




def get_input():
    global params
    if category_inside.get() == 'Any Category':
        params = {
            'amount': 10,
            'type': 'boolean',
        }
    else:
        params = {
            'amount': 10,
            'category': category_options[category_inside.get()],
            'type': 'boolean',
        }

    window.destroy()


window = Tk()
window.title('Options')
window.minsize(width=400, height=300)
window.config(pady=20, padx=20)

category_inside = StringVar(window)
category_inside.set('Any Category')

#Category Selection
category_menu = OptionMenu(window, category_inside,*category_options)
category_menu.config(width=50)

category_menu.pack(padx=10, pady=10)


#Submit Button
submit_but = Button(text='Submit', command=get_input)
submit_but.pack(padx=10, pady=10)



window.mainloop()




print(params)








# categories = {
#     'General Knowledge': 9,
#     'Entertainment: Books': 10,
#     'Entertainment: Film': 11,
#     'Entertainment: Music': 12,
#     'Entertainment: Musicals & Theatres': 13,
#     'Entertainment: Television': 14,
#     'Entertainment: Video Games': 15,
#     'Entertainment: Board Games': 16,
#     'Science & Nature': 17,
#     'Science: Computers': 18,
#     'Science: Mathematics': 19,
#
# }