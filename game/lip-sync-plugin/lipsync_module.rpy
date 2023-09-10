init python:
    import os
    import pygame
    
    renpy.music.register_channel("lipsync", "sfx", True)

    # Directory containing the lipsync data files
    lipsync_data_dir = "lip-sync-plugin/lip-sync-data/"

    # Function to load lipsync data for a character and audio track
    def load_lipsync_data(character, audio_track):
        global lipsync_data
        lipsync_data = []
        # Construct the relative path to the lipsync data file
        audio_file = os.path.basename(audio_track)
        file_path = os.path.join(lipsync_data_dir, character, os.path.splitext(audio_file)[0] + ".txt")
        # Load the lipsync data using renpy.load()
        lipsync_text = renpy.file(file_path).read().decode("utf-8")
        # Parse the lipsync data and store it as a list of tuples (start_time, mouth_shape)
        for line in lipsync_text.strip().split('\n'):
            start_time, mouth_shape = line.strip().split('\t')
            lipsync_data.append((float(start_time), mouth_shape))

    # Function to apply lipsync animation to a dialogue
    def lipsync(character, audio_track, dialogue):
        character_name = str(character.name)
        load_lipsync_data(character_name, audio_track)  # Load lipsync data based on the audio track
        prev_start_time = 0
        audio_path = os.path.join('voice', character_name, audio_track)
        # Play the audio track and show the dialogue
        renpy.music.play(audio_path, channel='lipsync')  # Play the audio track
        # Show the mouth shapes at the appropriate times
        for i in range(len(lipsync_data)):
            renpy.say(who=character, what=dialogue+"{fast}", interact=False)   # show the dialogue
            start_time, mouth_shape = lipsync_data[i]
            print(start_time, mouth_shape)
            renpy.show(character_name + ' mouth_' + mouth_shape)                    # Show the mouth shape image
            if i < len(lipsync_data) - 1:   
                next_start_time = lipsync_data[i + 1][0]
                duration = next_start_time - start_time + 0.01                      # Calculate duration between mouth shapes
            else:
                duration = 0.01  # Last mouth shape, no next_start_time
            renpy.pause(duration)  # Pause to synchronize with audio
            # Check for player interaction and break if interrupted
            keys = pygame.key.get_pressed()
            # mouse_clicked = any(event.type == pygame.MOUSEBUTTONDOWN for event in pygame.event.get())
            touched = any(event.type == pygame.FINGERDOWN for event in pygame.event.get())
            mouse_clicked = pygame.mouse.get_pressed()[0]
            # Check for skip or user input keys (e.g., RETURN, SPACE, CTRL) to stop playback (if mobile, also check for touch)
            if renpy.is_skipping() or touched or mouse_clicked or keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                renpy.show(character_name + ' mouth_X')
                renpy.music.stop(channel='lipsync')
                return
        renpy.say(who=character, what=dialogue+"{fast}", interact=True) 
        renpy.music.stop(channel='lipsync')