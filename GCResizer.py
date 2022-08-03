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
import ctypes
import logging
import traceback
import os
import sys
import platform
from ConvertDlg import FileSelect
from preview_dlg import PreviewDlg
from about_dlg import about
import gparser
from utils import clean_str, convert_res


class Frame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="GoldenCursor Resizer")
        self.menubar = wx.MenuBar()
        self.help_menu = wx.Menu()
        self.item: wx.MenuItem = self.help_menu.Append(wx.ID_ANY, "About\tF1")
        self.help_menu.Bind(wx.EVT_MENU, self.on_about, self.item)
        self.menubar.Append(self.help_menu, "&Help")
        self.SetMenuBar(self.menubar)
        self.pnl = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        self.convert_btn = wx.Button(self.pnl, label="Convert:")
        box.Add(self.convert_btn, 0, wx.ALL, 20)
        self.about_btn = wx.Button(self.pnl, wx.ID_ABOUT)
        self.about_btn.Bind(wx.EVT_BUTTON, lambda event: self.on_about(None))
        self.pnl.SetSizer(box)
        self.convert_btn.Bind(wx.EVT_BUTTON, self.open_file_dlg)
        self.Center()
        self.convert_btn.SetFocus()

    def on_about(self, event):
        with about(self) as about_dlg:
            about_dlg.ShowModal()

    def open_file_dlg(self, event):
        with FileSelect(self) as dlg:
            res = dlg.ShowModal()
        if res != wx.ID_OK:
            return
        if dlg.book.GetSelection() == 0:
            path = dlg.picker.GetPath()
            if not path or not os.path.isfile(path):
                wx.MessageBox(
                    "No file selected or file does not exist",
                    "Error",
                    wx.ICON_ERROR,
                )
                return
        if dlg.book.GetSelection() == 1:
            path = dlg.selector.GetCoordinates()
        if dlg.convert_from.Selection < 0:
            wx.MessageBox(
                "No from resolution target selected",
                "Error",
                wx.ICON_ERROR,
            )
            return
        if dlg.convert_to.Selection < 0:
            wx.MessageBox(
                "No to resolution target selected",
                "Error",
                wx.ICON_ERROR,
            )
            return

        convert_from = dlg.convert_from.GetString(dlg.convert_from.Selection).split(
            "\u00d7"
        )
        convert_from = tuple([int(i.strip()) for i in convert_from])
        if isinstance(path, tuple) and (
            path[0] - 2 > convert_from[0] or path[1] - 2 > convert_from[1]
        ):
            wx.MessageBox(
                f"Coordinates must be in the range that is converted from: {convert_from[0]}, {convert_from[1]}",
                "Error",
                wx.ICON_ERROR,
            )
            return
        if dlg.convert_to.Selection == 0:
            string = dlg.convert_to.GetString(0)
            convert_to = clean_str(string).split(" ")
        elif dlg.convert_to.Selection > 0:
            convert_to = dlg.convert_to.GetString(dlg.convert_to.Selection).split(
                "\u00d7"
            )
        convert_to = tuple([int(i.strip()) for i in convert_to if i.strip()])
        if isinstance(path, tuple):
            text = convert_res(*path, convert_from, convert_to)
            text = f"{text[0]}, {text[1]}"
        elif isinstance(path, str):
            text = gparser.parse(path, convert_from, convert_to)
        with PreviewDlg(self, path, text) as vdlg:
            vdlg.ShowModal()


if __name__ == "__main__":
    logging.basicConfig(
        filename="gcresizer.log",
        filemode="w",
        level=logging.DEBUG,
        format="%(levelname)s: %(module)s: %(message)s: %(asctime)s",
    )

    def exchandler(type, exc, tb):
        logging.error(
            "".join([str(i) for i in traceback.format_exception(type, exc, tb)])
        )

    sys.excepthook = exchandler
    logging.info("Setting dpi awareness")
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
    logging.info(f"running on {platform.platform()}")
    logging.info(f"python version: {sys.version}")
    logging.info(f"wx version: {wx.version()}")

    app = wx.App()
    main_frame = Frame()
    main_frame.Show()
    app.MainLoop()
