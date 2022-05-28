# File selection dialog, part of GCResizer
# Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi
# This program is free software:
#  you can redistribute it and/or modify it under the terms of the GNU General Public License 3.0 or later

# See the file LICENSE for more details.


import wx
import custom_res


class FileSelect(wx.Dialog):
    def __init__(self, frame):
        super().__init__(frame, title="Select a golden cursor file")
        box = wx.BoxSizer()
        self.picker = wx.FilePickerCtrl(
            self,
            wildcard="Golden Cursor files (*.gc)|*.gc",
            message="Select a Golden Cursor file",
        )
        box.Add(self.picker)
        gbox_sizer = wx.StaticBoxSizer(wx.VERTICAL, self, "Convert options")
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
        box.Add(self.CreateButtonSizer(wx.OK | wx.CANCEL))
        self.SetSizer(box)
        self.picker.SetFocus()
