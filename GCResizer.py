import wx
from FileSelectDlg import FileSelect
import gparser
from utils import write_file


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="GoldenCurser Resizer")
        self.pnl = wx.Panel(self)
        box = wx.BoxSizer()
        self.convert_btn = wx.Button(self.pnl, label="Convert:")
        box.Add(self.convert_btn)
        self.pnl.SetSizer(box)
        self.convert_btn.Bind(wx.EVT_BUTTON, self.open_file_dlg)

    def open_file_dlg(self, event):
        with FileSelect(self) as dlg:
            res = dlg.ShowModal()
            if res != wx.ID_OK:
                return
            path = dlg.picker.GetPath()
            if not path:
                return
        text = gparser.parse(path)
        r = wx.MessageBox(
            "Clicking on no will override the original file.",
            "Save converted data to a different file?",
            wx.YES_NO | wx.CANCEL | wx.ICON_WARNING,
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
                    write_file(save_path, text)
        elif r == wx.NO:
            write_file(path, text)


app = wx.App()
main_frame = Frame()
main_frame.Show()
app.MainLoop()
