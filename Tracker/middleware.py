# middleware.py
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from .models import BlockedWebsite

class WebsiteBlockerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.get_host()
        path = request.get_full_path()
        full_url = f"http://{host}{path}"

        blocked_websites = [bw.url for bw in BlockedWebsite.objects.all()]
        if any(full_url.startswith(url) for url in blocked_websites):
            return HttpResponseForbidden("Access to this website is blocked.")
        return None
