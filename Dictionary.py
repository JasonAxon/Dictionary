#Array section
dictionary={
    "Also-ran": "One that is of little importance especially competitively.",
    "Arson": "The willful or malicious burning of property (such as a building) especially with criminal or fraudulent intent.",
    "Bereft": "Deprived or robbed of the possession or use of something.",
    "Cinephile": "A devotee of motion pictures.",
    "Derange": "To disturb the operation or functions of.",
    "Exile": "The state or a period of forced absence from one's country or home.",
    "Forsake": "To renounce or turn away from entirely.",
    "Gauche": "Lacking social experience or grace.",
    "Hollow": "Having an unfilled or hollowed-out space within.",
    "Important": "Marked by or indicative of significant worth or consequence.",
    "Juxtaposition": "The act or an instance of placing two or more things side by side often to compare or contrast or to create an interesting effect.",
    "Kleptocracy": "Government by those who seek chiefly status and personal gain at the expense of the governed.",
    "Limerence": "Involuntary state of intense romantic desire for another person, characterized by intrusive thoughts, obsessive feelings, and a longing for emotional reciprocation.",
    "Malady": "An unwholesome or disordered condition.",
    "Malignant": "Tending to produce death or deterioration.",
    "Naive": "Deficient in worldly wisdom or informed judgment.",
    "Oppress": "To crush or burden by abuse of power or authority.",
    "Paradox": "One (such as a person, situation, or action) having seemingly contradictory qualities or phases.",
    "Pique": "To excite or arouse especially by a provocation, challenge, or rebuff.",
    "Quaff": "To drink (a usually alcoholic beverage) heartily or copiously.",
    "Rendezvous": "A place appointed for assembling or meeting.",
    "Soliloquy": "The act of talking to oneself.",
    "Somber": "So shaded as to be dark and gloomy.",
    "Tapestry": "A heavy handwoven reversible textile used for hangings, curtains, and upholstery and characterized by complicated pictorial designs.",
    "Undermine": "To subvert or weaken insidiously or secretly.",
    "Unrequited": "Not reciprocated or returned in kind.",
    "Verdict": "The finding or decision of a jury on the matter submitted to it in trial.",
    "War": "A state of usually open and declared armed hostile conflict between states or nations.",
    "Yearn": "To long persistently, wistfully, or sadly.",
    "Zone": "One of the sections of an area or territory created for a particular purpose."
    }
#interface section
word=input("Type a word you want to be defined. ->")
print(dictionary[word])
#loop section
response=input("Is there anything else you want to be defined? Yes or No?")
while response == "Yes":
    word=input("Type a word you want to be defined. ->")
    print(dictionary[word])
    response=input("Is there anything else you want to be defined? Yes or No?")
else:
    print("Thank you for using our dictionary.")