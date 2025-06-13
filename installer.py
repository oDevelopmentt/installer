from generatedCustomization import *
from download import *
from guizero import *



def install():
    download_file(appCustomization.getSource())

app = App(title=f"{appCustomization.getFullName()} Installer")
if appCustomization.getIcon():
    app.tk.iconbitmap(appCustomization.getIcon())
text = Text(app, text=f"{appCustomization.getFullName()} Installer")
button = PushButton(app, text=f"Install {appCustomization.getName()}", command=install)
app.display()