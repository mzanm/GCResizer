import wx
import custom_res


class FileSelect(wx.Dialog):
    def __init__(self, frame):
        super().__init__(frame, title="Select a golden curser file")
        self.pnl = wx.Panel(self)
        box = wx.BoxSizer()
        self.picker = wx.FilePickerCtrl(
            self.pnl, wildcard="*.gc", message="Select a Golden Curser file"
        )
        box.Add(self.picker)
        gbox_sizer = wx.StaticBoxSizer(wx.VERTICAL, self.pnl, "Convert options")
        gbox = gbox_sizer.GetStaticBox()
        gbox_sizer.Add(wx.StaticText(gbox, label="Convert from:"))
        screen_res = custom_res.stringify()
        self.convert_from = wx.Choice(gbox, choices=screen_res)
        gbox_sizer.Add(self.convert_from)
        gbox_sizer.Add(wx.StaticText(gbox, label="Convert to:"))
        self.convert_to = wx.Choice(gbox, choices=screen_res)
        gbox_sizer.Add(self.convert_to)
        box.Add(gbox_sizer)
        box.Add(wx.Button(self.pnl, wx.ID_OK))
        box.Add(wx.Button(self.pnl, wx.ID_CANCEL))
        self.pnl.SetSizer(box)
