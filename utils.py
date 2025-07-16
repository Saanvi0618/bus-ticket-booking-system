import re
def is_valid_email(email_id):
    '''
        Returns true if the provided email_id is correct.
    '''
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.fullmatch(regex, email_id)