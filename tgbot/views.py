from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Chat

@csrf_exempt
def index(request, pk):
    if request.method == 'POST':
        print(request.POST.get)
        # Chatni tozalash
        Chat.objects.filter(user_id=pk).delete()
        return JsonResponse({'status': 'success', 'message': 'Chat tozalandi!'})

    else:
        questions = Chat.objects.filter(user_id=pk).order_by('created_at').all()
        if questions:
            messages = []
            for q in questions:
                messages.append({
                    "sender": "Me",
                    "message": q.message,
                    "timestamp": q.created_at.strftime("%I:%M %p")
                })
                # Do'stdan kelgan javob
                messages.append({
                    "sender": "From OpenAI",
                    "message": q.answer,
                    "timestamp": q.created_at.strftime("%I:%M %p")
                })
        else:
            messages = [{'sender': 'System', 'message': 'No messages available.', 'timestamp': ''}]

        return render(request, 'index.html', {'messages': messages})
