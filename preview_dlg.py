import wx
from utils import write_file


class PreviewDlg(wx.Dialog):
    def __init__(self, parent, path, text):
        super().__init__(parent, title="Convertion result")
        self.text = text
        self.path = path
        pnl = wx.Panel(self)
        box = wx.BoxSizer()
        box.Add(wx.StaticText(pnl, label="Convertion succeeded"))
        box.Add(wx.StaticText(pnl, label="Result"))
        self.edit = wx.TextCtrl(
            pnl, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_RICH2
        )
        self.edit.SetValue(self.text)
        box.Add(self.edit)
        save = wx.Button(pnl, wx.ID_SAVE)
        save.Bind(wx.EVT_BUTTON, self.on_save)
        box.Add(save)
        box.Add(wx.Button(pnl, wx.ID_CLOSE))
        pnl.SetSizer(box)
        self.SetEscapeId(wx.ID_CLOSE)

    def on_save(self, event):
        menu = wx.Menu()
        override = menu.Append(wx.NewIdRef(), "&Override existing file").GetId()
        new = menu.Append(wx.NewIdRef(), "Save to a &new file").GetId()
        selection = self.GetPopupMenuSelectionFromUser(menu)
        if selection == new:
            with wx.FileDialog(
                self,
                "Select a location to save the converted golden cursor file in",
                wildcard="Golden Cursor files (*.gc)|*.gc",
                style=wx.FD_SAVE,
            ) as fdlg:
                if fdlg.ShowModal() == wx.ID_OK:
                    save_path = fdlg.GetPath()
                    write_file(save_path, self.text)
                    wx.MessageBox(
                        f"File written successfully at {save_path}",
                        "Success",
                        wx.ICON_WARNING,
                    )
                    self.Close()
        elif selection == override:
            write_file(self.path, self.text)
            wx.MessageBox(
                f"File written successfully at {self.path}", "Success", wx.ICON_WARNING
            )
            self.Close()
