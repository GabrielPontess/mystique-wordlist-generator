import itertools
import threading
import time
import sys

stop_loading = False

def loading_animation(message="Processing"):
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    while not stop_loading:
        sys.stdout.write(f"\r{message} {next(spinner)} ")
        sys.stdout.flush()
        time.sleep(0.1)

def start_loading(message="Processing"):
    global stop_loading
    stop_loading = False
    loading_thread = threading.Thread(target=loading_animation, args=(message,))
    loading_thread.start()
    return loading_thread

def stop_loading_animation(loading_thread):
    global stop_loading
    stop_loading = True
    loading_thread.join() 
    print("\r✅ Processing done!")
