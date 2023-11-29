from rest_framework.views import exception_handler
from django.http import Http404


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, Http404):   
        error_message = str(exc)        
        if "Branch" in error_message:
            custom_response_data = {'detail': 'This Branch does not exist'}
        elif "Company" in error_message:
            custom_response_data = {'detail': 'This Company does not exist'}        
        else:
            custom_response_data = {'detail': f'{exc}'}
        response.data = custom_response_data
    return response