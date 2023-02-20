from django.urls import include, path
from rest_framework.routers import SimpleRouter

from сommercial_network.views import CompanyViewSet, NetworkViewSet, ProductViewSet

network_router = SimpleRouter()
network_router.register("network", NetworkViewSet, basename="network")

company_router = SimpleRouter()
company_router.register("company", CompanyViewSet)

product_router = SimpleRouter()
product_router.register("product", ProductViewSet)

urlpatterns = [
    path("", include(network_router.urls)),
    path("", include(company_router.urls)),
    path("", include(product_router.urls))
]
