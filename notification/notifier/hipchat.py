from hypchat import HypChat
import json
import requests

class HipchatNotifier:

    def __init__(self, config):
        self.__config = config

    def start(self):
        if not self.__config['token'] or not self.__config['endpoint']:
            print "HipChat configuration is missing %s" % self.__config
            raise
        elif self.__config['endpoint']:
            return HypChat(self.__config['token'], endpoint=self.__config['endpoint'])
        else:
            return HypChat(self.__config['token'])

    def notify(self, notification):
        hc = self.start()
        try:
            description = notification.incident.description
            details = notification.incident.details
        except :
            description = notification.message
            details = ""
        try:
            message = description + " " + details
            colour = "yellow"
            if "CRITICAL" in message:
                colour = "red"
            elif "UNKNOWN" in message:
                colour = "gray"
            if notification.user_to_notify.profile.hipchat_room_name: 
                print "Notifying HipChat via API v2"
                response = hc.get_room(notification.user_to_notify.profile.hipchat_room_name).notification(message, color=colour, notify="True", format="html")
            elif notification.user_to_notify.profile.hipchat_room_url:
                print "Notifying HipChat via a simple POST"
                headers = {"content-type": "application/json"}
                hip_msg = '{"color": "' + colour  + '", "message": "' + message + '", "notify": true, "message_format": "html"}' 
                response = requests.post(notification.user_to_notify.profile.hipchat_room_url,headers=headers,data=hip_msg)
                print response.content
            else:
                print "HipChat message send failed"
                return 
            print "HipChat message sent"
        except Exception, e:
            try: 
                resp = json.loads(str(e))
                print "Failed to send HipChat message %s " % (e, str(resp['error']['code']) + " " + resp['error']['message'])
                raise
            except ValueError, e2:
                print "Failed to send HipChat message and failed to get it's error %s ; %s" % (e, e2)
                raise

    def get_all_rooms(self):
        try:
            hc = self.start()
            if not hc:
                return [""]
            else:
                rooms = hc.rooms().contents()
                names = []
                for room in rooms:
                    names.append(room['name'])
            return names
        except:
            return [""]
