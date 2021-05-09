from guizero import App

def test_window_icon():
    app = App(title="Window should have an icon")
    app.icon = "../examples/guizero.png"
    assert app.icon == "../examples/guizero.png"
    assert app._icon.tk_image is not None
    app.destroy()

def test_window_icon_different_file_formats():
    app = App(title="GIF icon test")
    app.icon = "../examples/guizero.gif"
    assert app.icon == "../examples/guizero.gif"
    assert app._icon.tk_image is not None
    app.destroy()
    app = App(title="JPG icon test")
    app.icon = "../examples/guizero.jpg"
    assert app.icon == "../examples/guizero.jpg"
    assert app._icon.tk_image is not None
    app.destroy()

