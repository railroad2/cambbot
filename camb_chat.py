import pylab as plt
from gbpipe.spectrum import get_spectrum_camb

class CAMBChat:
    STATUS_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Computing the angular power spectra, please wait for a moment ...",
        },
    }

    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username = "camb"
        self.icon_emoji = ""
        self.timestamp = ""

    def get_message_waiting(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.STATUS_BLOCK,
            ],
        }

    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.DIVIDER_BLOCK,
                self.get_plot_block(),
            ],
        }

    def get_plot_block(self):
        self.__make_spectrum_plot(2000)
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "plot?"
            },
        }

    def __make_spectrum_plot(self, lmax=2000):
        cls_camb = get_spectrum_camb(lmax)
        plt.figure()
        plt.loglog(cls_camb[:3].T)
        plt.loglog(cls_camb[3], 'r-')
        plt.loglog(-cls_camb[3], 'r--')
        plt.savefig("cls.png")
        plt.close()
    

