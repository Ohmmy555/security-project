if(pyautogui.locateOnScreen('./img/unlock2.png')):
            print('Login MetaMask')
            time.sleep(2)
            pyautogui.click(1684,137)
            if(pyautogui.locateOnScreen('./img/unlock3.png')):
                print('My Accounts')
                time.sleep(1)
                pyautogui.click(1397,624)
                if(pyautogui.locateOnScreen('./img/unlock4.png')):
                    print('Settings')
                    time.sleep(1)
                    pyautogui.click(1409,507)
                    if(pyautogui.locateOnScreen('./img/unlock5.png')):
                        print('Security')
                        time.sleep(1)
                        pyautogui.click(1465,400)