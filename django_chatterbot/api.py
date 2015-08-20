from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from chatterbot import ChatBot


chatterbot = ChatBot('Example ChatterBot')

chatterbot.train([
    "Hi",
    "How are you?"
])


class ChatterBotView(views.APIView):
    permission_classes = []

    def get(self, request, *args, **kwargs):
        data = {
            'error': 'You should make a POST request to this endpoint.'
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        input_statement = request.data.get('input', '')

        response_data = chatterbot.get_response(input_statement)

        return Response(response_data, status=status.HTTP_200_OK)

