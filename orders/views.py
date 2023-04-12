from rest_framework.generics import CreateAPIView


class OrderCreateAPIView(CreateAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
