from LLM_Brain.Text2Features import FeatureExtractor

class ChatBot:

	def __init__(self):
		
		self.respond = FeatureExtractor()

	def act(self, user_message: str):

		result, error = self.respond.get_respond(user_message)

		return result, error
	
# chatbot = ChatBot()
# user_message = "یه خونه میخوام 45 متری توی منطقه 10 محله صفدری، پارکینگ هم داشته باشه."
# res, error = chatbot.act(user_message)

# print(type(res), res['system_response'])