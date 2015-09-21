# -*- coding: utf8 -*-
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# --------------------------------------------------------------------------
# Blender 2.5 Blednigo Add-On
# --------------------------------------------------------------------------
#
# Authors:
# Doug Hammond, Marco Goebel
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
"""
Non-blender specific INDIGODB interface handlers should go in here
"""


import http.client, os, requests
import xml.etree.cElementTree as et
from extensions_framework import util as efutil


class IndigoSearchDB(object):

    user_agent = 'Blendigo'
    indigo_material_url = 'http://www.indigorenderer.com/materials/materials/search.xml'
    
    def __init__(self):
        self.get_material = None
        self.mat_items = None
    
    def material_search(self,searchquery):    
        
        try:
            self.get_material = requests.get(self.indigo_material_url,params="q="+searchquery)
            
        except Exception as err:
            return {'CANCELLED'}
        
        if self.get_material.status_code == 200:
            self.mat_items=[dict((attr.tag, attr.text) for attr in el) for el in et.fromstring(self.get_material.text)]
            
            # a=x.material_search('metall')
            # for index, item in enumerate(a):
            # print ("--->", a[index].get('name'))
            
            
        return self.mat_items

    
