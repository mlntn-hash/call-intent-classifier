import random
import pandas as pd

INTERESTED_PHRASES = [
    "Yeah actually I've been thinking about refinancing",
    "Sure I have a few minutes, what kind of rate could you offer",
    "I've been comparing lenders recently, what can you tell me",
    "Possibly, I'm interested in lowering my monthly payment",
    "Okay, I'm open to hearing some options if the rates are competitive",
    "That sounds interesting, can you explain the benefits",
    "I've been considering it for a while, what's available",
    "Maybe, depending on the terms and fees involved"
    "Sure, what are the details?",
    "Yeah, I'd like to hear more about it.",
    "Can you explain how the refinance works?",
    "That sounds interesting. What's the rate?",
    "I'm actually looking at my mortgage options right now.",
    "Okay, go ahead.",
    "I've been thinking about refinancing. Tell me more.",
    "What kind of savings are we talking about?",
    "I might be interested. Can you give me some information?",
    "How would this affect my monthly payment?",
    "Do you work with homeowners in my area?",
    "I'm open to hearing what you have to offer.",
    "Could this help lower my interest rate?",
    "Yeah, this might be worth discussing.",
    "Let's see if it makes sense for my situation.",
    "Can you walk me through the program?",
    "I'm kind of busy, but give me the quick version.",
    "I wasn't planning on refinancing, but what do you have?",
    "Not sure if I'm interested yet, but I'll listen.",
    "I don't know much about refinancing, so maybe explain it."
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
    "No thanks, I'm not interested.",
    "We're happy with our current mortgage.",
    "I don't want to refinance.",
    "Please remove me from your list.",
    "I'm not looking to make any changes right now.",
    "No, we're good.",
    "I already refinanced recently.",
    "This isn't something I want to discuss.",
    "Not interested, thank you.",
    "I don't think this is a fit for me.",
    "We're staying with our current lender.",
    "I'm not looking for mortgage offers.",
    "No, I don't need any information.",
    "I'm going to pass.",
    "I appreciate the call, but I'm not interested.",
    "I've already looked into refinancing and decided against it.",
    "I'm busy right now and honestly not interested anyway.",
    "Maybe another time, but probably not.",
    "You can call back if you want, but I doubt I'll be interested.",
    "Please stop calling, I'm not interested."
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
    "Can you call me back later?",
    "I'm in the middle of something right now.",
    "Could we talk tomorrow instead?",
    "I'm driving at the moment. Call me back later.",
    "Now isn't a good time.",
    "Can you try me again this afternoon?",
    "I'm heading into a meeting. Can you call back?",
    "Could you give me a call next week?",
    "I'm busy right now but I'd like to hear more.",
    "Can we schedule a better time to talk?",
    "I can't talk at the moment.",
    "Please call me after work.",
    "Can you reach out again in a few days?",
    "I'm not available right now. Try again later.",
    "Would you mind calling back this evening?",
    "Let's talk when I have a few minutes free.",
    "Not right now, maybe call back another day.",
    "I'm interested, just can't talk at the moment.",
    "Try me later and I'll decide if I want to hear more.",
    "I'm pretty busy these days, but you can call back next week."
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
    "You people keep calling me every week.",
    "I've asked to be removed from your list already.",
    "Why do I keep getting these calls?",
    "Stop calling this number.",
    "I never gave permission to be contacted.",
    "This is becoming harassment.",
    "I've told your company not to call me.",
    "If this continues, I'll file a complaint.",
    "I'm on the Do Not Call list.",
    "How did you even get my number?",
    "This is the third call I've gotten from you.",
    "Please stop contacting me.",
    "I'm tired of receiving these mortgage calls.",
    "I don't appreciate being called repeatedly.",
    "You need to take my number out of your system.",
    "I'm reporting these calls if they don't stop.",
    "Stop calling me, I'm not interested.",
    "I don't have time for this and you keep calling.",
    "Maybe I'd listen if you weren't calling every few days.",
    "Don't call again unless you have a really good reason."
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

def build_dataset(n_per_catagory=50):
    rows = []
    for label, phrases in ALL_CATEGORIES.items():
        for _ in range(n_per_catagory):
            phrase = random.choice(phrases)
            noisy_phrase = add_noise(phrase)
            rows.append({"text": noisy_phrase, "label": label})
    random.shuffle(rows)
    return rows

if __name__ == "__main__":
    rows = build_dataset(n_per_catagory=50)
    df = pd.DataFrame(rows)
    df.to_csv("dataset.csv", index=False)
    print(f"Done, saving {len(df)} str" )
    print(df.head())