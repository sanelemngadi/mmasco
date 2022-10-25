from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings

from django.core.mail import send_mail, EmailMessage

def emails_view(request):
    return Response({"error: ": "faild"}, status=status.HTTP_200_OK)    

    # {
    #     "name":"Sanele Mngadi",
    #     "email_owner": "sanelemngadi17@gmail.com",
    #     "email_user":"218014972@stu.ukzn.ac.za",
    #     "subject":"Trauma caunselling",
    #     "message":"Hi this is sanele mngadi I send this email because I want to book for an appointment",
    #     "greetings": "Good morning Sanele"
    # }


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
                "private.socialworker@xolanibukhosini.co.za", # email from
                ["sanelemngadi17@gmail.com"], # email to []
                # reply_to=["sanelemngad17@gmail.com"]
            )
            email_msg.send()
            return Response(data,status=status.HTTP_200_OK)
        except:
            return Response({"error": "invalid form data"},status=status.HTTP_400_BAD_REQUEST)