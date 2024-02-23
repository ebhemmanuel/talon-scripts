from talon import Module, actions

mod = Module()

@mod.action_class
class UserActions:
    def mouse_left_click():
        """Performs a left mouse click."""
        actions.mouse_click(button=0)
    
    def mouse_double_click():
        """Performs a double left mouse click."""
        actions.mouse_click(button=0)
        actions.sleep("50ms")
        actions.mouse_click(button=0)
        
    def mouse_middle_click():
        """Performs a middle mouse click."""
        actions.mouse_click(button=2)
        
    def mouse_right_click():
        """Performs a right mouse click."""
        actions.mouse_click(button=1)
        
    def mouse_back():
        """Performs the mouse back action, typically bound to side buttons."""
        actions.mouse_click(button=3)
        
    def mouse_forward():
        """Performs the mouse forward action, typically bound to side buttons."""
        actions.mouse_click(button=4)

    def scroll_down():
        """Scrolls down."""
        actions.mouse_scroll(y=800)  # Scrolls down

    def scroll_up():
        """Scrolls up."""
        actions.mouse_scroll(y=-800)  # Scrolls up