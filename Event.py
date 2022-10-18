import aiogram
from aiogram import types


class Emoji:
    OMG = '\U0001F631'
    SOS = '\U0001F198'
    OK = '\U0001F197'
    UP = '\U0001F199'


class TelegramEvent:
    def __init__(self, problem_notification):

        self.problem_notification = problem_notification
        self.chat_id = self.map_MZone_to_chat(problem_notification['MZone'])
        self.chat_id = problem_notification['chat_id']
        self.status = problem_notification['State']
        self.MZone = problem_notification['MZone']
        self.message = None

    def map_MZone_to_chat(self, MZone):
        MZone_to_chat: dict[str] = {
            "test_mz": "-1001693150662"
        }
        return MZone_to_chat.get(MZone, "-1001693150662")

    def make_message(self) -> types.Message:
        """
        тут создается мессадж сообщения и чат айди
        """

        if self.status == "OPEN":
            self.message = f"{Emoji.SOS} <b>{self.problem_notification['ProblemID']}: {self.status}</b>\n" \
                           f"<b>{self.problem_notification['ProblemTitle']}</b>\n" \
                           f"<pre>Management zone: {self.MZone}\n" \
                           f"Tags: {self.problem_notification['Tags']}\n" \
                           f"</pre>{self.problem_notification['ProblemDetailsText']}\n"
        elif self.status == "MERGED" or self.status == "RESOLVED":
            self.message = f"{Emoji.OK} <b>{self.problem_notification['ProblemID']}: {self.status}</b>\n" \
                           f"<b>{self.problem_notification['ProblemTitle']}</b>\n" \
                           f"<pre>Management zone: {self.MZone}\n" \
                           f"Tags: {self.problem_notification['Tags']}\n</pre>"
        else:
            raise Exception(f"Невозможно отправить в телеграм проблему в статусе '{self.status}'! ")
        msg = aiogram.types.Message(chat=aiogram.types.Chat(id=self.chat_id), text=self.message)
        return msg

