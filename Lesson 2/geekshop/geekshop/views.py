from django.shortcuts import render

def main(request):
    context = {
        'description': 'Офигенские СТУЛЬЯ',
        'subject': 'Популярно в лучших домах Филадельфии'
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')