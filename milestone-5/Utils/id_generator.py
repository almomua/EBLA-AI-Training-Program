"""Utility functions for generating unique identifiers.

This module provides helper functions for ID generation.
"""

import uuid


def generate_uuid() -> str:
    """Generate a unique UUID string.
    
    Returns:
        A string representation of a UUID4.
    """
    return str(uuid.uuid4())
