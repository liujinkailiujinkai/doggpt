import openai

openai.api_key = "Your API key here"

def train_dog():
    name = input("What's your name? ")
    print("Hi", name, "! I'm going to teach you how to use GPT.")

    while True:
        prompt = input("What would you like to talk to GPT about? ")
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=60
        )
        print("GPT: " + response.choices[0].text)

        feedback = input("Did GPT provide a good response? [y/n] ")
        if feedback.lower() == "n":
            correction = input("What would be a better response? ")
            openai.Completion.create(
                engine="davinci",
                prompt="Please provide a better response for: \n\n" + prompt + "\n\nNew response:",
                examples=[["Original response: " + response.choices[0].text, "New response: " + correction]],
                max_tokens=60
            )
            print("Thanks, I'll make sure to remember that.")
        else:
            print("Glad to hear it!")

train_dog()
