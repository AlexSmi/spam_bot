from base.hendler import DialogBot
from base.items import HTML
from rate.currency import Currency
import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
bank_list = ["Avg", "Black", 'Commercial', 'Government', 'Interbank']
get_currency = Currency()


def dialog():
    answer = yield ("Здравствуйте! Выбирите банк, который вас интересует.", bank_list)
    
    bank = answer.text.rstrip(".!").split()[0].capitalize()
    
    likes_python = yield from ask_yes_or_no(bank)
    if likes_python:
        answer = yield from discuss_good_python(bank)
    else:
        answer = yield from discuss_bad_python(bank)


def ask_yes_or_no(question):
    """Спросить вопрос и дождаться ответа, содержащего «да» или «нет».
    ('avg', 'black', 'commercial', 'government', 'interbank')
    Возвращает:
        bool
    """
    # answer = yield question
    # print(question.lower())
    while not ("avg" in question.lower() or "black" in question.lower() or
               "commercial" in question.lower() or "government" in question.lower() or
               "interbank" in question.lower()):
        text = 'Эту хрень - {} - не нужно вводить в строку. Выберите один из вариантов указанных ниже.'.format(question)
        answer = yield (text, ["Avg", "Black", 'Commercial', 'Government', 'Interbank'])
        # yield from ask_yes_or_no(answer)

    return question.lower()


def discuss_good_python(name):
    name1 = str(name).lower()
    correct = get_currency.select_currency
    # yield "Банк {} - курс ".format(correct(name1))
    l = []
    for key, value in correct(name1):
        l.append("Банк - {},    курс ({})\n".format(key, float(value)))
    z = ''.join(l)
    yield z


    # likes_article = yield from ask_yes_or_no(
    #     "Ага. А как вам, кстати, код Максима? Понравилась?")
    # if likes_article:
    #     answer = yield "Чудно!"
    # else:
    #     answer = yield "Жалко."
    # return answer


def discuss_bad_python(name):
    answer = yield "Ай-яй-яй. %s, фу таким быть! Что именно вам так не нравится?" % name
    likes_article = yield from ask_yes_or_no(
        "Ваша позиция имеет право на существование. Работать "
        "в целом, надо полагать, тоже не нравится?")
    if likes_article:
        answer = yield "Ну и ладно."
    else:
        answer = yield (
            "Что «нет»? «Нет, не понравилась» или «нет, понравилась»?",
            ["Нет, не понравилась!", "Нет, понравилась!"]
        )
        answer = yield "Спокойно, это у меня юмор такой."
    return answer


if __name__ == "__main__":
    dialog_bot = DialogBot(dialog)
    dialog_bot.start()
