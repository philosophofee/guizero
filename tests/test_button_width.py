from guizero import App, PushButton

def test_button_border_width():
    app = App()
    button = PushButton(app, text="Border width 20")
    button.borderwidth = 20
    assert button.borderwidth == 20  # testing getter, which i had trouble with
    app.destroy()