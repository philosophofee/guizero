from guizero import App, PushButton, MenuBar


def pressed():
    print("button was pressed")


def message(msg):
    print(msg)


def menuItemPressed():
    print("Menu bar item was pressed")


def menuItemExit():
    exit()


app = App()
# sets icon as png
app.icon = "guizero.png"

button = PushButton(app, command=pressed, text='Press me')
button_with_args = PushButton(app, command=message, text='Say hi', args=["hi"])

# set background color for the buttons
button.bg = "#ff0000"
button_with_args.bg = "pink"

# set border width for the second button
button_with_args.borderwidth = 8

# set a menu bar
m = MenuBar(app,
            {
                "File": {
                    "Close": menuItemExit
                },
                "Edit": {
                    "edit1": menuItemPressed,
                    "edit2": menuItemPressed
                }
            })

app.display()
