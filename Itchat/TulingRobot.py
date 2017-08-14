import itchat
import requests

KEY = 'a6ed782c1cc44a5d912dcdf72fbe2fec'

def get_resp(msg):
     api = 'http://www.tuling123.com/openapi/api'
     data = {
          'key'     : KEY,
          'info'    : msg,
          'userid'  : 'wechat-root'
     }

     try:
          r = requests.post(api, data=data).json()
          return r.get('text')
     except:
          return


@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
     defaultReply = 'I received: ' + msg['Text']
     reply = get_resp(msg['Text'])
     return reply or defaultReply

itchat.auto_login(hotReload=True)
itchat.run()
