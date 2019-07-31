from tensorflow.keras.callbacks import Callback
from twython import Twython
from telegram import Bot


class BaseBot(Callback):
    """
    Base class for tf/keras bot callback.
    Use this callback to send out live updates
    of model training.
    """
    def __init__(self, freq=1, init_message=None):
        """
        :param freq: (int) or None. If int, will
            send update message every freq epochs.
            If None, will only send a final message
            once model training is concluded.
        :param init_message: (str) or None. If set,
            this message will be send when training
            begins. Could e.g. contain current
            hyperparameter configuration.
        """
        self.freq = freq
        self.init_message = init_message
        self.epoch = None
        self.logs = dict()

    def on_train_begin(self, logs={}):
        """
        Send an initial message if defined in init.
        """
        if self.init_message is not None:
            self._send_message(self.init_message)

    def on_train_end(self, logs={}):
        """
        Send a message at end of training.
        """
        message = self._generate_message()
        self._send_message(message)

    def on_epoch_end(self, epoch, logs={}):
        """
        Send a message every freq epochs.
        If freq is None, no messages are sent
        from here.
        """
        self.epoch = epoch
        self.logs = logs
        if self.freq is None:
            return
        elif epoch % self.freq == 0:
            message = self._generate_message()
            self._send_message(message)

    def _send_message(self, message):
        """
        Sub classes need to define how
        they send out messages.
        """
        raise NotImplementedError('Implement in subclass!')

    def _generate_message(self):
        """
        Generate the message to be send
        based on current log and epoch.
        Replace this function if a
        different message/format is
        required.

        Log is a tf/keras generated dict
        that contains key: value pairs
        being all losses and metrics
        that are monitored. Example:
        loss: 0.5
        val_loss: 0.6
        lr: 0.001

        :param epoch: (int)
        :param logs: (dict)
        :return: (str)
        """
        message = 'epoch: ' + str(self.epoch) + '\n'
        for key in self.logs:
            if key == 'lr':
                number = '{:.2E}'.format(self.logs[key])
            else:
                number = '{0:.4f}'.format(self.logs[key])
            line = key \
                   + ': ' \
                   + number \
                   + '\n'
            message += line
        return message


class TelegramBot(BaseBot):
    """
    Telegram bot that sends
    messages with information on
    training progress.
    """
    def __init__(self, token,
                 chat_id, freq=1,
                 init_message=None):
        """
        On details for how to obtain
        telegram API tokens, please
        refer to readme.

        :param token: (str)
        :param chat_id: (str)
        :param freq: (int)
        :param init_message: (str)
        """
        self.bot = Bot(token=token)
        self.chat_id = chat_id

        super().__init__(freq=freq,
                         init_message=init_message)

    def _send_message(self, message):
        """
        Send telegram message.
        :param message: (str)
        """
        self.bot.send_message(chat_id=self.chat_id,
                              text=message)
