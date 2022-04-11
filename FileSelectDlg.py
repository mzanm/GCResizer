import wx


class FileSelect(wx.Dialog):
    def __init__(self, frame):
        super().__init__(frame, title="Select a golden curser file")
        self.pnl = wx.Panel(self)
        box = wx.BoxSizer()
        self.picker = wx.FilePickerCtrl(
            self.pnl, wildcard="*.gc", message="Select a Golden Curser file"
        )
        box.Add(self.picker)
        self.OK = wx.Button(self.pnl, wx.ID_OK)
        box.Add(self.OK)
        box.Add(wx.Button(self.pnl, wx.ID_CANCEL))
        self.pnl.SetSizer(box)
