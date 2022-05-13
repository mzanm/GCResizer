import wx
import logging
import traceback
import os
import sys
import platform
from FileSelectDlg import FileSelect
from preview_dlg import PreviewDlg
import gparser
from utils import clean_str


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
        if not path or not os.path.exists(path):
            wx.MessageBox(
                "Aborting...",
                "No file selected or file does not exist",
                wx.ICON_ERROR,
            )
            return
        if dlg.convert_from.Selection < 0:
            wx.MessageBox(
                "Aborting...",
                "No from resolution target selected",
                wx.ICON_ERROR,
            )
            return
        if dlg.convert_to.Selection < 0:
            wx.MessageBox(
                "Aborting...",
                "No to resolution target selected",
                wx.ICON_ERROR,
            )
            return

        convert_from = dlg.convert_from.GetString(dlg.convert_from.Selection).split(
            "\u00d7"
        )
        convert_from = tuple([int(i.strip()) for i in convert_from])
        if dlg.convert_to.Selection == 0:
            string = dlg.convert_to.GetString(0)
            convert_to = clean_str(string).split(" ")
        elif dlg.convert_to.Selection > 0:
            convert_to = dlg.convert_to.GetString(dlg.convert_to.Selection).split(
                "\u00d7"
            )
        convert_to = tuple([int(i.strip()) for i in convert_to if i.strip()])
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
    logging.info(f"running on {platform.platform()}")
    logging.info(f"python version: {sys.version}")
    logging.info(f"wx version: {wx.version()}")

    app = wx.App()
    main_frame = Frame()
    main_frame.Show()
    app.MainLoop()
