
class ValidatorMixin:
    """This class implementsvalidation for automated testing"""
    __allowed_methods = ("xpath", "name" , "link_text", "partial_link_text", "id", "tag_name", "class_name", "css_selector")
    
    def validate_method(self, method):
        """Validates whether provided method is valid or not """
        if method in ValidatorMixin.__allowed_methods:
            return True 
        else:
            raise Exception("This method is not allowed")