from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from game_api.models import User, Game
import random

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(username=username, password=password)
        user.save()
        return JsonResponse({'message': 'User created successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found.'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            user = User.objects.get(pk=user_id)
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username:
                user.username = username
            if password:
                user.password = password
            user.save()
            return JsonResponse({'message': 'User updated successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found.'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username, password=password)
            return JsonResponse({'message': 'User logged in successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'message': 'Invalid username or password.'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def start_game(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(pk=user_id)
            game = Game(user=user, board="")
            game.board = ""
            game.save()
            return JsonResponse({'game_id': game.game_id})
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found.'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def get_board(request):
    if request.method == 'GET':
        game_id = request.GET.get('game_id')
        try:
            game = Game.objects.get(pk=game_id)
            return JsonResponse({'board': game.board})
        except Game.DoesNotExist:
            return JsonResponse({'message': 'Game not found.'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def update_board(request):
    if request.method == 'POST':
        game_id = request.POST.get('game_id')
        character = request.POST.get('character')
        try:
            game = Game.objects.get(pk=game_id)
            if len(game.board) == 6:
                return JsonResponse({'message': 'Board already has 6 characters.'})
            game.board += character
            if len(game.board) == 6:
                is_palindrome = game.board == game.board[::-1]
                game.is_palindrome = is_palindrome
            game.random_number = random.randint(1, 100)
            game.save()
            return JsonResponse({'board': game.board})
        except Game.DoesNotExist:
            return JsonResponse({'message': 'Game not found.'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)

@csrf_exempt
def list_games(request):
    if request.method == 'GET':
        games = Game.objects.all()
        game_ids = [game.game_id for game in games]
        #print(game_ids)
        return JsonResponse({'game_ids': game_ids})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=405)