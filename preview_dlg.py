import wx


class PreviewDlg(wx.Dialog):
    def __init__(self, parent):
        super().__init__(parent, title="Convertion result")
        pnl = wx.Panel(self)
        box = wx.BoxSizer()
        box.Add(wx.StaticText(pnl, label="Convertion succeeded"))
        box.Add(wx.StaticText(pnl, label="Result"))
        self.edit = wx.TextCtrl(
            pnl, style=wx.TE_READONLY | wx.TE_MULTILINE | wx.TE_DONTWRAP | wx.TE_RICH2
        )
        box.Add(self.edit)
        box.Add(wx.Button(pnl, wx.ID_SAVE))
        box.Add(wx.Button(pnl, wx.ID_CLOSE))
        pnl.SetSizer(box)
        self.SetAffirmativeId(wx.ID_SAVE)
        self.SetEscapeId(wx.ID_CLOSE)
