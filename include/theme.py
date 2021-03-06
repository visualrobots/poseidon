#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of Poseidon.
#
# Poseidon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Poseidon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Poseidon. If not, see <http://www.gnu.org/licenses/>.

import os, sys, gi
from gi.repository import Gtk, Gdk
sys.path.append(".")
from settings import theme_file
from functions import is_image_valid

def apply_css():

    theme = """#notebook.header.top, #notebook header tabs { background: url('"""\
    + theme_file + """') no-repeat center; background-size: cover; }"""

    css = """

    /* Tested on Gtk 3.18/3.20 */

    #notebook.header.top, #notebook header tabs { background: none; }
    #notebook tab { padding: 10px 15px 10px 15px; }
    #frame_main border, #frame_find border, #frame_vte border, #frame_status border,
    #frame_permission border, #frame_cert border, #frame_cookies border { border-style: none; }
    #frame_main, #frame_find, #frame_vte, #frame_status, #frame_permission, #frame_cert, #frame_cookies
    { border-style: solid; padding: 5px; border-color: rgba(50, 50, 50, 0.20); }
    #frame_main, #frame_permission, #frame_cert { border-width: 0px 0px 1px 0px; }
    #frame_find, #frame_vte, #frame_status, #frame_cookies { border-width: 1px 0px 0px 0px; }
    #entry border { border-style: solid; }
    #frame_x509 border, #frame_x509 { border-width: 0px 1px 1px 0px;
    border-color: rgba(50, 50, 50, 0.20); border-radius: 0px; }
    #label_x509 { padding: 10px; }

    """

    if os.path.exists(theme_file):
        if is_image_valid(theme_file):
            css += theme

    cssprovider = Gtk.CssProvider()
    cssprovider.load_from_data(bytes(css.encode()))
    screen = Gdk.Screen.get_default()
    stylecontext = Gtk.StyleContext()
    stylecontext.add_provider_for_screen(screen, cssprovider, Gtk.STYLE_PROVIDER_PRIORITY_USER)

