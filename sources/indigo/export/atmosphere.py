# -*- coding: utf8 -*-
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# --------------------------------------------------------------------------
# Blender 2.5 Indigo Add-On
# --------------------------------------------------------------------------
#
# Authors:
# Marco Goebel
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# ***** END GPL LICENCE BLOCK *****
#
from indigo.export import xml_builder

           
class atmosphere_xml(xml_builder):
    
    def build_xml_element(self, scene, atmosphere_turbidity):
        xml = self.Element('medium')
        self.build_subelements(scene, self.get_format(), xml)
        return xml
    
    def __init__(self, scene,atmosphere_turbidity):
        self.atmosphere_turbidity = turbidity
        #self.medium_index = medium_index
        #self.medium_data = medium_data
    
    def get_format(self):
        medium_data = self.medium_data.medium_type
        
        fmt[self.medium_data.medium_type] = {
                'turbidity': [self.indigo_atmosphere.atmosphere_turbidity],
                #'center': [ str(self.medium_data.medium_posx) + ' ' + str(self.medium_data.medium_posy) + ' ' + str(self.medium_data.medium_posz)],
            }
        return fmt