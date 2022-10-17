import re
import random
from urllib import response

def get_response(user_imput):
    split_message= re.split(r'\s|[,:;.?!-_]\s*',user_imput.lower())
    response = check_all_messages(split_message)
    return response 

    def message_probability(user_message, recognized_words, single_response = False, required_word=[]):
     message_certainty = 0 
    has_required_words = True 

    for word in user_message:
      if word in recognized_words:
        message_certainty +=1

        percentage = float (message_certainty) / float (len(recognized_words))

        for word in required_word:
            if word not in user_message:
                has_required_words= False
                break 
            if has_required_words or single_response:
                return int(percentage * 100)
            else:
                return 0

                def check_all_messages(message):
                    highest_prob = {}

                    def response(bot_response, list_of_words, single_response = False, require_words = []):
                        nonlocal highest_prob
                        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

                        response('Hola', ['hola','buenas', 'saludos', 'que tal'],single_response = True)
                        response('Odio a la vida y tengo deprecion y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words =['como'])
                        response('No estudien programacion, mejor estudien gastronomia', ['estudiar', 'carrera', 'estudios'], single_response = True)
                        response('El mejor color es el naranja', ['color', 'color favorito', 'el mejor color', 'prueba'], single_response = Ture)

                        best_match = max(highest_prob, key=highest_prob.get)
                        print(highest_prob)

                        return unknown() if highest_prob[best_match] < 1 else best_match

                def unknown():
                    response = ['aun no me actualizan para comprender eso, podriar reformular tu pregunta', 'No estoy seguro de lo que me quieres decir', 'te me estas insinuando de una forma sexual?'][random.randrange(3)]

while True:
    print("Bot: " + get_response(input('you: ')))