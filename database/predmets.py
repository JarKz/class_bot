from .tables import Poned, Vtorn, Sred, Chetv, Pyant

items = ['Русск.яз.(база)', 'Русск.яз.(профиль)', 'Русск.лит.', 'Бел.яз.', 'Бел.лит.', 'Математ.(база)',
        'Математ.(профиль)', 'Биолог.', 'Всем.истор.', 'Истор.Бел.', 'Обществ.', 'Информат.', 'Астроном.',
        'Физ.', 'Хим.', 'Географ.', 'Франц.яз.(Тараникова)', 'Франц.яз.(Дорошкова)', 'Франц.яз.()', 'Нем.яз.']

weekday_dz = {
    0: Poned.name,
    1: Vtorn.name,
    2: Sred.name,
    3: Chetv.name,
    4: Pyant.name
}
weekday_day = {
    0: Poned,
    1: Vtorn,
    2: Sred,
    3: Chetv,
    4: Pyant
}
days = {
    'понедельник':0,
    'вторник':1,
    'среду':2,
    'четверг':3,
    'пятницу':4
}

pon = [Poned(name = 'Русск.яз.(профиль)'),
    Poned(name = 'Бел.лит.'),
    Poned(name = 'Франц.яз.(Тараникова)'),
    Poned(name = 'Франц.яз.(Дорошкова)'),
    Poned(name = 'Франц.яз.()'),
    Poned(name = 'Биолог.'),
    Poned(name = 'Математ.(база)'),
    Poned(name = 'Математ.(профиль)')]

vtorn = [Vtorn(name = 'Русск.лит.'),
    Vtorn(name = 'Русск.яз.(база)'),
    Vtorn(name = 'Русск.яз.(профиль)'),
    Vtorn(name = 'Математ.(база)'),
    Vtorn(name = 'Математ.(профиль)'),
    Vtorn(name = 'Всем.истор.'),
    Vtorn(name = 'Хим.'),
    Vtorn(name = 'Франц.яз.(Тараникова)'),
    Vtorn(name = 'Франц.яз.(Дорошкова)'),
    Vtorn(name = 'Франц.яз.()'),
    Vtorn(name = 'Нем.яз.')]

sred = [Sred(name = 'Математ.(профиль)'),
    Sred(name = 'Математ.(база)'),
    Sred(name = 'Физ.'),
    Sred(name = 'Франц.яз.(Дорошкова)'),
    Sred(name = 'Бел.яз.'),
    Sred(name = 'Бел.лит.')]

chetv = [Chetv(name = 'Информат.'),
    Chetv(name = 'Биолог.'),
    Chetv(name = 'Обществ.'),
    Chetv(name = 'Математ.(профиль)'),
    Chetv(name = 'Физ.'),
    Chetv(name = 'Хим.'),
    Chetv(name = 'Русск.яз.(профиль)')]

pyatn = [Pyant(name = 'Астроном.'),
    Pyant(name = 'Истор.Бел.'),
    Pyant(name = 'Географ.'),
    Pyant(name = 'Математ.(база)'),
    Pyant(name = 'Математ.(профиль)'),
    Pyant(name = 'Франц.яз.(Тараникова)'),
    Pyant(name = 'Франц.яз.(Дорошкова)'),
    Pyant(name = 'Франц.яз.()'),
    Pyant(name = 'Нем.яз.')]