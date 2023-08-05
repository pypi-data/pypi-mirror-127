from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

import os
import errno
import shelve

import scriptcontext as sc

import compas
import compas_rhino

from compas.rpc import Proxy
from compas_igs.rhino import Scene
from compas_igs.rhino import Browser
from compas_igs.activate import check
from compas_igs.activate import activate


__commandname__ = "IGS__init"


# the current working directory could be the APPTEMP directory for IGS
# until it is specified by the user
HERE = compas_rhino.get_document_dirname()
HOME = os.path.expanduser('~')
CWD = HERE or HOME


SETTINGS = {
    'IGS': {
        'autoupdate': False,
        'bi-directional': False,
        'max_deviation': 0.1,
    }
}


def RunCommand(is_interactive):

    if check():
        print("Current plugin is already activated")
    else:
        compas_rhino.rs.MessageBox("Detected environment change, re-activating plugin", 0, "Re-activating Needed")
        if activate():
            compas_rhino.rs.MessageBox("Restart Rhino for the change to take effect", 0, "Restart Rhino")
        else:
            compas_rhino.rs.MessageBox("Someting wrong during re-activation", 0, "Error")
        return

    shelvepath = os.path.join(compas.APPTEMP, 'IGS', '.history')
    if not os.path.exists(os.path.dirname(shelvepath)):
        try:
            os.makedirs(os.path.dirname(shelvepath))
        except OSError as error:
            if error.errno != errno.EEXIST:
                raise

    db = shelve.open(shelvepath, 'n')
    db['states'] = []

    scene = Scene(db, 20, SETTINGS)
    scene.purge()

    sc.sticky["IGS"] = {
        'proxy': Proxy(),
        'system': {
            "session.dirname": CWD,
            "session.filename": None,
            "session.extension": 'igs'
        },
        'scene': scene,
    }

    scene.update()

    # would be useful to add a notification about the cloud: new / reconnect
    # compas_rhino.display_message("IGS has started.")
    Browser()


# ==============================================================================
# Main
# ==============================================================================

if __name__ == '__main__':

    RunCommand(True)
