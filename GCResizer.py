import wx
from FileSelectDlg import FileSelect
import gparser


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
            text = gparser.parse(dlg.picker.GetPath())
            r = wx.MessageBox(
                "Clicking on no will override the original file.",
                "Save converted data to a different file?",
                wx.YES_NO | wx.ICON_QUESTION,
            )
            if r == wx.YES:
                with wx.FileDialog(
                    self,
                    "Select a location to save the converted golden curser file in",
                    wildcard="*.gc",
                    style=wx.FD_SAVE,
                ) as fdlg:
                    if fdlg.ShowModal() == wx.ID_OK:
                        save_path = fdlg.GetPath()
                        with open(save_path, "w") as f:
                            f.write(text)
            else:
                with open(dlg.picker.GetPath(), "w") as f:
                    f.write(text)


app = wx.App()
main_frame = Frame()
main_frame.Show()
app.MainLoop()
