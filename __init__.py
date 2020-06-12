from mycroft import MycroftSkill, intent_file_handler


class TellAJoke(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('joke.a.tell.intent')
    def handle_joke_a_tell(self, message):
        self.speak_dialog('joke.a.tell')


def create_skill():
    return TellAJoke()

