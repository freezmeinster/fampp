#!/usr/bin/env python

import gtk
import os 

class ControlPanel(gtk.Window):
    counter = 1

    
    def __init__(self, parent=None):
        # Create the toplevel window
        gtk.Window.__init__(self)
        try:
            self.set_screen(parent.get_screen())
        except AttributeError:
            self.connect('destroy', lambda *w: gtk.main_quit())
        
        self.set_title("Web Server Control Penel")
        self.set_border_width(25)             
        main_vbox = gtk.VBox()
        self.add(main_vbox)          

        frame_apache = gtk.Frame("Apache")
        main_vbox.pack_start(frame_apache, padding=10)
 
        vbox = gtk.VBox(False, 16)
        vbox.set_border_width(16)
        frame_apache.add(vbox)

        hbox = gtk.HBox(False, 16)
        vbox.pack_start(hbox)
        button = gtk.Button(stock='gtk-execute')
        button.connect('clicked', self.apache_start)
        hbox.pack_start(button, False, False, 0)

        button = gtk.Button(stock='gtk-stop')
        button.connect('clicked', self.apache_stop)
        hbox.pack_start(button, False, False, 0)
         
        button = gtk.Button(stock='gtk-refresh')
        button.connect('clicked', self.apache_restart)
        hbox.pack_start(button, False, False, 0)

        frame_mysql = gtk.Frame("Mysql")
        main_vbox.pack_start(frame_mysql, padding=10)
 
        vbox = gtk.VBox(False, 16)
        vbox.set_border_width(16)
        frame_mysql.add(vbox)

        hbox = gtk.HBox(False, 16)
        vbox.pack_start(hbox)
        button = gtk.Button(stock='gtk-execute')
        button.connect('clicked', self.mysqld_start)
        hbox.pack_start(button, False, False, 0)

        button = gtk.Button(stock='gtk-stop')
        button.connect('clicked', self.mysqld_stop)
        hbox.pack_start(button, False, False, 0)
         
        button = gtk.Button(stock='gtk-refresh')
        button.connect('clicked', self.mysqld_restart)
        hbox.pack_start(button, False, False, 0)
        
        self.show_all()
         

    def apache_start(self, button):
		dialog = gtk.MessageDialog(self,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                "Apache http server started")
                
		dialog.run()
                os.system("/usr/local/sbin/httpd -k start")
		dialog.destroy()
		 
	
    def apache_stop(self, button):
               
		dialog = gtk.MessageDialog(self,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_WARNING, gtk.BUTTONS_OK,
                "Apache http server stoped")
                dialog.run()               
                os.system("killall httpd")
                dialog.destroy()
			
	
    def apache_restart(self, button):
        
		dialog = gtk.MessageDialog(self,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                "Apache http server restarted")
                os.system("killall httpd")
                os.system("/usr/local/sbin/httpd -k start")
                
		dialog.run()
		dialog.destroy()
        
    def mysqld_start(self, button):
		dialog = gtk.MessageDialog(self,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                "Mysqld database server started")
                os.system("xmessage \"nguk\"")
		dialog.run()
		dialog.destroy()
		 
	
    def mysqld_stop(self, button):
               
		dialog = gtk.MessageDialog(self,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_WARNING, gtk.BUTTONS_OK,
                "Mysqld database  server stoped")
		dialog.run()
		dialog.destroy()
			
	
    def mysqld_restart(self, button):
        
		dialog = gtk.MessageDialog(self,
                gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
                gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
                "Mysqld database  server restarted")
		dialog.run()
		dialog.destroy()    
        
def main():
    ControlPanel()
    gtk.main()

if __name__ == '__main__':
    main()

