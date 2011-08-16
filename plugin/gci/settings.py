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
import sqlite3
from utils import get_languages


_db_path = None
_db_conn = None


class UnregisteredLanguageError(Exception):

    def __init__(self, lang):
        self._msg = 'Language "' + lang + '" is not registered'

    def __str__(self):
        return self._msg


def init_settings(data_path):
    global _db_path
    global _db_conn

    _db_path = os.path.join(data_path, 'data', 'settings.sqlite')

    if not os.path.exists(_db_path):
        _db_conn = sqlite3.connect(_db_path)
        _db_conn.execute("""
            CREATE TABLE IF NOT EXISTS lang_settings(
                lang VARCHAR(25) UNIQUE NOT NULL,
                tab_width INTEGER(2) NOT NULL,
                use_spaces INTEGER(1) NOT NULL
            )
        """)

        for lang in get_languages():
            _db_conn.execute('INSERT INTO lang_settings(\
                              lang, tab_width, use_spaces)\
                              VALUES("' + lang + '", 4, 1)')
        _db_conn.commit()

    else:
        _db_conn = sqlite3.connect(_db_path)


def set_lang_data(lang, tab_width, use_spaces):
    global _db_conn
    cur = _db_conn.cursor()

    cur.execute('UPDATE lang_settings SET tab_width=?, use_spaces=? \
                 WHERE lang=?', (tab_width, use_spaces, lang, ))

    if cur.rowcount == 0:
        raise UnregisteredLanguageError(lang)

    _db_conn.commit()


def get_lang_data(lang):
    global _db_conn
    cur = _db_conn.cursor()

    cur.execute('SELECT tab_width, use_spaces\
                 FROM lang_settings WHERE lang=?', (lang, ))

    if cur.rowcount == 0:
        raise UnregisteredLanguageError(lang)

    return cur.fetchone()


def get_all():
    global _db_conn
    return _db_conn.execute('SELECT * FROM lang_settings').fetchall()
