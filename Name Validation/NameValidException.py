/*
==========================================================================
            Name Validation Exception Module – Key Points
==========================================================================
              
    1. Defines custom exception classes for name validation
    2. Handles empty name input using ZeroNameLengthError
    3. Prevents only whitespace input using SpaceError
    4. Detects invalid characters (numbers/symbols) using InvalidNameError
    5. Improves data validation and input reliability
    6. Enhances error handling with meaningful exceptions
    7. Promotes clean and modular code design
    8. Used across multiple modules for consistent validation logic
      
==========================================================================
*/

class ZeroNameLengthError(Exception):pass
class SpaceError(Exception):pass
class InvalidNameError(Exception):pass
