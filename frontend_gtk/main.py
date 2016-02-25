import pygtk
pygtk.require("2.0")
import gtk
import gtk.glade
import requests

class LoginWindow:

    def __init__(self):
        self.glade = gtk.Builder()
        self.glade.add_from_file("form_login.glade")
        self.glade.connect_signals(self)
        self.main_window = self.glade.get_object("main_dialog")
        self.main_window.connect("destroy", gtk.main_quit)
        self.main_window.show_all()

    def on_MainWindow_delete_event(self, widget, event):
        gtk.main_quit()

    def on_btn_cancel_pressed(self, evt):
        gtk.main_quit()

    def on_btn_login_pressed(self, evt):
        txt_username = self.glade.get_object('txt_username').get_text()
        txt_password = self.glade.get_object('txt_password').get_text()
        print(txt_username, txt_password)

        login_sukses = False

        url = 'http://127.0.0.1:8080/login_json/{}/{}'.format(txt_username,txt_password)
        print('Communicating with backend server... please wait...')
        r = requests.get(url)
        d = r.json()
        print('Result from server {}'.format(d['login_status']))

        login_sukses = d['login_sukses']

        parent = self.main_window
        if login_sukses:
            md = gtk.MessageDialog(parent, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "Login succeed")
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()
        else:
            md = gtk.MessageDialog(parent, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Login failed")
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()

if __name__ == "__main__":
    try:
        a = LoginWindow()
        gtk.main()
    except KeyboardInterrupt:
        pass

