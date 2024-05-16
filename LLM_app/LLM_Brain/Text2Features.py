# from openai import OpenAI
from groq import Groq
from LLM_Brain.SystemPrompt import *

class FeatureExtractor:
	def __init__(self):
		# self.model_name = 'gpt-3.5-turbo'
		self.model_name = 'llama3-70b-8192'
		self.temperature = 0.2
		self.max_tokens = 4096
 

	def get_completion(self, messages):

		response, error = "", None
		
		try:
			# client = OpenAI(api_key = OPENAI_API_KEY)
			client = Groq(api_key=GROQ_API_KEY)
			r = client.chat.completions.create(
			model= self.model_name,
			messages=[{"role": m["role"], "content": m["content"]} for m in messages],
			)
			response = r.choices[0].message.content
			
		except Exception as err:
			error = "Unable to generate response"
			print(f"error: {err}")
		
		return response, error

	def get_respond(self, user_message):

		messages = [
				{'role':'system',
				'content': system_message},
				{'role':'user',
				'content': f"{user_message}"}
		]
		response, error = self.get_completion(messages)
		response_data = {
							"system_response": response
						}

		return response, error
