"""
Password Generation Engine
"""

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
        
        # Length points
        if len(password) >= 12:
            score += 30
        elif len(password) >= 8:
            score += 20
        else:
            score += 10
        
        # Character variety points
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(not c.isalnum() for c in password)
        
        score += sum([has_upper, has_lower, has_digit, has_special]) * 15
        
        # Determine rating
        if score >= 80:
            rating = "Very Strong 🔒"
        elif score >= 60:
            rating = "Strong 💪"
        elif score >= 40:
            rating = "Moderate ⚠️"
        else:
            rating = "Weak ⚡"
        
        return score, rating
