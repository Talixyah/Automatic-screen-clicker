import time
import pyautogui

def main():
    print("Program Started")

    while True:
        try:
            locateOnScreen = pyautogui.locateOnScreen('C:\\deneme.png')
            if locateOnScreen is not None:
                x, y = pyautogui.center(locateOnScreen)
                print("Clicked on the specified image!")
                pyautogui.click(x, y)
                pyautogui.moveTo(x, y + 250)

                choice = input("Image found! Press '1' to continue or '2' to exit: ")
                if choice == '2':
                    print("Exiting the program.")
                    return
            else:
                print("Image not found. Continuing...")

        except pyautogui.ImageNotFoundException:
            print("Image not found. Continuing...")

        time.sleep(0.2)

if __name__ == "__main__":
    main()

## Written and developed by Hilmi Uysaloğlu.
