define lisa = Character("lisa", color="#ffffff")

layeredimage lisa:
    zoom 3.0
    group mouth:
        attribute mouth_A:
            "lisa-A.png"
        attribute mouth_B:
            "lisa-B.png"
        attribute mouth_C:
            "lisa-C.png"
        attribute mouth_D:
            "lisa-D.png"
        attribute mouth_E:
            "lisa-E.png"
        attribute mouth_F:
            "lisa-F.png"
        attribute mouth_G:
            "lisa-G.png"
        attribute mouth_H:
            "lisa-H.png"
        attribute mouth_X default:
            "lisa-X.png"
        
# Note: Lip-sync requires audio files in .wav format.
# Note: Prepare lip-sync data using generate_lipsync_data.py.

label start:
    # show lisa at left
    show lisa at center
    "Hello, I'm lisa."
    "Watch me lip-sync."
    # Play the lip-sync animation for the given audio file.
    # parameters are : character, audio file, text to display
    $ lipsync(lisa, "what-can-i-do-for-you-npc-british-male-99751.wav", "What can I do for you?")
    $ lipsync(lisa, "ah-good-morning-sir-would-you-like-a-cup-of-tea.ogg", \
        "Ah, good morning sir. Would you like a cup of tea?")
    "Thank you for watching!"