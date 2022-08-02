import sys
import gi
import conf as ini

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')

from gi.repository import Gtk, Adw, Gio, GLib
from data import Environement

class LoadConfig():
    def __init__(self):
        print('hello')
        #Load Environement
        self.path = ini.load("ENVIRONEMENT", "path", 0)
        self.term = ini.load("ENVIRONEMENT", "term", 2)
        self.log_file = ini.load("ENVIRONEMENT", "log_file", 2)
        self.log_view = ini.load("ENVIRONEMENT", "log_view", 2)
        self.event_file = ini.load("ENVIRONEMENT", "event_file", 2)
        self.event_log = ini.load("ENVIRONEMENT", "event_log", 2)

        #Load Time
        self.log_time = ini.load("TIME", "log_time", 1)
        self.log_step = ini.load("TIME", "log_step", 1)
        self.event_step = ini.load("TIME", "event_step", 1)

        #Log Sensor
        self.humid = ini.load("SENSORS", "humid", 2)
        self.presure = ini.load("SENSORS", "presure", 2)
        self.temp = ini.load("SENSORS", "temp", 2)
        self.orientation = ini.load("SENSORS", "orientation", 2)
        self.Accel = ini.load("SENSORS", "Accel", 2)

    def get(self, info):
        switch={
        "path": self.path,
        "term": self.term,
        "log_file": self.log_file,
        "log_view": self.log_view,
        "event_file": self.event_file,
        "event_log": self.event_log,
        "log_time": self.log_time,
        "log_step": self.log_step,
        "event_step": self.event_step,
        "humid": self.humid,
        "presure": self.presure,
        "temp": self.temp,
        "orientation": self.orientation,
        "Accel": self.Accel
        }
        return switch.get(info, "err")

    def modif(self, info, modif):

        if "path" == info:
            ini.modify("ENVIRONEMENT", "path", modif)
        elif "term" == info:
            ini.modify("ENVIRONEMENT", "term", modif)
        elif "log_file" == info:
            ini.modify("ENVIRONEMENT", "log_file", modif)
        elif "log_view" == info:
            ini.modify("ENVIRONEMENT", "log_view", modif)
        elif "event_file" == info:
            ini.modify("ENVIRONEMENT", "event_file", modif)
        elif "event_log" == info:
            ini.modify("ENVIRONEMENT", "event_log", modif)
        elif "log_time" == info:
            ini.modify("TIME", "log_time", modif)
        elif "log_step" == info:
            ini.modify("TIME", "log_step", modif)
        elif "event_step" == info:
            ini.modify("TIME", "event_step", modif)
        elif "humid" == info:
            ini.modify("SENSORS", "humid", modif)
        elif "presure" == info:
            ini.modify("SENSORS", "presure", modif)
        elif "temp" == info:
            ini.modify("SENSORS", "temp", modif)
        elif "orientation" == info:
            ini.modify("SENSORS", "orientation", modif)
        elif "Accel" == info:
            ini.modify("SENSORS", "Accel", modif)

    def destroy(self):
        del self.path
        del self.term
        del self.log_file
        del self.log_view
        del self.event_file
        del self.event_log

        #Load Time
        del self.log_time
        del self.log_step
        del self.event_step

        #Log Sensor
        del self.humid
        del self.presure
        del self.temp
        del self.orientation
        del self.Accel



class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        self.config = LoadConfig()
        self.config.modif("term", "false")
        super().__init__(*args, **kwargs)
        self.mainBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.envBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.timeBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.sensorBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.mainBox)

        self.envSeparator_env = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        self.envSeparator_time = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)

        self.mainBox.append(self.envBox)
        self.mainBox.append(self.envSeparator_env)

        self.mainBox.append(self.timeBox)
        self.mainBox.append(self.envSeparator_time)

        self.mainBox.append(self.sensorBox)

        self.mainBox.set_spacing(5)
        self.envBox.set_spacing(5)
        self.timeBox.set_spacing(5)
        self.sensorBox.set_spacing(5)

        label_env = Gtk.Label()
        label_env.set_markup("<big><b>ENVIRONEMENT</b></big>")
        self.envBox.append(label_env)

        label_time = Gtk.Label()
        label_time.set_markup("<big><b>Temps</b></big>")
        self.timeBox.append(label_time)

        label_sensor = Gtk.Label()
        label_sensor.set_markup("<big><b>Capteur</b></big>")
        self.sensorBox.append(label_sensor)

        self.generate_spin(0.1, "Durrée d'un log en MS", "log_time")
        self.generate_spin(0.1, "délai d'un log", "log_step")
        self.generate_spin(0.1, "délai d'un vent", "event_step")
        #self.tesst_slide()
        self.tesst_top()
        self.tesst_about()
        self.path_entry()

        self.generate_stwitched(self.envBox, "Terminal", "term")
        self.generate_stwitched(self.envBox, "Sauvegarde log", "log_file")
        self.generate_stwitched(self.envBox, "Sauvegarde log", "log_file")
        self.generate_stwitched(self.envBox, "Sauvegarde event", "log_view")
        self.generate_stwitched(self.envBox, "Sauvegarde event", "event_log")
        self.generate_stwitched(self.sensorBox, "Humidité", "humid")
        self.generate_stwitched(self.sensorBox, "Pression", "presure")
        self.generate_stwitched(self.sensorBox, "Température", "temp")
        self.generate_stwitched(self.sensorBox, "Orientation", "orientation")
        self.generate_stwitched(self.sensorBox, "Acceléromètre", "Accel")

        self.config.destroy()

        self.set_default_size(600, 250)
        self.set_title("Sensor Log")

    def on_value_changed(self, scroll):
        print(self.spinbutton.get_value_as_int())

    def tesst_slide(self):
        self.slider = Gtk.Scale()
        self.slider.set_digits(0)  # Number of decimal places to use
        self.slider.set_range(0, 10)
        self.slider.set_draw_value(True)  # Show a label with current value
        self.slider.set_value(5)  # Sets the current value/position
        self.slider.connect('value-changed', self.slider_changed)
        self.envBox.append(self.slider)

    def tesst_top(self):
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        self.open_button = Gtk.Button(label="Open")
        self.header.pack_start(self.open_button)
        self.open_dialog = Gtk.FileChooserNative.new(title="Choose a file",
                                                     parent=self, action=Gtk.FileChooserAction.OPEN)

        self.open_dialog.connect("response", self.open_response)
        self.open_button.connect("clicked", self.show_open_dialog)

    def tesst_about(self):
        action = Gio.SimpleAction.new("something", None)
        action.connect("activate", self.print_something)
        self.add_action(action)  # Here the action is being added to the window, but you could add it to the
                                 # application or an "ActionGroup"

        # Create a new menu, containing that action
        menu = Gio.Menu.new()
        menu.append("Do Something", "win.something")  # Or you would do app.something if you had attached the
                                                      # action to the application
        # Create a popover
        self.popover = Gtk.PopoverMenu()  # Create a new popover menu
        self.popover.set_menu_model(menu)

        # Create a menu button
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")  # Give it a nice icon

        # Add menu button to the header bar
        self.header.pack_end(self.hamburger)

         # Set app name
        GLib.set_application_name("My App")

        # Create an action to run a *show about dialog* function we will create 
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.show_about)
        self.add_action(action)
        
        menu.append("About", "win.about")  # Add it to the menu we created in previous section

    def show_about(self, action, param):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self)  # Makes the dialog always appear in from of the parent window
        self.about.set_modal(self)  # Makes the parent window unresponsive while dialog is showing

        self.about.set_authors(["DaemonWhite"])
        self.about.set_copyright("Copyright 2022 DaemonWhite")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("http://ia-ultime.tplinkdns.com")
        self.about.set_website_label("ia-ultime.tplinkdns")
        self.about.set_version("0.0.1a")
        self.about.set_logo_icon_name("com.daemonwhite.sensorlog")  # The icon will need to be added to appropriate location
                                                 # E.g. /usr/share/icons/hicolor/scalable/apps/org.example.example.svg

        self.about.show()

    def print_something(self, action, param):
        print("Something!")


    def show_open_dialog(self, button):
        f = Gtk.FileFilter()
        f.set_name("Image files")
        f.add_mime_type("image/jpeg")
        f.add_mime_type("image/png")
        self.open_dialog.add_filter(f)
        self.open_dialog.show()

    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            filename = file.get_path()
            print(filename)

    def slider_changed(self, slider):
        print(int(slider.get_value()))

    def path_entry(self):
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Chemin absolue")
        self.entry.set_text(self.config.get("path"))
        self.envBox.append(self.entry)

    def generate_spin(self, step, name, conf):
        adjustment = Gtk.Adjustment(upper=100000.0, step_increment=step, page_increment=step)
        self.spinbutton = Gtk.SpinButton()
        self.spinbutton.set_adjustment(adjustment)
        self.spinbutton.set_climb_rate(1.0)
        self.spinbutton.set_digits(1)
        self.spinbutton.set_value(self.config.get(conf))
        self.spinbutton.connect("value-changed", self.on_value_changed)
        self.spinbutton.set_numeric(True)

        spinbutton_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        spinbutton_box.append(self.spinbutton)
        self.timeBox.append(spinbutton_box)

        self.label_term = Gtk.Label(label=name)
        spinbutton_box.append(self.label_term)
        spinbutton_box.set_spacing(5) 


    def generate_stwitched(self, box, name, conf):

        self.switch = Gtk.Switch()
        self.switch.set_active(self.config.get(conf))  # Let's default it to on
        self.switch.connect("state-set", self.switch_switched, conf) # Lets trigger a function

        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.switch_box.append(self.switch)
        box.append(self.switch_box)

        self.label_term = Gtk.Label(label=name)
        self.switch_box.append(self.label_term)
        self.switch_box.set_spacing(5) 

    def switch_switched(self, switch, state, conf):
        modif="false"
        print(conf)
        print(f"The switch has been switched {'on' if state else 'off'}")
        if state:
            modif="true"
        self.config.modif(conf, modif)

class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

app = MyApp(application_id="com.daemonwhite.sensorlog")
app.run(sys.argv)