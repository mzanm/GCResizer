# Copyright (C) 2022 mazen428, mohamedSulaimanAlmarzooqi
# This program is free software:
#  you can redistribute it and/or modify it under the terms of the GNU General Public License 3.0 or later

# See the file LICENSE for more details.


import wx


resolutions = (
    (1024, 768),
    (1280, 720),
    (1280, 800),
    (1280, 1024),
    (1360, 768),
    (1366, 768),
    (1440, 900),
    (1536, 864),
    (1600, 900),
    (1680, 1050),
    (1920, 1080),
    (1920, 1200),
    (2048, 1152),
    (2048, 1536),
    (2560, 1080),
    (2560, 1440),
    (2560, 1600),
    (3440, 1440),
    (3840, 2160),
)


def stringify():
    default_size = wx.GetDisplaySize().Get()
    final_list = [
        f"Automatic: {default_size[0]} \u00d7 {default_size[1]} (Current display resolution"
    ]
    for i in resolutions:
        final_list.append(f"{i[0]} \u00d7 {i[1]}")
    return final_list
