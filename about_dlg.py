# About Dialog
# Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi
# This program is free software:
#  you can redistribute it and/or modify it under the terms of the GNU General Public License 3.0 or later

# See the file LICENSE for more details.


import wx
import wx.adv


about_text = """GCResizer.
Version: 1.0.
Copyright \u00a9 2022 mazen428, mohamedSulaimanAlmarzooqi
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""


class about(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="About")
        sizer = wx.BoxSizer(wx.VERTICAL)
        text = wx.TextCtrl(self, value=about_text, style = wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_RICH2, size = (500, 500))
        sizer.Add(text, 0, wx.ALL | wx.EXPAND, 10)
        link_sizer = wx.BoxSizer(wx.HORIZONTAL)
        link_sizer.Add(
            wx.adv.HyperlinkCtrl(
                self, label="Homepage", url="https://github.com/mazen428/GCResizer"
            )
        )
        link_sizer.Add(
            wx.adv.HyperlinkCtrl(
                self, label="License", url="https://www.gnu.org/licenses/gpl-3.0.txt"
            )
        )
        sizer.Add(link_sizer, 0, wx.ALL, 5)
        sizer.Add(wx.Button(self, wx.ID_CLOSE))
        self.Bind(wx.EVT_BUTTON, lambda event: self.EndModal(wx.ID_CLOSE), id = wx.ID_CLOSE)
        self.SetSizer(sizer)
        self.SetEscapeId(wx.ID_CLOSE)
        sizer.Fit(self)
        self.Layout()
