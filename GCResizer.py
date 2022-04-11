import wx
from FileSelectDlg import FileSelect


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="GoldenCurser Resizer")
        self.pnl = wx.Panel(self)
        box = wx.BoxSizer()
        # add combo boxes here to choose resolution and Etc.
        self.convert_btn = wx.Button(self.pnl, label="Convert:")
        box.Add(self.convert_btn)
        self.pnl.SetSizer(box)
        self.convert_btn.Bind(wx.EVT_BUTTON, self.open_file_dlg)

    def open_file_dlg(self, event):
        with FileSelect(self) as dlg:
            dlg.ShowModal()


app = wx.App()
main_frame = Frame()
main_frame.Show()
app.MainLoop()
