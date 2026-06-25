import random

INTERESTED_PHRASES = [
    "Yeah actually I've been thinking about refinancing",
    "Sure I have a few minutes, what kind of rate could you offer",
    "I've been comparing lenders recently, what can you tell me",
    "Possibly, I'm interested in lowering my monthly payment",
    "Okay, I'm open to hearing some options if the rates are competitive",
    "That sounds interesting, can you explain the benefits",
    "I've been considering it for a while, what's available",
    "Maybe, depending on the terms and fees involved"
]

NOT_INTERESTED_PHRASES = [
    "No thanks, we're not looking to refinance right now",
    "I'm not interested, but thanks for calling",
    "We already refinanced recently",
    "I'm happy with my current mortgage",
    "Now isn't a good time for us to consider refinancing",
    "We're not looking to make any changes at the moment",
    "I don't think refinancing would benefit us right now",
    "Please remove me from your calling list"
]

CALLBACK_REQUEST_PHRASES = [
    "Can you call me back tomorrow, I'm driving right now",
    "I'm in a meeting at the moment, could you call back later",
    "This isn't a good time, can we talk sometime next week",
    "I'm a bit busy right now, please try again this afternoon",
    "Could you give me a call back in the evening when I'm home",
    "I'd like to hear more, but I'm unavailable at the moment",
    "Can you send me some information first and call back later",
    "I'm heading out right now, could you call me back another day"
]

COMPLAINT_PHRASES = [
    "You guys keep calling me every single day, this is harassment",
    "I've already asked to be removed from your call list",
    "This is the third call I've received from your company this week",
    "Please stop calling me, I'm not interested",
    "I don't appreciate these repeated unsolicited calls",
    "Why do I keep getting calls from you after saying no",
    "I've told your representatives multiple times to stop contacting me",
    "If these calls continue, I'm going to file a complaint"
]

ALL_CATEGORIES = {
    "interested": INTERESTED_PHRASES,
    "not_interested": NOT_INTERESTED_PHRASES,
    "callback_request": CALLBACK_REQUEST_PHRASES,
    "complaint": COMPLAINT_PHRASES,
}

FILLERS = ["um", "uh", "you know", "I mean", "well", "honestly", "actually"]

def add_noise(text):
    words = text.split()
    if random.random() > 0.4:
        filler = random.choice(FILLERS)
        position = random.randint(0, len(words))
        words.insert(position, filler)
    return " ".join(words)