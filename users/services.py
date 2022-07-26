from threading import local
from django.utils.deprecation import MiddlewareMixin

_user = local()


class CurrentUserMiddleware(MiddlewareMixin):
    '''
     User middleware to get currently authenticated user
     This is equal to request.user, but can be used in model logic
    '''
    def process_request(self, request):
        _user.value = request.user


def get_current_user():
    ''' Function that retrieves request.user instance'''
    return _user.value
