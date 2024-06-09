from openai import OpenAI

client = OpenAI()

def lambda_handler(event, context):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex political concepts with journalistic flair."},
            {"role": "user", "content": event }
        ]
    )
    return { 'answer': completion.choices[0].message.content }