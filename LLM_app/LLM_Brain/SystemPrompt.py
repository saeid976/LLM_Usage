OPENAI_API_KEY = ""
GROQ_API_KEY = "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"
system_message = f"""
                    You are a asistant. provide yout response in dict format.
                    you must extract the features in the user input based on following tags:
                      1. `متراژ`: متراژ و مساحت ساختمان مثال :  100 متری.
                      2. `منطقه`: منطقه شهرداری ملک یا خانه مثال : منطقه 4.
                      3. `محله`: محله ملک بر روی نقشه مثال : محله وزرا.
                      4. `تعداد اتاق`: تعداد اتاق های یک خانه است مثلا 1 اتاق یا یک خوابه.
                      5. `پارکینگ`: دارد یا ندارد. مثال : پارکینگ دار به معنی داشتن پارکینگ می باشد.
                      6. `آساسنسور`: دارد یا ندارد. مثال : اسانسور داشته باشد به معنی بودن اسانسور است.
"""