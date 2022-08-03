# File selection dialog, part of GCResizer
# Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi
# This program is free software:
#  you can redistribute it and/or modify it under the terms of the GNU General Public License 3.0 or later

# See the file LICENSE for more details.


import wx
import custom_res


class FileSelect(wx.Dialog):
    def __init__(self, frame):
        super().__init__(
            frame,
            title="Select a golden cursor file",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
        )
        box = wx.BoxSizer(wx.VERTICAL)
        self.book = wx.Choicebook(self)
        self.picker = FilePicker(self.book)
        self.book.AddPage(self.picker, "Convert .gc file", True)
        self.selector = CoordsSelect(self.book)
        self.book.AddPage(self.selector, "Convert one coordinate")
        box.Add(self.book, 0, wx.ALL, 10)
        gbox_sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self, "Convert options")
        gbox = gbox_sizer.GetStaticBox()
        gbox_sizer.Add(wx.StaticText(gbox, label="Convert from:"))
        resolutions = custom_res.stringify()
        self.convert_from = wx.Choice(gbox, choices=resolutions[1:])
        gbox_sizer.Add(self.convert_from)
        gbox_sizer.Add(wx.StaticText(gbox, label="Convert to:"))
        self.convert_to = wx.Choice(gbox, choices=resolutions)
        self.convert_to.SetSelection(0)
        gbox_sizer.Add(self.convert_to)
        box.Add(gbox_sizer, 0, wx.ALL, 10)
        box.Add(self.CreateSeparatedButtonSizer(wx.OK | wx.CANCEL))
        self.SetSizer(box)
        self.picker.picker.SetFocus()


class FilePicker(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self, "Select a file")
        gbox = sizer.StaticBox
        sizer.Add(wx.StaticText(gbox, label="Path"))
        self.picker = wx.FilePickerCtrl(
            gbox,
            wildcard="Golden Cursor files (*.gc)|*.gc",
            message="Select a Golden Cursor file",
        )
        sizer.Add(self.picker)
        self.SetSizer(sizer)

    def GetPath(self):
        return self.picker.GetPath()


class CoordsSelect(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        sizer = wx.StaticBoxSizer(wx.HORIZONTAL, self, "Coordinates:")
        gbox = sizer.StaticBox
        sizer.Add(wx.StaticText(gbox, label="X:"))
        self.x = wx.SpinCtrl(gbox, max=16384)
        sizer.Add(self.x, 0, wx.ALL, 10)
        sizer.Add(wx.StaticText(gbox, label="Y:"))
        self.y = wx.SpinCtrl(gbox, max=16384)
        sizer.Add(self.y, 0, wx.ALL, 10)
        self.SetSizer(sizer)

    def GetCoordinates(self):
        return (int(self.x.GetValue()), int(self.y.GetValue()))
