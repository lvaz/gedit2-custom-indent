# -*- coding: utf-8 -*-
#
#    Gedit Custom Indentation
#    Copyright (C) 2011  Leandro Vaz
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import gtk
import pygtk
import gobject
from gci import utils
from gci import settings


class ConfigDialog():

    def __init__(self, window, data_path):
        self._window = window
        self._data_path = data_path
        self._ui_path = os.path.join(data_path, 'ui', 'config-dialog.ui')

        builder = gtk.Builder()
        builder.add_from_file(self._ui_path)

        self._dialog = builder.get_object('config_dialog')
        self._combo_language = builder.get_object('combo_language')
        self._spin_tab_width = builder.get_object('spin_tab_width')
        self._check_use_spaces = builder.get_object('check_use_spaces')
        self._adjustment_tab_width =\
            builder.get_object('adjustment_tab_width')

        lang_list_store = gtk.ListStore(gobject.TYPE_STRING)

        for lang in utils.get_languages():
            lang_list_store.append([lang])

        self._combo_language.set_model(lang_list_store)
        self._combo_language.set_active(0)

        cell = gtk.CellRendererText()
        self._combo_language.pack_start(cell, True)
        self._combo_language.add_attribute(cell, 'text', 0)

        self._combo_language.connect('changed',
            self.on_combo_language_changed)
        self._spin_tab_width.connect('value-changed',
            self.on_spin_tab_width_value_changed)
        self._check_use_spaces.connect('toggled',
            self.on_check_use_spaces_toggled)

    def get_dialog(self):
        return self._dialog

    def on_combo_language_changed(self, combo_language):
        selected_lang = combo_language.get_active_text()
        lang_data = settings.get_lang_data(selected_lang)

        self._adjustment_tab_width.set_value(lang_data[0])
        self._check_use_spaces.set_active(bool(lang_data[1]))

    def on_spin_tab_width_value_changed(self, spin_tab_width):
        self._apply_settings()

    def on_check_use_spaces_toggled(self, check_use_spaces):
        self._apply_settings()

    def _apply_settings(self):
        lang = self._combo_language.get_active_text()
        tab_width = self._spin_tab_width.get_value_as_int()
        use_spaces = self._check_use_spaces.get_active()

        settings.set_lang_data(lang, tab_width, bool(use_spaces))
        utils.apply_settings_to_documents(self._window)
