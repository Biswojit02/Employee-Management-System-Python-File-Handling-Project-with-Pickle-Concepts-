/*
==============================================================================
                Name Validation Module – Key Highlights
==============================================================================

        1. Validates employee name and company name inputs
        2. Prevents empty input using ZeroNameLengthError
        3. Blocks names containing only spaces (SpaceError)
        4. Splits input into words for detailed validation
        5. Ensures each word contains only alphabets (isalpha())
        6. Raises InvalidNameError for numbers/special characters
        7. Uses strip() to remove extra spaces before validation
        8. Returns valid name if all checks pass successfully
  
==============================================================================
*/


from NameValidException import ZeroNameLengthError,SpaceError,InvalidNameError
def name_validate(name):
    if len(name)==0:
        raise ZeroNameLengthError
    elif name.isspace():
        raise SpaceError
    else:
        res=True
        words=name.strip().split()
        for word in words:
            if not word.isalpha():
                res=False
                break
        if res:
            return name
        else:
            raise InvalidNameError
)
