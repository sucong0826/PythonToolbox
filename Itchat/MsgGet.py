import itchat

# Picture: itchat.content.PICTURE
# Voice  : itchat.content.RECORDING
# CARD   : itchat.content.CARD

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
     return 'I\'m busy now...Please leave me a msg.'

itchat.auto_login(hotReload=True)
itchat.run()

itchat.send(u'Test Msg', 'filehelper')
