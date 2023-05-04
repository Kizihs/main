import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import random
import os

token = 'vk1.a.ffrL4gZ-LWS-foaGEhhp-ieSLrvWgkLbf4iIhwSIAlS6Dc5lhrgU0Ga8vwLtNMWhQ0eIVT_VXN8CwwDA2p4vFIgpLq-vGN6x' \
        'fdKr6Rm77nYlLQ4gXW4ndbZsYMcEa8MftTuu2IqFpE_lG9k4P8d5elEMTvBSmDYoHqzZFv6jxrmyECHxWtfCCTSiNWUalTED_4nDDz-' \
        '6lTc8fHJkXG5U4g'
user_token = 'vk1.a.NwGArHJBKgqVrLfEsYvZFxetIUiEsRWZba_SnMjqFEX3KtmTaLN4nNUuFTn8IveyPL45lxqb8klv7IY398zndiTiw8Fvcb' \
             'Yy7bG_aOm4AMjrcU6-ahE4jI_hxiEGJNf_ijaZtN5IXCAGloOPuXkxFFMX8zfcC1kKRKQOyPkbwydHQXVjn1n9HS7mWh-QhNzWde-' \
             'N_nLCU7NiWB_xYOUyjw'

vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, 217780580)
answer = 'Иди нахуй'


def sender(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})


def chat_sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


def my_honest_reaction(id):
    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_messages('images/fzn67MRdxWg.jpg')
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk_session.method('messages.send', {'chat_id': id, 'random_id': 0, 'message': 'My honest reaction',
                                        'attachment': attachment})


def kick(id, msg_obj):
    fwd = vk_session.method('messages.getByConversationMessageId',
                            {'conversation_message_ids': msg_obj['conversation_message_id'],
                             'peer_id': msg_obj['peer_id']})['items'][0]

    fwd = fwd['reply_message']
    mem_id = fwd['from_id']
    vk_session.method('messages.removeChatUser', {'chat_id': id, 'random_id': 0, 'user_id': mem_id})


def findPic(direct, tag=None):
    henList = os.listdir(direct)
    random.shuffle(henList)
    if tag is not None:
        for obj in henList:
            if tag in obj.split(' '):
                uploadPic(direct, obj)
                break
    else:
        uploadPic(direct)


def uploadPic(direct, filename=None):
    upload = vk_api.VkUpload(vk_session)
    if filename is not None:
        photo = upload.photo_messages(str(os.path.join(direct, str(filename))))
    else:
        photo = upload.photo_messages(str(os.path.join(direct, random.choice(os.listdir(direct)))))
    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk_session.method('messages.send', {'chat_id': pid, 'random_id': 0, 'attachment': attachment})


def hen(id):
    direct = "C:\\Users\\andre\\Pictures\\Hentai"
    tag = None
    if msg == '-хентай':
        numb = 1
    else:
        paramList = msg.split(' ')
        match len(paramList):
            case 2:
                if paramList[1].isdigit():
                    numb = int(paramList[1])
                else:
                    tag = paramList[1]
                    numb = 1
            case 3:
                if paramList[1].isdigit():
                    numb = int(paramList[1])
                    tag = paramList[2]
                else:
                    numb = int(paramList[2])
                    tag = paramList[1]
    for i in range(numb):
        findPic(direct, tag)


def sasha(id, count=1):
    vk_session = vk_api.VkApi(token=user_token)
    photo_dict = vk_session.method('photos.get', {'owner_id': 176245974, 'album_id': 'wall', 'count': 1000})
    for i in range(count):
        photo = photo_dict['items'][random.randint(0, 47)]
        owner_id = photo['owner_id']
        photo_id = photo['id']
        attachment = f'photo{owner_id}_{photo_id}_{user_token}'
        vk_session = vk_api.VkApi(token=token)
        vk_session.method('messages.send', {'chat_id': id, 'random_id': 0, 'attachment': attachment})


def ecchi(id):
    direct = "C:\\Users\\andre\\Pictures\\Ecchi"
    tag = None
    if msg == '-этти':
        numb = 1
    else:
        paramList = msg.split(' ')
        match len(paramList):
            case 2:
                if paramList[1].isdigit():
                    numb = int(paramList[1])
                else:
                    tag = paramList[1]
                    numb = 1
            case 3:
                if paramList[1].isdigit():
                    numb = int(paramList[1])
                    tag = paramList[2]
                else:
                    numb = int(paramList[2])
                    tag = paramList[1]
    for i in range(numb):
        findPic(direct, tag)


def music(id):
    vk_session.method('messages.send', {'chat_id': id, 'random_id': 0,
                                        'attachment': 'audio-60027733_456277234_07b9ae58f7ecc471eb'})


def get_id(mssg):
    return mssg['id']


global pid
global direct

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        mssg = event.object.message
        msg = event.object.message['text']
        try:
            if msg != '' and msg[0] == '-':
                pid = event.chat_id

                if msg == '-кик':
                    kick(pid, mssg)
                elif '-саня' in msg:
                    sasha(pid, int(msg.split(' ')[1]) if len(msg) > 5 else 1)
                elif '-этти' in msg:
                    ecchi(pid)
                elif '-хентай' in msg:
                    hen(pid)
                elif '-ХОНЭСТ' in msg:
                    my_honest_reaction(pid)
                elif '-музик' in msg:
                    music(pid)
                elif '-ид':
                    chat_sender(pid, pid)
                else:
                    chat_sender(pid, answer)
        except Exception as ex:
            chat_sender(pid, ex)
