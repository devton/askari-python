from .proxies import ProxyUser


class ProxyUserMiddleware():
    def process_request(self, request):
        if hasattr(request, 'user') and request.user.is_authenticated():
            request.user.__class__ = ProxyUser