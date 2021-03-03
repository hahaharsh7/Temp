from functools import wraps
from app.constants import csv_writer

def bool_logger(method):
    def inner_function(cls,*args, **kwargs):
        try:
            result = method(cls,*args, **kwargs)
            error_type = "NA"
            path = cls.__class__.get_name()
            if "error_type" in result:
                
                error_type = result["error_type"]
            if "extra_path" in result:
                path = f'{path}>>{result["extra_path"]}'
                
            csv_writer.append([path ,error_type, result["remarks"] ,result["value"]])
        except Exception as e:
            print(f'Exception occured in bool logger message:- {e}')
    return inner_function