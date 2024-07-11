from communication import SmsSender, MailSender


class TestableSmsSender(SmsSender):
    def send(self, schedule):
        print("테스트용 SmsSender에서 send 메서트 실행됨")
        self.__send_method_is_call = True

    def is_send_method_is_called(self):
        return self.__send_method_is_call


class TestableMailSender(MailSender):
    def __init__(self):
        self.__count_send_mail_is_called = 0

    def send_main(self, schedule):
        self.__count_send_mail_is_called += 1

    def get_count_send_mail_is_called(self):
        return self.__count_send_mail_is_called
