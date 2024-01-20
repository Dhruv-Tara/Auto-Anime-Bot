# Licensed under GNU General Public License
# Copyright (C) 2024  Dhruv-Tara

import libtorrent as lt
import time
from AAB import LOG
from pyrogram.types import Message



def download_magnet(link : str,message : Message) -> str :


    try :

        ses = lt.session()
        ses.listen_on(6881, 6891)
        params = {'save_path': './downloads'}

        handle = lt.add_magnet_uri(ses, link, params)
        ses.start_dht()

        begin = time.time()

        while (not handle.has_metadata()):
            time.sleep(1)
        LOG.info('Starting Torrent Download...')

        LOG.info(f"Starting{handle.name()}")

        while (handle.status().state != lt.torrent_status.seeding):
            s = handle.status()
            state_str = ['queued', 'checking', 'downloading metadata', \
                    'downloading', 'finished', 'seeding', 'allocating']
            LOG.info('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
            
            message.edit_text('%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s ' % (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, s.num_peers, state_str[s.state]))
            
            time.sleep(10)


        end = time.time()
        print(handle.name(), "COMPLETE")

        print("Elapsed Time: ",int((end-begin)//60),"min :", int((end-begin)%60), "sec")
        message.edit_text("Completed Download Now Uploading")
        return {"file" : "./downloads/{}".format(handle.name()), "name" : handle.name()}
    
    except Exception as eor :
        LOG.error(eor)
        return None
    
