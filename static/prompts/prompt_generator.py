import random
import json

breakpoint_options = [
    [2, 3, 4],
    [1, 2, 3],
    [3, 4, 5],
    [2, 4, 6],
    [1, 3, 5],
    [1, 2, 4],
    [2, 3, 5],
    [3, 5, 6],
    [1, 3, 6],
    [2, 4, 5]
]
nouns = [
    "the capital of Spain", "the square root of 49", "the tallest mountain", "the currency of Japan",
    "the boiling point of water", "the fastest land animal", "2 + 2", "the meaning of AI",
    "the color of the sky", "the inventor of the lightbulb", "the largest planet",
    "the first president of the USA", "a black hole", "gravity", "the capital of Italy",
    "the most spoken language", "photosynthesis", "the speed of light", "quantum physics",
    "a haiku", "a limerick", "Shakespeare", "a palindrome", "the Eiffel Tower", "the Pyramids",
    "a solar eclipse", "a lunar eclipse", "COVID-19", "the human brain", "the liver's function",
    "DNA", "RNA", "a gene", "photosynthesis", "chlorophyll", "an atom", "a molecule",
    "Newton's laws", "Einstein's theory", "pi", "Euler's number", "the capital of Canada",
    "the Amazon rainforest", "Mount Everest", "the Sahara Desert", "the Pacific Ocean",
    "the Great Wall of China", "the Statue of Liberty", "the Leaning Tower of Pisa",
    "a volcano", "an earthquake", "a tsunami", "climate change", "global warming", "a glacier",
    "a comet", "a meteor", "a constellation", "the Milky Way", "the Big Bang", "the Hubble Telescope",
    "light years", "a planet", "a star", "a galaxy", "Jupiter", "Saturn", "Neptune", "Pluto",
    "the Moon", "the Sun", "a calendar", "a leap year", "a decade", "a century", "a millennium",
    "a light bulb", "a smartphone", "a computer", "the Internet", "WiFi", "Bluetooth", "email",
    "a web browser", "a URL", "HTTP", "HTTPS", "IP address", "a server", "a database",
    "artificial intelligence", "machine learning", "deep learning", "neural networks", "GPT",
    "OpenAI", "CodeSignal", "Python", "JavaScript", "Java", "C++", "HTML", "CSS", "SQL", "JSON", 
    "the capital of France", "the tallest building in the world", "the population of India", "the distance to the Moon"
]

# Generate questions from nouns
user_questions = [f"What is {noun}?" for noun in nouns]

# Generate the 365 entries
entries = []
for i in range(365):
    entry = {
        "llm": "gpt-4o",
        "system_prompt": "You are a helpful assistant. Your answers must only contain 10 words.",
        "user_question": random.choice(user_questions),
        "breakpoints": random.choice(breakpoint_options)
    }
    entries.append(entry)

# Verify we have the right number of entries
print(f"Generated {len(entries)} entries")
print("Sample entry:", entries[0])

# Save the entries list to a json file 
with open("data.json","w") as f:
    json.dump(entries,f,indent=2)
    
print("Data saved to data.json")