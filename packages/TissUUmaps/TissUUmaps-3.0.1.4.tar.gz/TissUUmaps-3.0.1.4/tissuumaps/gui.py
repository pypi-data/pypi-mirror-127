
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox, QPlainTextEdit, QDialog, QSplashScreen, QProgressDialog, QMainWindow, QToolBar, QAction, QStyle
from PyQt5.QtWebChannel import QWebChannel
from PyQt5 import QtGui 
from PyQt5.QtGui import QDesktopServices
from optparse import OptionParser

from pathlib import Path
from urllib.parse import urlparse
from urllib.parse import parse_qs
import subprocess

import threading, time
import sys
import socket

import urllib.parse
import urllib.request
import os
import json

from tissuumaps import views

class CustomWebEnginePage(QWebEnginePage):
    """ Custom WebEnginePage to customize how we handle link navigation """

    def acceptNavigationRequest(self, url,  _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url)
            return False
        return True
    
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        print (level, msg, line, sourceID)
    
class textWindow(QDialog):
    def __init__(self, parent, title, message):
        QDialog.__init__(self, parent)

        self.setMinimumSize(QSize(700, 500))    
        self.setWindowTitle(title) 

        # Add text field
        self.b = QPlainTextEdit(self)
        self.b.setMinimumSize (650,450)
        self.b.setReadOnly(True)
        self.b.insertPlainText(message)
        self.b.move(10,10)
        self.b.resize(400,200)


class MainWindow(QMainWindow):
    def __init__(self, qt_app, app, *args, **kwargs):
        super(MainWindow, self).__init__()
        self.resize(1400,1000)

        self.browser = webEngine(qt_app, app, self, *args)
        
        self.setCentralWidget(self.browser)
  
        #self.status = QStatusBar()
        #self.setStatusBar(self.status)
        
        bar = self.menuBar()
        file = bar.addMenu("File")

        open = QAction(self.style().standardIcon(QStyle.SP_DialogOpenButton), "Open",self)
        open.setShortcut("Ctrl+O")
        file.addAction(open)
        open.triggered.connect(self.browser.openImage)

        save = QAction(self.style().standardIcon(QStyle.SP_DialogSaveButton), "Save project",self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        def trigger():
            self.browser.page().runJavaScript("flask.standalone.saveProject();")
        save.triggered.connect(trigger)

        exit = QAction(self.style().standardIcon(QStyle.SP_DialogCancelButton), "Exit",self)
        exit.setShortcut("Ctrl+Q")
        file.addAction(exit)
        exit.triggered.connect(self.close)

        #edit = file.addMenu("Edit")
        #edit.addAction("copy")
        #edit.addAction("paste")
        
        plugins = bar.addMenu("Plugins")
        for pluginName in app.config["PLUGINS"]:
            plugin = QAction(pluginName,self)
            plugins.addAction(plugin)
            def trigger():
                print ("Plugin triggered:", pluginName)
                self.browser.page().runJavaScript("pluginUtils.startPlugin(\""+pluginName+"\");");
            plugin.triggered.connect(trigger)
        
        self.showMaximized()
class webEngine(QWebEngineView):
    def __init__(self, qt_app, app, mainWin, args):
        super().__init__()
        self.setAcceptDrops(True)
        self.qt_app = qt_app
        self.app = views.app
        self.args = args
        self.setMinimumSize(800,400)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.lastdir = str(Path.home())
        self.setPage(CustomWebEnginePage(self))
        self.webchannel = QWebChannel()
        self.page().setWebChannel(self.webchannel)
        self.webchannel.registerObject('backend', self)
        self.location = None
        self.mainWin = mainWin

        self.mainWin.setWindowTitle("TissUUmaps")
        self.mainWin.resize(1024, 800)
        self.setZoomFactor(1.0)
        self.page().profile().clearHttpCache()
        self.page().profile().downloadRequested.connect(
            self.on_downloadRequested
        )
        self.mainWin.setWindowIcon(QtGui.QIcon('static/misc/favicon.ico')) 
        #self.showMaximized()
    
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
            links = []
            for url in event.mimeData().urls():
                links.append(str(url.toLocalFile()))
            for link in links:
                #link = link.replace("\\","/").replace(self.app.basedir.replace("\\","/"), "")
                #print ("link",link, self.app.basedir)
                if(".tmap") in link:
                    self.openImagePath(link)
                self.page().runJavaScript(f"flask.standalone.addLayer(\"{link}\");")
            #self.emit(SIGNAL("dropped"), links)
        else:
            event.ignore()

    def on_downloadRequested(self, download):
        old_path = download.path()  # download.path()
        suffix = QFileInfo(old_path).suffix()
        print (suffix)
        path, _ = QFileDialog.getSaveFileName(
            self, "Save File", old_path, "*." + suffix
        )
        if path:
            download.setPath(path)
            download.accept()

            def openImageThread():
                for i in range(100):
                    if os.path.isfile(path):
                        break
                    time.sleep(0.1)
                else:
                    return
                os.startfile(os.path.normpath(path))
            
            threading.Thread(target=openImageThread,daemon=True).start()
        
    def run (self):
        sys.exit(self.qt_app.exec_())

    def setLocation (self, location):
        self.location = location
        while True:
            try:
                if (urllib.request.urlopen(self.location).getcode() == 200):
                    break
            except:
                pass
            
            print ("Impossible to load",self.location)
            time.sleep(0.1)
        print ("loading page ", self.location)
        if (len(self.args) > 0):
            if not self.openImagePath(self.args[0]):
                self.load(QUrl(self.location))
        else:
            self.load(QUrl(self.location))
            
    @pyqtSlot(str)
    def getProperties(self, path):
        try:
            path = urllib.parse.unquote(path)[:-4]
            print (path)
            slide = views._get_slide(path)
            propString = "\n".join([n + ": " + v for n,v in slide.properties.items()])
        except:
            propString = ""
        
        messageBox = textWindow(self,os.path.basename(path) + " properties", propString)
        messageBox.show()
        
    def openImage(self):
        folderpath = QFileDialog.getOpenFileName(self, 'Select a File',self.lastdir)[0]
        self.openImagePath(folderpath)

    


    @pyqtSlot(str)
    def saveProject(self, state):
        def addRelativePath(state, relativePath):
            def addRelativePath_aux (state, path):
                if len(path) == 1:
                    if isinstance(state[path[0]], list):
                        state[path[0]] = [relativePath + "/" + s for s in state[path[0]]]
                    else:
                        state[path[0]] = relativePath + "/" + state[path[0]]
                    return
                if not path[0] in state.keys():
                    return
                else:
                    if isinstance(state[path[0]], list):
                        for state_ in state[path[0]]:
                            addRelativePath_aux (state_, path[1:])
                    else:
                        addRelativePath_aux (state[path[0]], path[1:])
            
            try:
                relativePath = relativePath.replace("\\","/")
                paths = [
                    ["layers","tileSource"],
                    ["markerFiles","path"],
                    ["regionFiles","path"],
                    ["regionFile"]
                ]
                for path in paths:
                    addRelativePath_aux (state, path)
            except:
                import traceback
                print (traceback.format_exc())
                
            return state

        parsed_url = urlparse(self.url().toString())
        previouspath = parse_qs(parsed_url.query)['path'][0]
        previouspath = os.path.abspath(os.path.join(self.app.basedir, previouspath))
        print (previouspath)
        
        folderpath = QFileDialog.getSaveFileName(self, 'Save project as',self.lastdir)[0]
        if (not folderpath):
            return {}

        relativePath = os.path.relpath(previouspath, os.path.dirname(folderpath))
        state = addRelativePath(json.loads(state), relativePath)
        with open(folderpath, "w") as f:
            json.dump(state, f)

    def openImagePath (self, folderpath):
        print ("openImagePath",folderpath)
        try:
            oldBaseDir = self.app.basedir
        except AttributeError:
            oldBaseDir = ""
        self.lastdir = os.path.dirname(folderpath)
        if not folderpath:
            return
        print ("openImagePath",oldBaseDir, folderpath)
        parts = Path(folderpath).parts
        if (not hasattr(self.app, 'cache')):
            setup(self.app)
        self.app.basedir = parts[0]
        imgPath = os.path.join(*parts[1:])
        imgPath = imgPath.replace("\\","/")
        try:
            if not ".tmap" in imgPath:
                views._get_slide(imgPath)
        except:
            self.app.basedir = oldBaseDir
            import traceback
            print (traceback.format_exc())
            QMessageBox.about(self, "Error", "TissUUmaps did not manage to open this image.")

            return False
        print ("Opening:", self.app.basedir, self.location + imgPath, QUrl(self.location + imgPath))

        filename = os.path.basename(imgPath)
        path = os.path.dirname(imgPath)
        self.load(QUrl(self.location + filename + "?path=" + path))
        self.mainWin.setWindowTitle("TissUUmaps - " + os.path.basename(folderpath))
        return True

    @pyqtSlot()
    def exit(self):
        self.close()
        #sys.exit()

    @pyqtSlot(str, str, result="QJsonObject")
    def addLayer(self, path, folderpath):
        if (folderpath == ""):
            folderpath = QFileDialog.getOpenFileName(self, 'Select a File')[0]
        if not folderpath:
            returnDict = {"dzi":None,"name":None}
            return returnDict
        parts = Path(folderpath).parts
        print (self.app.basedir)
        if (self.app.basedir != parts[0]):
            if (not self.app.basedir == "C:\mnt\data\shared"):
                reply = QMessageBox.question(self, "Error", "All layers must be in the same drive. Would you like to open this image only?")
                reply = reply == QMessageBox.Yes
            else:
                reply = True
            if reply:
                self.openImagePath(folderpath)
            returnDict = {"dzi":None,"name":None}
            return returnDict
        imgPath = os.path.join(*parts[1:])
        try:
            views._get_slide(imgPath)
        except:
            import traceback
            print (traceback.format_exc())
            QMessageBox.about(self, "Error", "TissUUmaps did not manage to open this image.")
            returnDict = {"dzi":None,"name":None}
            return returnDict
        path = os.path.abspath(os.path.join(self.app.basedir, path))
        imgPath = os.path.abspath(os.path.join(self.app.basedir, imgPath))
        print (path, os.path.dirname(imgPath))
        relativePath = os.path.relpath(os.path.dirname(imgPath), path) 
        if ".." in relativePath:
            reply = QMessageBox.question(self, "Error", "Impossible to add layers from a parent folder. Would you like to open this image only?")
            if reply == QMessageBox.Yes:
                self.openImagePath(folderpath)
            returnDict = {"dzi":None,"name":None}
            return returnDict
        returnDict = {
            "dzi":relativePath + "/" + os.path.basename(imgPath) + ".dzi",
            "name":os.path.basename(imgPath)
        }
        print ("returnDict", returnDict)
        return returnDict
    
def is_port_in_use(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('localhost', port)) == 0

def main():
    parser = OptionParser(usage='Usage: %prog [options] [slide-directory]')
    parser.add_option('-B', '--ignore-bounds', dest='DEEPZOOM_LIMIT_BOUNDS',
                default=False, action='store_false',
                help='display entire scan area')
    parser.add_option('-c', '--config', metavar='FILE', dest='config',
                help='config file')
    parser.add_option('-d', '--debug', dest='DEBUG', action='store_true',
                help='run in debugging mode (insecure)')
    parser.add_option('-e', '--overlap', metavar='PIXELS',
                dest='DEEPZOOM_OVERLAP', type='int',
                help='overlap of adjacent tiles [1]')
    parser.add_option('-f', '--format', metavar='{jpeg|png}',
                dest='DEEPZOOM_FORMAT',
                help='image format for tiles [jpeg]')
    parser.add_option('-l', '--listen', metavar='ADDRESS', dest='host',
                default='127.0.0.1',
                help='address to listen on [127.0.0.1]')
    parser.add_option('-p', '--port', metavar='PORT', dest='port',
                type='int', default=5000,
                help='port to listen on [5000]')
    parser.add_option('-Q', '--quality', metavar='QUALITY',
                dest='DEEPZOOM_TILE_QUALITY', type='int',
                help='JPEG compression quality [75]')
    parser.add_option('-s', '--size', metavar='PIXELS',
                dest='DEEPZOOM_TILE_SIZE', type='int',
                help='tile size [254]')
    parser.add_option('-D', '--depth', metavar='LEVELS',
                dest='FOLDER_DEPTH', type='int',
                help='folder depth search for opening files [4]')

    (opts, args) = parser.parse_args()
    # Overwrite only those settings specified on the command line
    for k in dir(opts):
        if not k.startswith('_') and getattr(opts, k) is None:
            delattr(opts, k)
    views.app.config.from_object(opts)
    views.app.config["isStandalone"] = True

    qInstallMessageHandler(lambda x,y,z: None)

    fmt = QtGui.QSurfaceFormat()
    fmt.setVersion(4, 1)
    fmt.setProfile(QtGui.QSurfaceFormat.CoreProfile)
    fmt.setSamples(4)
    QtGui.QSurfaceFormat.setDefaultFormat(fmt)

    vp = QtGui.QOpenGLVersionProfile(fmt)
    
    qt_app = QApplication([])

    logo = QtGui.QPixmap('static/misc/design/logo.png')
    logo = logo.scaledToWidth(512, Qt.SmoothTransformation)
    splash = QSplashScreen(logo, Qt.WindowStaysOnTopHint)

    desktop = qt_app.desktop()
    scrn = desktop.screenNumber(QtGui.QCursor.pos())
    currentDesktopsCenter = desktop.availableGeometry(scrn).center()
    splash.move(currentDesktopsCenter - splash.rect().center())

    splash.show()
    #splash.showMessage('Loading TissUUmaps...',Qt.AlignBottom | Qt.AlignCenter,Qt.white)

    qt_app.processEvents()

    port = 5000
    print ("Starting port detection")
    while (is_port_in_use(port)):
        port += 1
        if port == 6000:
            exit(0)
    print ("Ending port detection", port)

    def flaskThread():
        views.app.run(host="127.0.0.1", port=port, threaded=True, debug=False)

    threading.Thread(target=flaskThread,daemon=True).start()

    ui = MainWindow(qt_app, views.app, args)
    ui.browser.setLocation ("http://127.0.0.1:" + str(port) + "/")

    QTimer.singleShot(1000, splash.close)
    ui.browser.run()

if __name__ == '__main__':
    main ()