# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara


import asyncio
import os
from AAB import *
from pyrogram import *
from pyrogram.types import *
import time
import threading
from AAB.utils import *
from AAB.db import *

loop = asyncio.get_event_loop()


@bot.on_message(filters.command("alive") & filters.user(Vars['owner']),group=2)
async def alive(client : Client, message : Message) :
    await message.reply_text("I am alive.")
    return



@bot.on_message(filters.command('start') & filters.private)
async def start_pm(client : bot,message : Message) :
    try :

        txt = message.text.split("_")[-1]
        doc = get_file_by_hash(txt)

        if not txt :
            await message.reply_text("Hello I am the file sender bot\n\nI send anime based on the given hash and id.")

        elif doc == None :
            await message.reply_text("Wrong Hash given")
        
        else :

            await bot.forward_messages(message.chat.id,file_channel,doc['message_id'],protect_content= True)


    
    except Exception as eor :
        LOG.error(eor)
        return




@bot.on_message(filters.command('logs') & filters.user(Vars['owner']))
async def send_logs(client : Client, message : Message) :
    try :
        await client.send_document(message.from_user.id,'logging.txt',caption="This the log of current session.")
        await message.reply_text("Sent Logs to your pm")
        LOG.info("Sent logs to {}".format(message.from_user.id))
        return
    except Exception as eor :
        await message.reply_text("This error occured during sending of logs : \n\n{}".format(eor))
        LOG.error("Error occured during sending of logs : \n\n{}".format(eor))




def progress(current, total):
    
    LOG.info(f"{current * 100 / total:.1f}%")



# As the name suggests 

def anime_upload(anime_list) :
    
    try :
        for i in anime_list :
            

            name = extract_info(i['title'][0])
            anime_info = anime(name['search_que'])

            message = bot.send_photo(Main_Channel,anime_info['image'],caption= post_message.format(name['main_res'],name['episode'],anime_info['status']),reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Uploading",callback_data="NTG")]]))

            for number in range(0,len(i['hash'])) :

                try :
                    
                    update_msg = bot.send_message(production_chat,"Downloading {}".format(i['name']))


                    if i['quality'][number] == " 720" :

                        file_ = download_magnet(i['magnet'][number],update_msg)
                        bot.send_message(production_chat,"Uploading {}".format(i['name']))
                        
                        file_msg = file_client.send_document(chat_id=file_channel,document= file_['file'],file_name= name['main_res'],caption=i['title'][number],force_document= True,thumb=thumbnail_url,progress=progress)
                        anime_hash = generate_hash(20)
                        msg_id = file_msg.id
                        add_file(i['title'][number],anime_hash,msg_id)

                        # NORMAL 

                        markup = message.reply_markup.inline_keyboard if message.reply_markup else []
                        [markup.append([InlineKeyboardButton(text=f'{i["quality"][number]}',url= f"https://t.me/{bot_me.username}?start={msg_id}_{anime_hash}")])]
                        message.edit_reply_markup(InlineKeyboardMarkup(markup))


                        # ENCODING START'S HERE 

                        enc_msg = bot.send_message(production_chat,"Encoding {}".format(i['name']))
                        encoded = encode_file(file_['file'])
                        enc_msg.edit_text("Encoded Sucessfully now uploading")
                        enocde_msg = file_client.send_document(chat_id=file_channel,document= encoded,file_name= f"[ENCODED] {name['main_res']}",caption=f"[ENCODED] {i['title'][number]}",force_document= True,thumb=thumbnail_url,progress=progress)
                        enc_anime_hash = generate_hash(20)
                        enc_msg_id = enocde_msg.id
                        add_file(i['title'][number],enc_anime_hash,enc_msg_id)
                        
                        #Removing Uploading BTN

                        

                        markup = message.reply_markup.inline_keyboard if message.reply_markup else []
                        markup.reverse()
                        markup.pop()
                        markup.reverse()
                        [markup.append([InlineKeyboardButton(text='[ENCODED]',url= f"https://t.me/{bot_me.username}?start={enc_msg_id}_{enc_anime_hash}")])]
                        message.edit_reply_markup(InlineKeyboardMarkup(markup))

                        
                        
                        # ENCODING END'S HERE 

                        os.remove(file_['file'])
                        os.remove(encoded)
                        remove_anime_from_remain()

                            

                    else :

                        file_ = download_magnet(i['magnet'][number],update_msg)
                        bot.send_message(production_chat,"Uploading {}".format(i['name']))
                        
                        file_msg = file_client.send_document(chat_id=file_channel,document= file_['file'],file_name= name['main_res'],caption=i['title'][number],force_document= True,thumb=thumbnail_url,progress=progress)

                        anime_hash = generate_hash(20)
                        msg_id = file_msg.id
                        add_file(i['title'][number],anime_hash,msg_id)

                        markup = message.reply_markup.inline_keyboard if message.reply_markup else []
                        [markup.append([InlineKeyboardButton(text=f'{i["quality"][number]}',url= f"https://t.me/{bot_me.username}?start={msg_id}_{anime_hash}")])]
                        message.edit_reply_markup(InlineKeyboardMarkup(markup))


                        os.remove(file_['file'])

                        remove_anime_from_remain()
                        pass
                        

                except Exception as error:
                    LOG.error(error)
                    bot.send_message(production_chat,"There was a issue sending a file check logs for more info")
                    pass
    

        update_worker(False)
        return
    except Exception as e :
        LOG.error(e)
        update_worker(False)


# Starts The Torrent worker if needed 
        
def anime_worker() :

    working = is_working()

    if working :
        return
    else :

        try :
            anime_lst = get_remain_anime()

            if len(anime_lst) == 0 :
                return
            else :
                anime_upload(anime_lst)
        
        except Exception :
            pass



# Checks for new Anime
        
def check_anime() :

    is_new = is_new_db()

    if is_new :

        LOG.info("New DB making required changes")
        anime_list = get_anime('0',10)
        add_remain_amime(anime_list['array'])
        add_hash(anime_list['hash'])
        return 
    
    else :

        LOG.info("Checking for new anime")
        last_hash = get_last_hash()
        anime_list = get_anime(last_hash,30)

        if anime_list == None :
            LOG.info("No new anime found.")
            return
        
        else :
            add_remain_amime(anime_list['array'])
            add_hash(anime_list['hash'])
            bot.send_message(production_chat,"{} new anime are added to db".format(len(anime_list['array'])))
            LOG.info("{} new anime are added to db.".format(len(anime_list['array'])))
            return


# Interval Maker // Same as javascript setInterval //

def set_interval(callback, interval_seconds):
    def wrapper():
        while True:
            callback()
            time.sleep(interval_seconds)

    thread = threading.Thread(target=wrapper)
    thread.daemon = True
    thread.start()




async def main() -> None :
    
    try :
        mongo_client.admin.command('ping')
        LOG.info("Connected to Mongo-DB")
        pass
    except Exception as eor :
        LOG.critical("Mongo DB Not connected error : {}".format(eor))
        return
    

    await file_client.start()
    # await file_client.send_message(Vars['production_chat'],"File Bot Started")
    LOG.info('File Bot Started')

    await bot.start()
    # await bot.send_message(Vars['production_chat'],"Main Bot Started")
    LOG.info('Main Bot Started')

    global bot_me 
    bot_me = await bot.get_me()

    update_worker(False)


    set_interval(check_anime, 5 * 60)
    set_interval(anime_worker, 5 * 60)


    await idle()
    await file_client.stop()
    await bot.stop()


if __name__ == "__main__" :
    loop.run_until_complete(main())


# End of Main File