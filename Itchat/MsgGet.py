import itchat

# Picture: itchat.content.PICTURE
# Voice  : itchat.content.RECORDING
# CARD   : itchat.content.CARD

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
     print(msg['Text'])
     return 'Please leave me a message...'

itchat.auto_login(hotReload=True)
itchat.run()

itchat.send(u'Test Msg', 'filehelper')
