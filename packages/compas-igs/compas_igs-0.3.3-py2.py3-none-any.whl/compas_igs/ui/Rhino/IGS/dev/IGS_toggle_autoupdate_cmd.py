from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import scriptcontext as sc

import compas_rhino


__commandname__ = "IGS_toggle_autoupdate"


def RunCommand(is_interactive):

    if 'IGS' not in sc.sticky:
        compas_rhino.display_message('IGS has not been initialised yet.')
        return

    scene = sc.sticky['IGS']['scene']

    answer = compas_rhino.rs.GetString("Autoupdate of Form/Force Diagram", "Cancel", ["On", "Off", "Cancel"])
    if answer == "On":
        scene.settings['IGS']['autoupdate'] = True
        compas_rhino.display_message("Autoupdate Form/Force: [On]")
    if answer == "Off":
        scene.settings['IGS']['autoupdate'] = False
        compas_rhino.display_message("Autoupdate Form/Force: [Off]")


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
