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

import gedit
import settings


def get_languages():
    langs = gedit.language_manager_list_languages_sorted(
        gedit.get_language_manager(), True)
    lang_ids = []

    for lang in langs:
        lang_ids.append(lang.get_id())

    return lang_ids


def apply_settings_to_document(doc):
    lang = doc.get_language()
    if lang != None:
        view = gedit.tab_get_from_document(doc).get_view()
        lang_data = settings.get_lang_data(lang.get_id())
        view.set_tab_width(lang_data[0])
        view.set_insert_spaces_instead_of_tabs(bool(lang_data[1]))


def apply_settings_to_documents(window):
    for doc in window.get_documents():
        apply_settings_to_document(doc)
