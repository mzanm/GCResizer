import wx
import os


class LinkCtrl(wx.Button):
    def __init__(self, parent, label, url):
        super().__init__(parent, label=label)
        self.SetForegroundColour(wx.BLUE)
        self.url = url
        self.Bind(wx.EVT_BUTTON, self.OnClick)

    def OnClick(self, event):
        os.startfile(self.url)
        self.Disable()
        wx.CallLater(250, self.Enable, (True))
