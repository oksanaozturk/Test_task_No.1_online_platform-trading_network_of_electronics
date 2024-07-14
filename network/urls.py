from rest_framework.routers import SimpleRouter

from network.apps import NetworkConfig
from network.views import ProductViewSet, NetworkObjectViewSet

app_name = NetworkConfig.name

# Создаем экземпляр класса SimpleRouter(), он обеспечивает маршрутизацию всех путей CRUD
# [HttpGet]
router = SimpleRouter()
router.register("products", ProductViewSet)
router.register("networkobjects", NetworkObjectViewSet)

urlpatterns = [

] + router.urls
