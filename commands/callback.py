from __main__ import bot
from vkbottle import GroupEventType, GroupTypes
from database import show_new_dz, new_dz

@bot.on.raw_event(GroupEventType.MESSAGE_EVENT, GroupTypes.MessageEvent)
async def rusyas(event: GroupTypes.MessageEvent):
    if event.object.payload == {'cmd':'rusyas'}: # Русск. язык
        new_dz('Русск.яз.(база)', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'rusyas_p'}: # Русск. язык (профиль)
        new_dz('Русск.яз.(профиль)', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'ruslit'}: # Русск. литература
        new_dz('Русск.лит.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'belyas'}: # Бел. язык
        new_dz('Бел.яз.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'bellit'}: # Бел. литература
        new_dz('Бел.лит.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'mat'}: # Математика (база)
        new_dz('Математ.(база)', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'mat_p'}: # Математика (профиль)
        new_dz('Математ.(профиль)', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'bio'}: # Биология
        new_dz('Биолог.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'vistor'}: # Всемирная история
        new_dz('Всем.истор.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'bistor'}: # История Беларуси
        new_dz('Истор.Бел.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'obsch'}: # Обществоведение
        new_dz('Обществ.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'info'}: # Информатика
        new_dz('Информат.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'astro'}: # Астрономия
        new_dz('Астроном.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'phys'}: # Физика
        new_dz('Физ.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'him'}: # Химия
        new_dz('Хим.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'geo'}: # География
        new_dz('Географ.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'fra_t'}: # Французский язык (Тараникова)
        new_dz('Франц.яз.(Тараникова)', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'fra_d'}: # Французский язык (Дорошкова)
        new_dz('Франц.яз.(Дорошкова)', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'fra_'}: # Французский язык ()
        new_dz('Франц.яз.()', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )
    elif event.object.payload == {'cmd':'nem'}: # Немецкий язык
        new_dz('Нем.яз.', show_new_dz())
        await bot.api.messages.send_message_event_answer(
            event_id = event.object.event_id,
            user_id = event.object.user_id,
            peer_id = event.object.peer_id,
            event_data = '{"type":"show_snackbar", "text":"Записано!"}'
        )