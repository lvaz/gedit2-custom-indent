Gedit Custom Indent
-------------------

A plugin for gedit that allows to customize indent and tab settings per language

* Authors:
  * Leandro Vaz
* Version: 0.1


Installation
------------

1. Download Gedit Custom Indent package
2. Copy the contents inside 'plugin/' (gci/ and gci.gedit-plugin file) to ~/.gnome2/gedit/plugins/
3. Restart gedit
4. Activate the plugin under 'Edit -> Preferences -> Plugins'


Usage
-----

This plugin aims to aid developers that usually work with many different languages and like to customize
their own indent and tab settings per language. It manages your indentation settings in gedit, in the instant
that it's activated, it instantly overrides your gedit indent and tab settings and applies the settings to all
opened documents. All changes made in the plugin configuration dialog are instantly applied to opened documents too, you
don't need to restart gedit. Finally, all settings are permanently stored, you don't need to apply them each time
you start gedit.


Updating
-------

When you want to update to a new version, you should delete the old plugin and download the new one, then just
follow the instructions written on "Installation". Your old settings will be lost, if you want to keep them, you need to
backup "data/" folder before deleting the old plugin, then install the new version and paste your backup on the new plugin folder.


License
-------

Copyright (C) 2011 Leandro Vaz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
