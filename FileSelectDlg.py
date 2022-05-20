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
import custom_res


class FileSelect(wx.Dialog):
    def __init__(self, frame):
        super().__init__(frame, title="Select a golden cursor file")
        self.pnl = wx.Panel(self)
        box = wx.BoxSizer()
        self.picker = wx.FilePickerCtrl(
            self.pnl,
            wildcard="Golden Cursor files (*.gc)|*.gc",
            message="Select a Golden Cursor file",
        )
        box.Add(self.picker)
        gbox_sizer = wx.StaticBoxSizer(wx.VERTICAL, self.pnl, "Convert options")
        gbox = gbox_sizer.GetStaticBox()
        gbox_sizer.Add(wx.StaticText(gbox, label="Convert from:"))
        resolutions = custom_res.stringify()
        self.convert_from = wx.Choice(gbox, choices=resolutions[1:])
        gbox_sizer.Add(self.convert_from)
        gbox_sizer.Add(wx.StaticText(gbox, label="Convert to:"))
        self.convert_to = wx.Choice(gbox, choices=resolutions)
        self.convert_to.SetSelection(0)
        gbox_sizer.Add(self.convert_to)
        box.Add(gbox_sizer)
        box.Add(wx.Button(self.pnl, wx.ID_OK))
        box.Add(wx.Button(self.pnl, wx.ID_CANCEL))
        self.pnl.SetSizer(box)
