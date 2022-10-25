from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings

from django.core.mail import EmailMessage

class EmailCreateView(APIView):
    def post(self, request):
        data = {
            "name": request.data["name"],
            "email_owner": request.data["email_owner"],
            "email_user": request.data["email_user"],
            "subject": request.data["subject"],
            "message": request.data["message"],
            "greetings": request.data["greetings"]
        }
        msg = f"""
            {data['greetings']}\n\n
            You have a new message from {data['name']}\n
            name: '{data['name']}'
            email: '{data['email_user']}'
            message: \n
            '{data['message']}'

            Your developers
            MMASCo.
        """

        try:
            subject = f"{data['name'].upper()} - {data['subject'].upper()}"
            email_msg = EmailMessage(
                subject, # subject
                msg, # message
                 settings.EMAIL_HOST_USER, # email from
                [data["email_owner"]], # email to []
            )
            email_msg.send()
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({"error": "invalid form data"},status=status.HTTP_400_BAD_REQUEST)