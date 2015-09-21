# -*- coding: utf8 -*-
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
# --------------------------------------------------------------------------
# Blender 2.5 Indigo Add-On
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
import bpy

from indigo import IndigoAddon

from indigo.operators.indigodb_lib import IndigoSearchDB


@IndigoAddon.addon_register_class
class INDIGO_OT_indigodb(bpy.types.Operator):
    """Indigo Materials Database"""

    bl_idname = 'indigo.indigodb'
    bl_label = 'Indigo Material'

    invoke_action_id = bpy.props.IntProperty(default=0)

    def execute(self, context):
        try:
            aid = self.properties.invoke_action_id

            if aid == -1:
                # Activate panel
                lrmdb_state._active = True
                lrmdb_state.show_category_list(context)
            if aid == -2:
                # Deactivate panel
                lrmdb_state._active = False

            # Otherwise look for action id in current list
            for action in lrmdb_state.actions:
                if action.aid == aid:
                    action.execute(context)

            return {'FINISHED'}

        except Exception as err:
            self.report({'ERROR'}, '%s' % err)
            return {'CANCELLED'}

    @classmethod
    def poll(cls, context):
        return context.scene.render.engine == 'INDIGO_RENDER'

