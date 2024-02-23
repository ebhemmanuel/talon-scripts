from talon import Module, actions, app
# import time

mod = Module()

# Variables to track the state of the Escape key presses
# last_esc_press_time = 0
# esc_press_interval = 0.5  # 500 milliseconds between presses

@mod.action_class
class UserActions:
    def mic_on():
        """Turns the microphone on."""
        if not actions.speech.enabled():
            actions.speech.enable()
            app.notify("Microphone enabled")
            actions.key("f8")

    def mic_toggle():
        """Turns the microphone on."""
        if not actions.speech.enabled():
            actions.speech.enable()
            app.notify("commands enabled - discord muted")
            actions.key("f8")
        else:
            actions.speech.disable()
            app.notify("commands disabled - discord unmuted")
            actions.key("f8")

    def mic_off():
        """Turns the microphone off."""
        if actions.speech.enabled():
            actions.speech.disable()
            app.notify("Microphone disabled")
    
#     def toggle_mic_on_double_esc():
#         """Toggles the microphone on double press of the Escape key."""
#         global last_esc_press_time
#         current_time = time.time()
#         if (current_time - last_esc_press_time) < esc_press_interval:
#             # Double press detected, toggle the microphone
#             if actions.speech.enabled():
#                 actions.speech.disable()
#                 app.notify("Microphone disabled")
#             else:
#                 actions.speech.enable()
#                 app.notify("Microphone enabled")
#         last_esc_press_time = current_time


