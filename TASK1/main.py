"""
Main Program
CodSoft Python Internship - Task 1
"""

from engine import PasswordGenerator
from user_interface import UI


def main():
    """Main application"""
    
    ui = UI()
    generator = PasswordGenerator()
    
    ui.show_welcome()
    
    while True:
        try:
            # Get user input
            length = ui.get_length()
            upper, lower, digits, special = ui.get_options()
            
            # Setup generator
            if not generator.setup(upper, lower, digits, special):
                ui.show_error("Select at least one character type!")
                continue
            
            # Generate password
            password = generator.generate(length)
            
            if not password:
                ui.show_error("Could not generate password!")
                continue
            
            # Check strength
            strength = generator.check_strength(password)
            
            # Display result
            ui.show_result(password, length, generator.selected, strength)
            
            # Ask to continue
            if not ui.ask_continue():
                break
            
            print("\n" + "─" * 60 + "\n")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Cancelled by user")
            break
        
        except Exception as e:
            ui.show_error(f"Error: {e}")
            break
    
    ui.show_goodbye()


if __name__ == "__main__":
    main()
