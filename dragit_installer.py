#!/usr/bin/python
# coding=utf-8
import os
import sys

NEED_APT_GET = ['PiCar-V', 'PiSmart']

class Installer_TK(object):
    try:
        import tkinter as tk
    except:
        pass
    import string

    VERSION = "v1.0.0"
    COMPANY = "SunFounder     www.sunfounder.com"

    BACKGROUND_COLOR = '#EEEEEE'
    FOREGROUND_COLOR = '#202020'
    ERROR_COLOR = '#FA0F0F'

    _alphabets = list(string.ascii_lowercase)

    def __init__(self):
        # Get avalible disks
        self.top = self.tk.Tk()
        self.top.title('SunFounder Dragit installer')
        main_frame = self.tk.Frame(self.top, width=800)
        info_frame = self.tk.Frame(self.top)
        installer_frame = self.tk.Frame(main_frame, width=360)
        frame_lable_1 = self.tk.Frame(installer_frame)
        frame_lable_2 = self.tk.Frame(installer_frame)
        frame_selector = self.tk.Frame(installer_frame)
        frame_all = self.tk.Frame(frame_selector)
        frame_dragit = self.tk.Frame(frame_selector)
        frame_modules = self.tk.Frame(frame_selector)
        frame_picar_v = self.tk.Frame(frame_selector)
        frame_picar_s = self.tk.Frame(frame_selector)
        frame_pismart = self.tk.Frame(frame_selector)
        frame_install = self.tk.Frame(frame_selector)
        self.install_all = self.tk.IntVar()
        self.install_dragit = self.tk.IntVar()
        self.install_modules = self.tk.IntVar()
        self.install_picar_v = self.tk.IntVar()
        self.install_picar_s = self.tk.IntVar()
        self.install_pismart = self.tk.IntVar()
        #self.message = self.tk.StringVar(frame_1_7)
        #self.message.set('')

        main_1_lable   = self.tk.Label(frame_lable_1, text="Dragit installer", fg=self.FOREGROUND_COLOR)
        main_2_lable   = self.tk.Label(frame_lable_2, text="Select the modules you want to install", fg=self.FOREGROUND_COLOR)
        
        self.all_check      = self.tk.Checkbutton(frame_all, text="All", variable=self.install_all, command=self.changes_all)
        layer_1_1           = self.tk.Label(frame_dragit, text="└-", fg=self.FOREGROUND_COLOR)
        self.dragit_check   = self.tk.Checkbutton(frame_dragit, text="Dragit", variable=self.install_dragit, command=self.changes_dragit)
        layer_1_2           = self.tk.Label(frame_modules, text="└-", fg=self.FOREGROUND_COLOR)
        self.modules_check  = self.tk.Checkbutton(frame_modules, text="Extentions", variable=self.install_modules, command=self.changes_modules)
        layer_2_1           = self.tk.Label(frame_picar_v, text="    └-", fg=self.FOREGROUND_COLOR)
        self.picar_v_check  = self.tk.Checkbutton(frame_picar_v, text="PiCar-V", variable=self.install_picar_v, command=self.changes_picar_v)
        layer_2_2           = self.tk.Label(frame_picar_s, text="    └-", fg=self.FOREGROUND_COLOR)
        self.picar_s_check  = self.tk.Checkbutton(frame_picar_s, text="PiCar-S", variable=self.install_picar_s, command=self.changes_picar_s)
        layer_2_3           = self.tk.Label(frame_pismart, text="    └-", fg=self.FOREGROUND_COLOR)
        self.pismart_check  = self.tk.Checkbutton(frame_pismart, text="PiSmart", variable=self.install_pismart, command=self.changes_pismart)
        install_button = self.tk.Button(frame_install, width=10, text='Install')

        # Pack 
        main_frame.pack(fill="both")
        info_frame.pack(side=self.tk.BOTTOM,fill="both")

        installer_frame.pack(padx=20, pady=20, fill="both")

        frame_lable_1.pack(pady=10, side=self.tk.TOP,fill="both")
        frame_lable_2.pack(side=self.tk.TOP,fill="both")
        frame_selector.pack(padx=30, side=self.tk.TOP,fill="both")
        frame_all.pack(pady=0, side=self.tk.TOP,fill="both")
        frame_dragit.pack(pady=0, side=self.tk.TOP,fill="both")
        frame_modules.pack(pady=0, side=self.tk.TOP,fill="both")
        frame_picar_v.pack(pady=0, side=self.tk.TOP,fill="both")
        frame_picar_s.pack(pady=0, side=self.tk.TOP,fill="both")
        frame_pismart.pack(pady=0, side=self.tk.TOP,fill="both")

        frame_install.pack(side=self.tk.TOP,fill="both")

        main_1_lable.pack(side=self.tk.LEFT)
        main_2_lable.pack(side=self.tk.LEFT)
        self.all_check.pack(side=self.tk.LEFT)
        layer_1_1.pack(side=self.tk.LEFT)
        self.dragit_check.pack(side=self.tk.LEFT)
        layer_1_2.pack(side=self.tk.LEFT)
        self.modules_check.pack(side=self.tk.LEFT)
        layer_2_1.pack(side=self.tk.LEFT)
        self.picar_v_check.pack(side=self.tk.LEFT)
        layer_2_2.pack(side=self.tk.LEFT)
        self.picar_s_check.pack(side=self.tk.LEFT)
        layer_2_3.pack(side=self.tk.LEFT)
        self.pismart_check.pack(side=self.tk.LEFT)
        install_button.pack(side=self.tk.RIGHT)

        # Setup
        self.top.resizable(width=False, height=False)
        #self.top.geometry('{}x{}'.format(300, 350))
        install_button.bind('<ButtonRelease-1>', self.install)
        self.dragit_check.select()

    def start(self):
        self.top.mainloop()

    def changes_all(self):
        if self.install_all.get():
            self.dragit_check.select()
            self.modules_check.select()
            self.picar_v_check.select()
            self.picar_s_check.select()
            self.pismart_check.select()
        else:
            self.dragit_check.deselect()
            self.modules_check.deselect()
            self.picar_v_check.deselect()
            self.picar_s_check.deselect()
            self.pismart_check.deselect()

    def changes_modules(self):
        if self.install_modules.get():
            self.picar_v_check.select()
            self.picar_s_check.select()
            self.pismart_check.select()
            if self.install_dragit.get():
                self.all_check.select()
        else:
            self.picar_v_check.deselect()
            self.picar_s_check.deselect()
            self.pismart_check.deselect()
            self.all_check.deselect()

    def changes_dragit(self):
        if self.install_dragit.get():
            if self.install_modules.get():
                self.all_check.select()
        else:
            self.all_check.deselect()

    def changes_picar_v(self):
        if self.install_picar_v.get():
            if self.install_picar_s.get():
                if self.install_pismart.get():
                    self.modules_check.select()
                    if self.install_dragit.get():
                        self.all_check.select()
        else:
            self.all_check.deselect()
            self.modules_check.deselect()

    def changes_picar_s(self):
        if self.install_picar_s.get():
            if self.install_picar_s.get():
                if self.install_pismart.get():
                    self.modules_check.select()
                    if self.install_dragit.get():
                        self.all_check.select()
        else:
            self.all_check.deselect()
            self.modules_check.deselect()

    def changes_pismart(self):
        if self.install_pismart.get():
            if self.install_picar_s.get():
                if self.install_pismart.get():
                    self.modules_check.select()
                    if self.install_dragit.get():
                        self.all_check.select()
        else:
            self.all_check.deselect()
            self.modules_check.deselect()

    def install(self, event):
        print("install_dragit: %s"%self.install_dragit.get())
        print("install_picar_v: %s"%self.install_picar_v.get())
        print("install_picar_s: %s"%self.install_picar_s.get())
        print("install_pismart: %s"%self.install_pismart.get())
        results = []
        if self.install_dragit.get():
            results.append('Dragit')
        if self.install_picar_v.get():
            results.append('PiCar-V')
        if self.install_picar_s.get():
            results.append('PiCar-S')
        if self.install_pismart.get():
            results.append('PiSmart')
        results = ' '.join(results)
        print("results: %s"%results)
        install_modules(results)

class Installer_whiptail(object):
    def __init__(self):
        pass

    def start(self):
        dialog = 'answer=$(whiptail --title "Dragit Installer" --checklist \
        "Choose what you need to install" 20 78 4 \
        "Dragit" "Install Dragit" ON \
        "PiCar-V" "Install OpenCV for PiCar-V" OFF \
        "PiCar-S" "Install NOTHING for PiCar-S (No need)" OFF \
        "PiSmart" "Install dependences and modules od PiSmart" OFF 3>&1 1>&2 2>&3) && \
        echo "answer = "$answer && \
        echo $answer > dragit_installer.tmp'
        os.system(dialog)
        fp = open('dragit_installer.tmp', 'r')
        results = fp.read().strip()
        fp.close()
        print("results: %s"%results)
        os.system('rm dragit_installer.tmp')
        install_modules(results)

def install_modules(results):
    print('results: %s'%results)
    modules = results.replace('"', '').split(' ')
    for n_module in NEED_APT_GET:
        if n_module in modules:
            print('Updating apt-get')
            os.system('sudo apt-get update')
            break
    for module in modules:
        install(module)

def install(module):
    if module == 'Dragit':
        r = os.system('ls /opt/SunFounder_Dragit')
        if r == 0:
            print("Dragit already downloaded, updating...")
            cmd = 'cd /opt/SunFounder_Dragit && git pull origin master && sudo ./install'
        else:
            print("\nInstalling Dragit...")
            cmd = '\
            cd /opt && \
            git clone https://github.com/sunfounder/SunFounder_Dragit.git && \
            cd SunFounder_Dragit && \
            sudo ./install'
        r = os.system(cmd)
        if r == 0:
            print("Done")
        else:
            print("Error")
    elif module == 'PiCar-V':
        r = os.system('ls /home/pi/SunFounder_PiCar-V')
        if r == 0:
            print("PiCar-V already downloaded, updating...")
            cmd = 'cd /home/pi/SunFounder_PiCar-V && git pull origin master && sudo ./install_dependencies'
        else:
            print("\nInstalling PiCar-V...")
            cmd = '\
            cd /home/pi && \
            git clone https://github.com/sunfounder/SunFounder_PiCar-V.git && \
            cd SunFounder_PiCar-V && \
            sudo ./install_dependencies'
        r = os.system(cmd)
        if r == 0:
            print("Done")
        else:
            print("Error")
    elif module == 'PiCar-S':
        print("\nInstalling PiCar-S...")
        print('Do nothing')
    elif module == 'PiSmart':
        r = os.system('ls /home/pi/SunFounder_PiSmart')
        if r == 0:
            print("PiSmart already downloaded, updating...")
            cmd = 'cd /home/pi/SunFounder_PiSmart && git pull origin master && sudo ./install'
        else:
            print("\nInstalling PiSmart")
            cmd = '\
            cd /home/pi && \
            git clone https://github.com/sunfounder/SunFounder_PiSmart.git && \
            cd SunFounder_PiSmart && \
            sudo ./install'
        r = os.system(cmd)
        if r == 0:
            print("Done")
        else:
            print("Error")
    else:
        print("Error, no module named %s"%module)

def main():
    euid = os.geteuid()
    if euid != 0:
        print("Script not started as root. Running sudo..")
        args = ['sudo', sys.executable] + sys.argv + [os.environ]
        # the next line replaces the currently-running process with the sudo
        os.execlpe('sudo', *args)

    print('Running. Your euid is %s'% euid)
    try:
        d = Installer_TK()
    except:
        d = Installer_whiptail()
    d.start()

if __name__ == '__main__':
    main()
