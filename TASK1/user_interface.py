"""
User Interface Module
"""

import os
import config


class UI:
    """Handles user input and display"""
    
    def clear(self):
        """Clear screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_welcome(self):
        """Display welcome message"""
        self.clear()
        print("\n" + "=" * 60)
        print("    PASSWORD GENERATOR - CodSoft Internship")
        print("=" * 60)
        print("    Author: [Your Name]")
        print("    Date: October 2025")
        print("=" * 60 + "\n")
    
    def get_length(self):
        """Get password length from user"""
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
                    print(f"❌ Must be between {config.MIN_LENGTH} and {config.MAX_LENGTH}\n")
            
            except ValueError:
                print("❌ Please enter a number\n")
    
    def get_options(self):
        """Get character type preferences"""
        print("\n" + "─" * 60)
        print("Character Types:")
        print("─" * 60)
        
        upper = self._ask("Include UPPERCASE (A-Z)?", True)
        lower = self._ask("Include lowercase (a-z)?", True)
        digits = self._ask("Include numbers (0-9)?", True)
        special = self._ask("Include special (!@#$%)?", False)
        
        return upper, lower, digits, special
    
    def _ask(self, question, default):
        """Ask yes/no question"""
        hint = "Y/n" if default else "y/N"
        answer = input(f"  {question} [{hint}]: ").strip().lower()
        
        if not answer:
            return default
        
        return answer in ['y', 'yes']
    
    def show_result(self, password, length, types, strength):
        """Display generated password"""
        score, rating = strength
        
        print("\n" + "=" * 60)
        print("  PASSWORD GENERATED!")
        print("=" * 60)
        
        print(f"\n🔐 Your Password:")
        print(f"   ┌{'─' * (len(password) + 2)}┐")
        print(f"   │ {password} │")
        print(f"   └{'─' * (len(password) + 2)}┘")
        
        print(f"\n📊 Details:")
        print(f"   Length: {length} characters")
        print(f"   Types: {', '.join(types)}")
        print(f"   Strength: {score}/100 - {rating}")
        
        print("\n" + "=" * 60 + "\n")
    
    def ask_continue(self):
        """Ask if user wants another password"""
        answer = input("Generate another password? (y/N): ").strip().lower()
        return answer in ['y', 'yes']
    
    def show_goodbye(self):
        """Display exit message"""
        print("\n" + "─" * 60)
        print("  Thank you for using Password Generator!")
        print("─" * 60 + "\n")
    
    def show_error(self, message):
        """Display error"""
        print(f"\n❌ {message}\n")
