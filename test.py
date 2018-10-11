import wx
"""
author JunYoung Cho
last modified: 2018-10-11
"""


class Gathering(wx.Frame):
    def __init__(self, parent, title):
        super(Gathering, self).__init__(parent, title=title)
        self.init_ui()

    def init_ui(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour('gray')
        v_box = wx.BoxSizer(wx.VERTICAL)

        mid_pan = wx.Panel(panel)
        mid_pan.SetBackgroundColour('#ededed')

        v_box.Add(mid_pan, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(v_box)


def main():
    app = wx.App()

    gathering = Gathering(None, title='test')
    gathering.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
