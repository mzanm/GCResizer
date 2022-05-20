#    Gc resizer, A program to change resolution coordinates for a golden cursor file.

#    Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi 

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import wx
from utils import write_file


class PreviewDlg(wx.Dialog):
    def __init__(self, parent, path, text):
        super().__init__(parent, title="Convertion result")
        self.text = text
        self.path = path
        box = wx.BoxSizer()
        box.Add(wx.StaticText(self, label="Convertion succeeded"))
        box.Add(wx.StaticText(self, label="Result"))
        self.edit = wx.TextCtrl(
            self, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_RICH2
        )
        self.edit.SetValue(self.text)
        box.Add(self.edit)
        save = wx.Button(self, wx.ID_SAVE)
        save.Bind(wx.EVT_BUTTON, self.on_save)
        box.Add(save)
        box.Add(wx.Button(self, wx.ID_CLOSE))
        self.SetSizer(box)

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
