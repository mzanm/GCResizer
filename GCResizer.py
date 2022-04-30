import wx
from FileSelectDlg import FileSelect
from preview_dlg import PreviewDlg
import gparser
from utils import write_file


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="GoldenCursor Resizer")
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
                r = wx.MessageBox(
                    "Aborting...",
                    "No file selected",
                    wx.ICON_ERROR,
                )
                return
            if not dlg.convert_from.GetString(dlg.convert_from.Selection):
                r = wx.MessageBox(
                    "Aborting...",
                    "No from resolution target selected",
                    wx.ICON_ERROR,
                )
                return
            if not dlg.convert_to.GetString(dlg.convert_to.Selection):
                r = wx.MessageBox(
                    "Aborting...",
                    "No to resolution target selected",
                    wx.ICON_ERROR,
                )
                return

            convert_from = dlg.convert_from.GetString(dlg.convert_from.Selection).split(
                "X"
            )
            convert_from = tuple([int(i.strip()) for i in convert_from])
            convert_to = dlg.convert_to.GetString(dlg.convert_to.Selection).split("X")
            convert_to = tuple([int(i.strip()) for i in convert_to])
        text = gparser.parse(path, convert_from, convert_to)
        with PreviewDlg(self) as vdlg:
            vdlg.edit.SetValue(text)
            if vdlg.ShowModal() != wx.ID_SAVE:
                return
        r = wx.MessageBox(
            "Clicking on no will override the original file.",
            "Save converted data to a different file?",
            wx.YES_NO | wx.CANCEL | wx.ICON_WARNING,
        )
        if r == wx.YES:
            with wx.FileDialog(
                self,
                "Select a location to save the converted golden cursor file in",
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
