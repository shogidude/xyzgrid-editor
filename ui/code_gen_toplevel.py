import tkinter as tki
from tkinter import RIGHT, BOTH
from tkinter import Text

pre_map = r'''
"""
This is the xyzgrid map generated from the editor.
"""
from evennia.contrib.grid.xyzgrid import xymap_legend

MAP_NAME = r"""
'''

post_map = r'''
"""

# Setting up teleports within the same map grid
LEGEND_FOR_MAP = {
    't': xymap_legend.TeleporterMapLink,
    'p': xymap_legend.TeleporterMapLink,
    'q': xymap_legend.TeleporterMapLink,
}

PROTOTYPES_LEVEL_NAME = {
    (0, 0): {
        "prototype_parent": "xyz_room",
        "key": "A specific room",
        "desc": "Specific stuff everywhere."
    },
    (0, 0, 'e'): {
        "prototype_parent": "xyz_exit",
        "desc": "A specific exit description"
    },
    ('*', '*'): {
        "prototype_parent": "xyz_room",
        "key": "Endless generic rooms",
        "desc": "Generic room description."
    },
    ('*', '*', '*'): {
        "prototype_parent": "xyz_exit",
        "desc": "Generic exit"
    }
}

# define all information describing this map
SOME_LEVEL = {
    "map": MAP_NAME,
    "zcoord": "level name",
    "legend": LEGEND_FOR_MAP,
    "prototypes": PROTOTYPES_LEVEL_NAME,
    "options": {"map_visual_range": 1, "map_mode": "scan"},
}

# This is read by the parser
XYMAP_DATA_LIST = [SOME_LEVEL]


'''

class CodeGenToplevel(object):

    def __init__(self, root):

        # creating code
        map_code = pre_map + "my map!!!" + post_map

        # create the GUI to display the map code
        root.update_idletasks()

        dialog_width = 800
        dialog_height = 400

        at_y = int(root.winfo_rooty() + (root.winfo_height() / 4) - (dialog_height/2))
        at_x = int(root.winfo_rootx() + (root.winfo_width() / 2) - (dialog_width/2))

        self.top = tki.Toplevel(root)
        self.top.geometry(f"{dialog_width}x{dialog_height}+{at_x}+{at_y}")
        self.top.title('Xyzgrid code ...')

        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        inner_frame = tki.Frame(frm, borderwidth=2)
        inner_frame.pack(fill=BOTH, expand=True)

        text_box = Text(
            inner_frame,
            height=20,
            width=80
        )
        text_box.pack(expand=True)
        text_box.insert('end', map_code)
        text_box.config(state='disabled')

        #close the window
        b_submit = tki.Button(frm, text='Close')
        b_submit['command'] = lambda: self.close_window()
        b_submit.pack(side=RIGHT, padx=5, pady=5)

        self.top.grab_set()


    def close_window(self):
        try:
            self.top.destroy()
        except:
            print("Something went wrong closing the window.")
