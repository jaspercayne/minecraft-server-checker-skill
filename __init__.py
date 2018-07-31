from mycroft import MycroftSkill, intent_file_handler


class MinecraftServerChecker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('checker.server.minecraft.intent')
    def handle_checker_server_minecraft(self, message):
        self.speak_dialog('checker.server.minecraft')


def create_skill():
    return MinecraftServerChecker()

