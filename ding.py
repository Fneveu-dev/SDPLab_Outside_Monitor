import os, time, hashlib, logging, notify2, pdb

#pre reqs are libnotify
logging.basicConfig(filename='uploader.log', encoding='utf-8', level=logging.DEBUG)


notify2.init('Hall Monitor')

#send commands to the computer
def send_commands():
    if os.path.isfile("./show_images"):
        os.system("touch ~/show_images")
        os.system("rm ~/show_videos")
    else:
        os.system("touch ~/show_videos")
        os.system("rm ~/show_images")

def notify_now(msg, timeout=1):
    n = notify2.Notification('Hall Monitor', msg)
    n.set_urgency(2)
    n.show()
    time.sleep(timeout)
    n.close()

def send_files():
    os.system("cp ./Videos/* ~/Videos")
    os.system("cp ./Images/* ~/Pictures")
    
    notify_now("files were sent")

try:
    os.chdir("/media/hallmonitor/hallpass")
    decoded_file = hashlib.md5(open('key','rb').read()).hexdigest()

    if decoded_file==key:
        logging.info('key is correct')
        notify_now("sending commands")
        send_commands()
        notify_now("sending files")
        send_files()
        notify_now("rebooting, remove flashdrive", 10)
        os.system('systemctl reboot -i')
    else:
        notify_now('"bad-key error"')
        logging.debug("key is not existant or not correct")

except Exception as e: 
    print("error")
    print(e)
    logging.debug(e)
    notify_now("error")


