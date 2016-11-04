from rest_framework import viewsets, status
from .models import App, Entity, Session, Checkin, Checkout
from .serializers import AppSerializer, EntitySerializer, SessionSerializer, CheckinSerializer, CheckoutSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer

class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class CheckinViewSet(viewsets.ModelViewSet):
    queryset = Checkin.objects.all().order_by('-created_at')
    serializer_class = CheckinSerializer

class CheckoutViewSet(viewsets.ModelViewSet):
    queryset = Checkout.objects.all().order_by('-created_at')
    serializer_class = CheckoutSerializer

##################################################
##################################################
##################################################

# from rest_framework import renderers
# from rest_framework import generics
# from rest_framework.response import Response
#
# class EntityCheckout(generics.GenericAPIView):
#     queryset = Entity.objects.all()
#     # serializer_class = EntitySerializer
#     # renderer_classes = (renderers.JSONRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         checkout = self.get_object()
#
#         sessions = checkout.session_set.filter(active=True)
#
#         if(sessions.count()>0):
#             session = sessions.first()
#
#             try:
#                 return Response(CheckoutSerializer(session.checkout, many=False).data)
#             except Exception as e:
#                 return Response({"msg":str(e)},status=status.HTTP_404_NOT_FOUND)
#                 pass
#         else:
#             return Response({"msg":"active session doesn't exists"},status=status.HTTP_404_NOT_FOUND)
#
#     # # TODO: HACER QUE FUNCIONE ESTA WEA
#     # def post(self, request, *args, **kwargs):
#     #     checkout = self.get_object()
#     #
#     #     sessions = checkout.session_set.filter(active=True)
#     #
#     #     if(sessions.count()>0):
#     #         session = sessions.first()
#     #
#     #         try:
#     #             return Response(CheckoutSerializer(session.checkout, many=False).data)
#     #         except Exception as e:
#     #             return Response({"msg":str(e)},status=status.HTTP_404_NOT_FOUND)
#     #             pass
#     #     else:
#     #         return Response({"msg":"active session doesn't exists"},status=status.HTTP_404_NOT_FOUND)
