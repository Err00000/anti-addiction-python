import psutil
import time
from playsound import playsound
game_process_name = "LeagueClient.exe"
start_time = None

def verify_processes():
        running_processes = psutil.process_iter(attrs=['name'])
        game_running = any(process.info['name'] == game_process_name for process in running_processes)
        return game_running

def game_check():
    str: game_running
    global start_time
    game_running = verify_processes()
    print("Checking!!!!!!!!")
    if game_running:
        print(f"{game_process_name} is running")
        if start_time is None:
             start_time = time.time()

        elapsed_time = time.time() - start_time
        if elapsed_time > 5:
            while True:            
                sound_file = r'E:\restrictpc\sound.mp3'
                playsound(sound_file)
                print(f"Stop playing {game_process_name}, fucker. Back to work!!")
                time.sleep(5)
    else:
        if start_time is not None:
            elapsed_time = time.time() - start_time
            print(f"{game_process_name} was active for {elapsed_time:.2f} seconds. Game is not active now.")
            start_time = None
        else: print(f"{game_process_name} is not running. Game is not active.")

def main():
    while True:
        game_check()
        time.sleep(2)

if __name__ == "__main__":
    main()