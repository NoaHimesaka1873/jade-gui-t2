# user_screen.py

#
# Copyright 2022 user

#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from gi.repository import Gtk, Adw
from gettext import gettext as _
import re, subprocess, shutil
from jade_gui.classes.jade_screen import JadeScreen


@Gtk.Template(resource_path="/al/getcryst/jadegui/pages/user_screen.ui")
class UserScreen(JadeScreen, Adw.Bin):
    __gtype_name__ = "UserScreen"

    password_entry = Gtk.Template.Child()
    password_confirmation = Gtk.Template.Child()

    password_filled = False
    move_to_summary = False

    password = ""

    def __init__(self, window, application, **kwargs):
        super().__init__(**kwargs)
        self.set_valid(True)
        self.window = window
        self.sudo_enabled = True
        self.root_enabled = True
        self.password_entry.connect("changed", self.verify_password)
        self.password_confirmation.connect("changed", self.verify_password)

    def verify_password(self, widget):
        if (
            self.password_entry.get_text() == self.password_confirmation.get_text()
            and (
                 len(self.password_entry.get_text().strip()) > 7
                 or self.password_entry.get_text().strip() == ''
                )
        ):
            self.password_filled = True
            self.verify_continue()
            self.password_confirmation.remove_css_class("error")
            self.password = self.encrypt_password(self.password_entry.get_text())
            self.password = (
                self.encrypt_password(self.password_entry.get_text())
            )
        else:
            self.password_filled = False
            self.verify_continue()
            self.password_confirmation.add_css_class("error")

    def verify_continue(self):
        self.set_valid(self.password_filled)

    def encrypt_password(self, password):
        return password

    def carousel_next_summary(self, widget):
        self.next_page.move_to_summary = True
        self.carousel.scroll_to(self.next_page, True)
