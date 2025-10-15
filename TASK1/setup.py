"""
Auto Setup for Task 1 - Simple Version
"""

import os
from pathlib import Path

FILES = {
    "config.py": '''"""Configuration Settings"""

UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
SPECIAL = '!@#$%^&*()_+-=[]{}|;:,.<>?'

MIN_LENGTH = 6
MAX_LENGTH = 128
DEFAULT_LENGTH = 12
''',

    "password_engine.py": '''"""Password Generation Engine"""

import secrets
import config


class PasswordGenerator:
    """Generates secure passwords"""
    
    def __init__(self):
        self.char_pool = ""
        self.selected = []
    
    def setup(self, upper, lower, digits, special):
        """Build character pool"""
        self.char_pool = ""
        self.selected = []
        
        if upper:
            self.char_pool += config.UPPERCASE
            self.selected.append('Uppercase')
        if lower:
            self.char_pool += config.LOWERCASE
            self.selected.append('Lowercase')
        if digits:
            self.char_pool += config.DIGITS
            self.selected.append('Digits')
        if special:
            self.char_pool += config.SPECIAL
            self.selected.append('Special')
        
        return len(self.char_pool) > 0
    
    def generate(self, length):
        """Create password"""
        if not self.char_pool:
            return None
        
        if length < config.MIN_LENGTH or length > config.MAX_LENGTH:
            return None
        
        return ''.join(secrets.choice(self.char_pool) for _ in range(length))
    
    def check_strength(self, password):
        """Calculate password strength"""
        score = 0
        
        if len(password) >= 12:
            score += 30
        elif len(password) >= 8:
            score += 20
        else:
            score += 10
        
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        score += sum([has_upper, has_lower, has_digit, has_special]) * 15
        
        if score >= 80:
            rating = "Very Strong 🔒"
        elif score >= 60:
            rating = "Strong 💪"
        elif score >= 40:
            rating = "Moderate ⚠️"
        else:
            rating = "Weak ⚡"
        
        return score, rating
''',

    "user_interface.py": '''"""User Interface Module"""

import os
import config


class UI:
    """Handles user input and display"""
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_welcome(self):
        self.clear()
        print("\\n" + "=" * 60)
        print("    PASSWORD GENERATOR - CodSoft Internship")
        print("=" * 60)
        print("    Author: [Your Name]")
        print("    Date: October 2025")
        print("=" * 60 + "\\n")
    
    def get_length(self):
        while True:
            try:
                print(f"Password Length: {config.MIN_LENGTH}-{config.MAX_LENGTH}")
                user_input = input(f"Enter length [{config.DEFAULT_LENGTH}]: ").strip()
                
                if not user_input:
                    return config.DEFAULT_LENGTH
                
                length = int(user_input)
                
                if config.MIN_LENGTH <= length <= config.MAX_LENGTH:
                    return length
                else:
                    print(f"❌ Must be between {config.MIN_LENGTH} and {config.MAX_LENGTH}\\n")
            
            except ValueError:
                print("❌ Please enter a number\\n")
    
    def get_options(self):
        print("\\n" + "─" * 60)
        print("Character Types:")
        print("─" * 60)
        
        upper = self._ask("Include UPPERCASE (A-Z)?", True)
        lower = self._ask("Include lowercase (a-z)?", True)
        digits = self._ask("Include numbers (0-9)?", True)
        special = self._ask("Include special (!@#$%)?", False)
        
        return upper, lower, digits, special
    
    def _ask(self, question, default):
        hint = "Y/n" if default else "y/N"
        answer = input(f"  {question} [{hint}]: ").strip().lower()
        
        if not answer:
            return default
        
        return answer in ['y', 'yes']
    
    def show_result(self, password, length, types, strength):
        score, rating = strength
        
        print("\\n" + "=" * 60)
        print("  PASSWORD GENERATED!")
        print("=" * 60)
        
        print(f"\\n🔐 Your Password:")
        print(f"   ┌{'─' * (len(password) + 2)}┐")
        print(f"   │ {password} │")
        print(f"   └{'─' * (len(password) + 2)}┘")
        
        print(f"\\n📊 Details:")
        print(f"   Length: {length} characters")
        print(f"   Types: {', '.join(types)}")
        print(f"   Strength: {score}/100 - {rating}")
        
        print("\\n" + "=" * 60 + "\\n")
    
    def ask_continue(self):
        answer = input("Generate another password? (y/N): ").strip().lower()
        return answer in ['y', 'yes']
    
    def show_goodbye(self):
        print("\\n" + "─" * 60)
        print("  Thank you for using Password Generator!")
        print("─" * 60 + "\\n")
    
    def show_error(self, message):
        print(f"\\n❌ {message}\\n")
''',

    "main.py": '''"""Main Program - CodSoft Python Internship Task 1"""

from password_engine import PasswordGenerator
from user_interface import UI


def main():
    """Main application"""
    
    ui = UI()
    generator = PasswordGenerator()
    
    ui.show_welcome()
    
    while True:
        try:
            length = ui.get_length()
            upper, lower, digits, special = ui.get_options()
            
            if not generator.setup(upper, lower, digits, special):
                ui.show_error("Select at least one character type!")
                continue
            
            password = generator.generate(length)
            
            if not password:
                ui.show_error("Could not generate password!")
                continue
            
            strength = generator.check_strength(password)
            
            ui.show_result(password, length, generator.selected, strength)
            
            if not ui.ask_continue():
                break
            
            print("\\n" + "─" * 60 + "\\n")
        
        except KeyboardInterrupt:
            print("\\n\\n⚠️  Cancelled by user")
            break
        
        except Exception as e:
            ui.show_error(f"Error: {e}")
            break
    
    ui.show_goodbye()


if __name__ == "__main__":
    main()
'''
}

def create_project():
    """Create complete project"""
    
    folder = Path("Task1-PasswordGenerator")
    folder.mkdir(exist_ok=True)
    
    print("\n" + "=" * 60)
    print("  CREATING TASK 1 PROJECT")
    print("=" * 60 + "\n")
    
    for filename, content in FILES.items():
        filepath = folder / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Created: {filename}")
    
    print("\n" + "=" * 60)
    print("  PROJECT READY!")
    print("=" * 60 + "\n")
    
    print("📁 Files created:")
    print("  - config.py")
    print("  - password_engine.py")
    print("  - user_interface.py")
    print("  - main.py")
    
    print("\n🎯 TO RUN:")
    print(f"  cd {folder}")
    print("  python main.py")
    print()

if __name__ == "__main__":
    create_project()
