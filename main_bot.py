# -*- coding: utf-8 -*-
from base.hendler import DialogBot
from base.items import HTML


def dialog():
    answer = yield "Здравствуйте! Меня забыли наградить именем, а как зовут вас?"

    name = answer.text.rstrip(".!").split()[0].capitalize()
    print(name)
    likes_python = yield from ask_yes_or_no(
        "Приятно познакомиться, %s. Вам нравится работать с Максимом?" % name)
    if likes_python:
        answer = yield from discuss_good_python(name)
    else:
        answer = yield from discuss_bad_python(name)


def ask_yes_or_no(question):
    """Спросить вопрос и дождаться ответа, содержащего «да» или «нет».

    Возвращает:
        bool
    """
    answer = yield (question, ["Да.", "Нет."])
    while not ("да" in answer.text.lower() or "нет" in answer.text.lower()):
        answer = yield HTML("Так <b>да</b> или <b>нет</b>?")
    return "да" in answer.text.lower()


def discuss_good_python(name):
    answer = yield "Мы с вами, %s, поразительно похожи! Что вам нравится в нём больше всего?" % name
    likes_article = yield from ask_yes_or_no(
        "Ага. А как вам, кстати, код Максима? Понравилась?")
    if likes_article:
        answer = yield "Чудно!"
    else:
        answer = yield "Жалко."
    return answer


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
