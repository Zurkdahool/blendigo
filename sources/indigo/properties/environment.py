# -*- coding: utf8 -*-
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# --------------------------------------------------------------------------
# Blender 2.5 Indigo Add-On
# --------------------------------------------------------------------------
#
# Authors:
# Doug Hammond
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

import bpy 

from extensions_framework import declarative_property_group

import indigo
from indigo import IndigoAddon


@IndigoAddon.addon_register_class
class indigo_lightlayer_data(declarative_property_group):
    '''
    Storage class for Indigo light layers. The
    indigo_lightlayers object will store 1 or more of
    these in its CollectionProperty 'lightlayers'.
    '''
    
    ef_attach_to = []    # not attached
    
    controls = [
        'lg_enabled',
        'name',
        'gain'
    ]
    
    enabled = {
        'name':     { 'lg_enabled': True },
        'gain':     { 'lg_enabled': True }
    }
    
    properties = [
        {
            'type': 'bool',
            'attr': 'lg_enabled',
            'name': '',
            'description': 'Enable this light layer',
            'default': True
        },
        {
            'type': 'string',
            'attr': 'name',
            'name': ''
        },
        {
            'type': 'float',
            'attr': 'gain',
            'name': 'Gain',
            'description': 'Overall gain for this light layer',
            'min': 0.0,
            'soft_min': 0.0,
            'default': 1.0,
            'precision': 4
        }
    ]

@IndigoAddon.addon_register_class
class indigo_lightlayers(declarative_property_group):
    '''
    Storage class for Indigo Light Layers.
    '''
    
    ef_attach_to = ['Scene']
    
    controls = [
        'op_lg_add',
        'ignore',
    ]
    
    visibility = {}
    
    properties = [
        {
            'type': 'collection',
            'ptype': indigo_lightlayer_data,
            'name': 'lightlayers',
            'attr': 'lightlayers',
            'items': []
        },
        {
            'type': 'int',
            'name': 'lightlayers_index',
            'attr': 'lightlayers_index',
        },
        {
            'type': 'operator',
            'attr': 'op_lg_add',
            'operator': 'indigo.lightlayer_add',
            'text': 'Add',
            'icon': 'ZOOMIN',
        },
        {
            'type': 'bool',
            'attr': 'ignore',
            'name': 'Merge LightLayers',
            'description': 'Enable this for final renders, or to decrease RAM usage.',
            'default': False
        },
        {
            'type': 'float',
            'attr': 'default_gain',
            'name': 'Gain',
            'description': 'Gain for the default light layer',
            'default': 1.0,
            'min': 0.0,
            'soft_min': 0.0,
            'precision': 4
        }
    ]
    
    def gain_for_layer(self, name):
        ll_gain = self.default_gain
        if name in self.lightlayers:
            ll_gain = self.lightlayers[name].gain
        return ll_gain
    
    def is_enabled(self, name):
        if name != '' and name in self.lightlayers:
            return self.lightlayers[name].lg_enabled
        return True
    
    def enumerate(self):
        en = {
            'default': 0,
        }
        if not self.ignore:
            idx = 1
            for name, lyr in self.lightlayers.items():
                if lyr.lg_enabled:
                    en[name] = idx
                    idx += 1
        return en

@IndigoAddon.addon_register_class
class indigo_atmosphere(declarative_property_group):
    '''
    Storage class for Indigo Light Layers.
    '''
    
    ef_attach_to = ['Scene']
    
    
        
    def toogle_atmosphere(self, context):
        w = context.scene.indigo_atmosphere
        if (w.atmosphere == True):
            atmosphere_sphere = bpy.ops.object.empty_add(type='SPHERE', radius=200, view_align=True, location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))
            ac = context.active_object
            ac.name = "Indigo Atmosphere"

        
    ef_attach_to = ['Scene']
    controls = [
        'atmosphere',
        [ 'atmosphere_turbidity'],
        [ 'atmosphere_posx', 'atmosphere_posy', 'atmosphere_posz', ],
        ]
    
    visibility = {
        'atmosphere_turbidity':   { 'atmosphere': True },
        'atmosphere_posx':        { 'atmosphere': True },
        'atmosphere_posy':        { 'atmosphere': True },
        'atmosphere_posz':        { 'atmosphere': True },
        }
    
    
    properties = [
                    {
            'type': 'bool',
            'attr': 'atmosphere',
            'name': 'Enable Atmosphere',
            'update': toogle_atmosphere,
            'text': 'Add',
            'icon': 'ZOOMIN',
        },
        {
            'type': 'float',
            'attr': 'atmosphere_turbidity',
            'name': 'Turbidity',
            'description': 'Turbidity',
            'slider': True,
            'default': 2.2,
            'min': 1.0,
            'max': 10.0
        },
        {
            'type': 'string',
            'attr': 'center',
            'name': 'center'
        },
        {
            'type': 'float',
            'attr': 'atmosphere_posx',
            'name': 'X:',
            'description': 'Position X',
            'default': 0,
            'min': -9999999,
            'max': 9999999
        },
        {
            'type': 'float',
            'attr': 'atmosphere_posy',
            'name': 'Y:',
            'description': 'Position Y',
            'default': 0,
            'precision':0,
            'min': -9999999,
            'max': 9999999
        },
        {
            'type': 'float',
            'attr': 'atmosphere_posz',
            'name': 'Z',
            'description': 'Position Z',
            'default': 6538472,
            'precision':0,
            'min': -9999999,
            'max': 9999999
        },          
        ]
    
    

    
  