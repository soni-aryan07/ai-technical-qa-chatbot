import time
from analytics import save_interaction
from config import openai, anthropic, google
 
system_prompt = """
You are QueryForge, a technical Q&A assistant.

If the user asks for code:
- Provide complete working code.
- Use Markdown code blocks.
- Explain how the code works.
"""

def ask_ai(provider, model, history):
    history = [{'role': h['role'], 'content': h['content']} for h in history]
    
    start_time = time.time()
    messages = [{'role': 'system', 'content': system_prompt}] + history

    answer = ""
    try:
        
        if provider == 'OpenAI':
                stream = openai.chat.completions.create(
                model= model,
                messages=messages,
                stream=True
            )
        elif provider == 'Google':
            stream = google.chat.completions.create(
                model= model,
                messages=messages,
                stream=True
            )
        elif provider == 'Claude':
            stream = anthropic.chat.completions.create(
                model= model,
                messages=messages,
                stream=True
            )
        else:
            yield history + [{'role': 'assistant', 'content': 'Provider not supported.'}]
            return

        
        for chunk in stream:
            answer += chunk.choices[0].delta.content or ""

            # Yield the full history for messages type chatbot
            yield history + [{'role': 'assistant', 'content': answer}]

        end_time = time.time()
        response_time = end_time - start_time

        save_interaction(
            provider= provider,
            model= model,
            question= history[-1]['content'],
            answer= answer,
            response_time = response_time,
            success= True,
            error=False
        )

        print(f"Response time: {response_time:.2f} seconds")


    except Exception as e:
        end_time = time.time()
        response_time = end_time - start_time

        print(f"Error after {response_time:.2f} seconds")

        save_interaction(
            provider= provider,
            model= model,
            question= history[-1]['content'],
            answer= answer,
            response_time = response_time,
            success= False,
            error=True
        )

        yield history + [{'role': 'assistant', 'content':f"Error: {e}"}]