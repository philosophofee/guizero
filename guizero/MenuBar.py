from tkinter import Menu
from .tkmixins import ScheduleMixin, DestroyMixin, FocusMixin
from . import utilities as utils
from .base import Component
from .App import App
from .Window import Window

class MenuBar(Component):

    def __init__(self, master, menudict):

        """
        Creates a MenuBar

        :param Container master:
            The Container (App, Box, etc) the MenuBar will belong too.

        :param Dict menudict
            A dictionary that contains all of the menus and their sub-menus
            e.g ::
                  {
                      "foo": {
                          "foo1": callback,
                          "foo2": callback
                      },
                      "bar": {
                          "bar1": callback,
                          "bar2": callback
                      }
                  }
        """

        if not isinstance(master, (App, Window)):
            utils.error_format("The [MenuBar] must have an [App] or [Window] object as its master")

        # Create a tk Menu object within this object
        tk = Menu(master.tk)

        super(MenuBar, self).__init__(master, tk, False)

        # Keep track of submenu objects
        self._sub_menus = []

        # Create all the top level menus
        i = 0
        for menu_item in menudict:
            # Create this submenu
            new_menu = Menu(self.tk, tearoff=0)

            # Populate the drop down menu with the items/commands from the list
            for k in menudict[menu_item]:
                new_menu.add_command(label=k, command=menudict[menu_item].get(k))

            # Append to the submenus list
            self._sub_menus.append(new_menu)

            # Add to the menu bar
            self.tk.add_cascade(label=menu_item, menu=self._sub_menus[i])
            i+=1

       	# Set this as the menu for the master object
       	master.tk.config(menu=self.tk)

    @property
    def bg(self):
        """
        Sets the background color of the widget.

        Note - some operating systems dont allow the background color of the 
        menu bar to be changed. 
        """
        return super(MenuBar, self.__class__).bg.fget(self)

    # Set the background colour
    @bg.setter
    def bg(self, color):
        super(MenuBar, self.__class__).bg.fset(self, color)
        for sub_menu in self._sub_menus:
            sub_menu["bg"] = utils.convert_color(color)
    