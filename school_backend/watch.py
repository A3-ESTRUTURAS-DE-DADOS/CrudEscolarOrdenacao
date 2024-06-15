import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class MyHandler(FileSystemEventHandler):
    def __init__(self, script_name):
        self.script_name = script_name
        self.process = self.start_script()

    def start_script(self):
        return subprocess.Popen([sys.executable, self.script_name])

    def on_modified(self, event):
        if event.src_path.endswith(self.script_name):
            print(f'{self.script_name} foi modificado; reiniciando...')
            self.process.terminate()
            self.process = self.start_script()

if __name__ == "__main__":
    script_name = 'main.py'
    event_handler = MyHandler(script_name)
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
