# Preview Dialog
# Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi
# This program is free software:
#  you can redistribute it and/or modify it under the terms of the GNU General Public License 3.0 or later

# See the file LICENSE for more details.


import wx
from utils import write_file


class PreviewDlg(wx.Dialog):
    def __init__(self, parent, path, text):
        super().__init__(
            parent,
            title="Convertion result",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        )
        self.text = text
        self.path = path
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(
            wx.StaticText(
                self,
                label="Convertion succeeded.",
            )
        )
        box.Add(wx.StaticText(self, label="Result"))
        self.edit = wx.TextCtrl(
            self, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_RICH2
        )
        self.edit.SetValue(self.text)
        box.Add(self.edit, 0, wx.EXPAND)
        copy = wx.Button(self, wx.ID_COPY)
        copy.Bind(wx.EVT_BUTTON, self.on_copy)
        save = wx.Button(self, wx.ID_SAVE)
        save.Bind(wx.EVT_BUTTON, self.on_save)
        box.Add(copy)
        box.Add(save)
        box.Add(wx.Button(self, wx.ID_CLOSE))
        self.SetEscapeId(wx.ID_CLOSE)
        self.SetSizer(box)
        box.Fit(self)
        self.Layout()
        if not isinstance(self.path, str):
            save.Hide()
            save.Disable()

    def on_copy(self, event):
        self.edit.SetFocus()
        self.edit.SelectAll()
        self.edit.Copy()

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
