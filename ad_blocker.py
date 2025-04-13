import keyboard
import time
import sys

class YouTubeAdBlocker:
    def __init__(self):
        self.is_running = False

    def block_ad(self):
        """Attempt to block an ad using keyboard navigation"""
        try:
            # Press space to ensure video is playing
            keyboard.press_and_release('space')
            time.sleep(0.2)

            # Press Tab twice to get to the "i" info button
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('enter')  # Select the info button
            time.sleep(1.0)  # Wait for info window to appear

            # Press Tab three times to get to the "Block" button
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('enter')  # Select the block button
            time.sleep(1.0)  # Wait for block window to appear

            # Press Tab once to get to "Continue" button
            keyboard.press_and_release('tab')
            time.sleep(0.2)
            keyboard.press_and_release('enter')  # Select continue
            time.sleep(0.5)

            # Press Shift+Tab to go back to close button
            keyboard.press('shift')
            keyboard.press_and_release('tab')
            keyboard.release('shift')
            time.sleep(0.2)
            keyboard.press_and_release('enter')  # Close Ad Center window
            time.sleep(0.5)

        except Exception as e:
            print(f"Error attempting to block ad: {e}")

    def run(self):
        """Main loop to monitor for hotkey presses"""
        try:
            self.is_running = True
            print("YouTube Ad Blocker started!")
            print("Press '`' when an ad appears to block it")
            print("Press 'Esc' to exit")
            
            keyboard.on_press_key('`', lambda _: self.block_ad())
            keyboard.wait('esc')
            
        finally:
            self.is_running = False
            print("YouTube Ad Blocker stopped!")

if __name__ == "__main__":
    blocker = YouTubeAdBlocker()
    blocker.run() 