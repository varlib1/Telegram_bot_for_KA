
class Emoji:
    OMG = '\U0001F631'
    SOS = '\U0001F198'
    OK = '\U0001F197'
    UP = '\U0001F199'


class TelegramEvent:
    def __init__(self, problem_notification):

        self.problem_notification = problem_notification
        self.chat_id = self.map_MZone_to_chat(problem_notification.MZone)
        self.chat_id = problem_notification.chat_id
        self.status = problem_notification.State
        self.MZone = problem_notification.MZone

    def map_MZone_to_chat(self, MZone):
        MZone_to_chat: dict[str] = {
            "test_mz": "-1001693150662"
        }
        return MZone_to_chat.get(MZone, "-1001693150662")

    def make_event(self):
        """
        тут создается мессадж сообщения и чат айди
        """

        if self.status == "OPEN":
            self.message = f'{Emoji.SOS} <b>{self.problem_notification.ProblemID}: {self.status}</b>\n<b>{self.problem_notification.ProblemTitle}</b>\n<pre>Management zone: {self.MZone}\nTags: {self.problem_notification.Tags}\n</pre>{self.problem_notification.ProblemDetailsText}\n'
        elif self.status == "MERGED" or self.status == "RESOLVED":
            self.message = f'{Emoji.OK} <b>{self.problem_notification.ProblemID}: {self.status}</b>\n<b>{self.problem_notification.ProblemTitle}</b>\n<pre>Management zone: {self.MZone}\nTags: {self.problem_notification.Tags}\n</pre>'
        else:
            print(f'Невозможно отправить в телеграм проблему в статусе \'{self.status}\'! ')
        return {
            "message.chat.id": self.chat_id,
            "message.text": self.message
        }
