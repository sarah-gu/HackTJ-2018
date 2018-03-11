# -*- coding: utf-8 -*-
""" Trivia quiz.. """
from __future__ import print_function
import math
import string
import random
 
GAME_STATE_TRIVIA = "TRIVIA"
GAME_STATE_START = "START"
GAME_STATE_HELP = "HELP"
 
GAME_QUESTIONS_KEY = "gameQuestions"
ANSWERTEXT_KEY = "correctAnswerText"
SCORE = "score"
CORRECTANSWERINDEX = "correctAnswerIndex"
SPEECHOUTPUT_KEY = "speechOutput"
REPROMPT_KEY = "repromptText"
CURRENTQUESTION_KEY = "currentQuestionIndex"
STATE_KEY = "state"
LOCALE = "locale"
 
COUNTER = 0
QUIZSCORE = 0
GAME_LENGTH = 20
ANSWER_COUNT = 3
 
game_state = GAME_STATE_START
 
"""
 * When editing your questions pay attention to your punctuation. Make sure you use question marks or periods.
 * Make sure the first answer is the correct one. Set at least ANSWER_COUNT answers, any extras will be shuffled in.
"""
 
languageSupport = {
    "en-US": {
        "translation": {
            "QUESTIONS": [
    	{
        	"You want to park uphill on a two-way road and there is no curb. Which way do you turn your front wheels?":
            ["Left - Towards the center of the road.", "So they face straight ahead.", "Right- Towards the side of the road."]},
    	{	
        	"A solid yellow line next to a broken yellow line means that vehicles.":
            ["Next to the broken line may pass.", "In both directions may pass.", "Next to the solid line may pass."]},
    	{
        	"You must notify DMV within 5 days if you.":
        	[" Sell or transfer your vehicle.", "Are cited for a traffic violation.", "Paint your vehicle a different color."]
    	},
    	{
       	 "Drivers are required to obey instructions from.":
        	[" Other drivers whose vehicles are broken down on the roadway.", "Security guards patrolling parking lots.", "No more than 200 feet before making a right turn."]},
    	{
        	"It is illegal for a person 21 years of age or older to drive with a blood alcohol concentration (BAC) that is blank or higher.":
            ["0.08% - Eight hundredths of one percent.", "0.10% - One tenth of one percent.", "0.05% - Five hundredths of one percent."]
    	},
    	{
        	"If the roadway is wet and your vehicle starts to skid, you should.":
            ["Slowly ease your foot off the gas pedal.",
        	"Slow down by shifting to a slower gear.",
        	"Slow down by pumping the breaks quickly and firmly."]
    	},
    	{
        	"You may drive in a bike lane.":
        	["No more than 200 feet before making a right turn.", "If you drive slower than 15 MPH.", "Whenever bicyclist are not present."]
    	},
    	{
            "Driving under the influence of any medication which impairs your driving is permitted.":
            ["Under no circumstances", "If you don't feel drowsy.", "If it is prescribed by a physician."]
    	},
    	{
            "When you back up in a passenger vehicle.":
            ["Look over your right shoulder through your rear window.", "Rely on your rearview mirror.", "Only use your side and your rearview mirrors."]
    	},
     	{
            "California's 'Basic Speed Law' says you must.":
            ["Never drive faster than is safe for current conditions.", "Keep your speed close to that of other traffic.", "Always drive at the posted speed limit."]
    	},
    	{
            "Generally speaking, you are in a large truck's blind spot if you.":
            ["Cannot see the truck driver in the truck's side mirrors.", "Drive close to the large truck's left front wheel.", "Follow no closer than ten feet behind the large truck."]
    	},
    	{
            "Which of the following is true about the use of your turn signals?":
        	["You must always signal for lane changes.", "You should never use both electric and hand signals.", "If you signal for a lane change, other drivers must let you in."]
    	},
    	{
        	"Two sets of solid double yellow lines spaced two feet or more apart.":
            ["Should be treated like a solid wall and not be crossed.", "May only be crossed to make a left turn or U-turn.", "May be used to begin or end left-hand turns."]
    	},
    	{
        	"When driving in the far right lane of a freeway, you.":
            ["Should expect merging vehicles at on-ramps.", "Must be driving slower than other traffic.", "Must give the right-of-way to merging traffic."]
    	},
    	{
            "Which statement is true about motorcyclist and motorist?": [
            "Motorcyclist have the same rights/responsibilities as other motorist.", "Motorcyclist are not allowed to drive faster than other traffic during congested road conditions.", "Motorcycles are heavier than other vehicles and are less affected by wind/rain."]
    	},
    	{
            "Unless prohibited by a sign, you may legally make a U-turn.": [
        	"At an intersection with a green light.", "At an intersection with a one-way street.", "In front of a fire station."]
    	},
    	{
        	"If you cannot stop safely at a yellow traffic light, you should.": [
            "Enter the intersection cautiously and continue across.", "Stop your vehicle before entering the intersection anyway.", "Stop your vehicle in the intersection and back up carefully."]
    	},
    	{
            "Parking is NEVER permitted.": [
         	"In a crosshatched (diagonal) pattern space.", "Twenty feet from a railroad track.", "In a bicycle lane, unless otherwise posted."]
    	},
    	{
        	"You may legally turn right on a solid red light in Virginia.": [
        	"Only after stopping unless otherwise posted.", "Only after slowing down and checking traffic.", "Under no circumstances."]
    	},
    	{
        	"You must yield the right-of-way to an emergency vehicle by.": [
            "Driving as near to the right edge of the road as possible and stopping.", "Moving into the right lane and driving slowly until is has passed.", "Stopping immediately, even if you are in an intersection."]
    	},
    	{
            "Which child requires a child passenger restraint system?": [
        	"A 7 year old who is 4 feet 7 inches tall.", "A 6 year old who is 4 feet 10 inches tall.", "An 8 year old who is 4 feet 9 inches tall."]
    	},
    	{
            "Smoking inside a vehicle when a person younger than 18 years of age is present is.": [
            "Illegal at all times.", "Legal, if it is your child.", "Not restricted by law."]
    	},
    	{
        	"If it starts to rain on a hot day, the road is most slippery.": [
        	"For the first few minutes.", "After it has been raining for a few hours.", "After it has stopped raining."]
    	},
    	{
        	"The 'three-second rule' applies to the space blank of your vehicle.": [
            "Ahead.", "In back", "To the sides."]
    	},
    	{
        	"You are crossing an intersection and an emergency vehicle is approaching with a siren and flashing lights. You should.": [
            "Continue through the intersection, pull to the right, and stop.", "Stop immediately in the intersection until it passes.", "Pull to the right in the intersection and stop."]
    	},
    	{
        	"A law enforcement officer notices that one of your passengers is not wearing a seat belt and writes a citation. Which of the following is true?": [
        	"You can receive the citation if the passenger is younger than 16.", "Both you and your passenger will receive a citation.", "No toys", "Your passenger will receive the citation, regardless of his or her age."]
    	},
    	{
            "Orange-colored road signs warn you of.": [
        	"Road workers or rad equipment ahead.", "A school zone ahead.", "A traffic signal ahead."]
    	},
    	{
        	"To make a right turn onto a two-way street from a two-way street, start in the right-hand lane and end in.": [
        	"the lane closest to the curb.", "The left lane.", "Any lane that is available."]
    	},
    	{
            "Driving along the right-rear side of another vehicle is.": [
            "Dangerous because you are probably in one of the driver's blind spots.", "A good defensive drivers technique to avoid drivers' blind spots.", "A good way to maintain a space cushion on your left side."]
    	},
    	{
        	"If you see orange construction signs or cones on a freeway, you must.": [
        	"Be prepared for workers and equipment ahead.", "Slow down because the lane ends ahead.", "Change lanes and maintain your current speed."]
    	},
    	{
        	"You are being chased by a police vehicle with its lights and sirens activated. You ignore the warning to stop and speedway. During the chase, a person is seriously injured. You are subject to.": [
            "Imprisonment in a state prison for up to seven years.", "A fine of not less than $1,000.", "Attending an anger-management class."]
    	},
    	{
            "Before driving into an intersection from a stop, you should look.": [
            "Left, right, and left again.", "Left and right only.", "Straight ahead and to the left."]
    	},
    	{
            "Weaving in and out of freeway lanes during heavy traffic.": [
            "Causes further traffic congestion by slowing down other vehicles.", "Improves traffic flow by creating space for others to merge.", "Increases fuel efficiency."]
    	},
    	{
        	"If a pedestrian is in a crosswalk in the middle of a block.": [
        	"The pedestrian has the right-of-way.", "The pedestrian must yield the right-of-way.", "Vehicles have the right-of-way, but drivers must legally take care for the pedestrians safety."]
    	},
    	{
        	"When sharing the road with a light rail vehicle, you.": [
            "Should monitor all traffic signals closely because light rail vehicles can interrupt traffic signals.", "May not drive in the lane next to the light rail vehicle.", "May turn in front of an approaching light rail vehicle at an uncontrolled intersection."]
    	}
 
	],
            "GAME_NAME" : "Driving Quiz", # Be sure to change this for your skill.
            "HELP_MESSAGE": "I will ask you {0} multiple choice questions. Respond with the number of the answer. " +
        	"For example, say one, two, or three. To start a new game at any time, say, start game. ",
            "REPEAT_QUESTION_MESSAGE": "To repeat the last question, say, repeat. ",
            "ASK_MESSAGE_START": " What would you like to do? ",
            "HELP_REPROMPT": "To give an answer to a question, respond with the number of the answer. ",
            "STOP_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "CANCEL_MESSAGE": "Ok, let's play again soon.",
            "NO_MESSAGE": "Ok, we'll play another time. Goodbye!",
            "TRIVIA_UNHANDLED": "Try saying a number between 1 and %s",
            "HELP_UNHANDLED": "Say yes to continue, or no to end the game.",
            "START_UNHANDLED": "Say start to start a new game.",
            "NEW_GAME_MESSAGE": "Welcome to {0}. ",
            "WELCOME_MESSAGE": "I will ask you {0} questions, try to get as many right as you can. Just say the number of the answer. Let's begin. ",
            "ANSWER_CORRECT_MESSAGE": "correct. ",
            "ANSWER_WRONG_MESSAGE": "wrong. ",
            "CORRECT_ANSWER_MESSAGE": "The correct answer is {0}: {1}. ",
            "ANSWER_IS_MESSAGE": "That answer is ",
            "TELL_QUESTION_MESSAGE": "Question {0}. {1} ",
            "GAME_OVER_MESSAGE": "You got {0} out of {1} questions correct. Thank you for playing!",
            "SCORE_IS_MESSAGE": "Your score is {0}. "
 	}
	}
}
 
# --------------- entry point -----------------
 
def lambda_handler(event, context):
	""" App entry point  """
	if event['request']['type'] == "LaunchRequest":
    	return on_launch(event['request'], event['session'])
	elif event['request']['type'] == "IntentRequest":
    	return on_intent(event['request'], event['session'])
	elif event['request']['type'] == "SessionEndedRequest":
    	return on_session_ended()
 
# --------------- response handlers -----------------
 
def on_intent(request, session):
	""" called on Intent """
	intent = request['intent']
	intent_name = request['intent']['name']
    #print("on_intent " +intent_name)
	#print(request)
 
	getstate(session)
	locale = getlocale(request, session)
 
	if get_game_state() == GAME_STATE_TRIVIA:       
    	return rungame(request, session, locale, intent, session)
    	
	return help_handler(False, request, locale, session)
 
def rungame(request, newgame, locale, intent, session):
	""" process the game questions and user response """
	intent_name = request['intent']['name']
	resource = getresource(locale)
 
	if 'dialogState' in request:
    	#delegate to Alexa until dialog sequence is complete
    	if request['dialogState'] == "STARTED" or request['dialogState'] == "IN_PROGRESS":
        	attributes = {"locale":locale}
        	return dialog_response(attributes, False)
	
	if intent_name == "AMAZON.StartOverIntent":
    	return start_game(request, True, locale)
	elif intent_name == "AMAZON.RepeatIntent":
    	reprompt = session['attributes'][REPROMPT_KEY]
    	return rebuild_response(request, locale, session, reprompt )
	elif intent_name == "AMAZON.CancelIntent":
    	return cancel_response(locale)
    elif intent_name == "AMAZON.StopIntent":
    	return cancel_response(locale)
	elif intent_name == "AMAZON.HelpIntent":
    	return dohelp(request, False, locale)
	elif intent_name == "AnswerIntent":
    	return processuserguess(False, request, session, intent, locale)
	elif intent_name == "DontKnowIntent":
    	return processuserguess(True, request, session, intent, locale)
	return dohelp(request, False, locale)
 
def processuserguess(usergaveup, request, session, intent, locale):
	""" process the users response, builf next question if required """
  
	resource = getresource(locale)
	speech_output = ""
 
	game_questions = session['attributes'][GAME_QUESTIONS_KEY]
	correct_answer_index_previous_question = int(session['attributes'][CORRECTANSWERINDEX])
	current_score = int(session['attributes'][SCORE])
    current_question_index_previous_question = int(session['attributes'][CURRENTQUESTION_KEY])
	correct_answer = session['attributes'][ANSWERTEXT_KEY]
 
	if match_guess_with_answer(intent, correct_answer_index_previous_question):	
   	current_score += 1
   	speech_output = resource["ANSWER_CORRECT_MESSAGE"]
	else:
    	if usergaveup == False:        	
	       speech_output = resource["ANSWER_WRONG_MESSAGE"]
                         
    	speech_output += resource["CORRECT_ANSWER_MESSAGE"].format(correct_answer_index_previous_question, correct_answer)
 
	if current_question_index_previous_question >= (GAME_LENGTH - 1):
    	speech_message = ""
    	if usergaveup == False:
           speech_message = resource["ANSWER_IS_MESSAGE"]
    	
    	speech_message += speech_output + resource["GAME_OVER_MESSAGE"].format(str(current_score), str(GAME_LENGTH))
    	return response("", response_plain_text(speech_message, True))  
	
    current_question_index_next_question = current_question_index_previous_question + 1	
    correct_answer_index_next_question = random.randrange(0, ANSWER_COUNT-1, 1)	
    	
	new_questions = game_questions[current_question_index_next_question]
        	
	round_answers = populate_round_answers(new_questions,
                    current_question_index_next_question, correct_answer_index_next_question)
     	
    correct_answer_text_next_question = round_answers[correct_answer_index_next_question]	
      	
	reprompt = get_answers_text(game_questions[current_question_index_next_question], round_answers,
               current_question_index_next_question, locale)
        	
	if usergaveup == False:
       speech_message  = resource["ANSWER_IS_MESSAGE"]
	else:
    	speech_message = ""  
	speech_message += speech_output + " " + resource["SCORE_IS_MESSAGE"].format(str(current_score)) + " " + reprompt
 
    correct_answer_index_next_question += 1	
    set_game_state(GAME_STATE_TRIVIA)
 
	attributes = { SPEECHOUTPUT_KEY: reprompt,
                      REPROMPT_KEY: reprompt,
                      CURRENTQUESTION_KEY: str(current_question_index_next_question),
                      CORRECTANSWERINDEX: str(correct_answer_index_next_question),
                      GAME_QUESTIONS_KEY: game_questions,
                      SCORE: str(current_score),
                      ANSWERTEXT_KEY: correct_answer_text_next_question,
                      STATE_KEY: get_game_state(),
                      LOCALE: locale
             	}
	
	return response(attributes, speech_response_prompt_card(resource["GAME_NAME"],speech_message, reprompt, False))
 
 
def match_guess_with_answer(intent, correctAnswerIndex):
	""" check if answer matches """ 
	if 'slots' in intent:
    	slots = intent['slots']
    	for key, val in slots.items():        	
        	if val.get('value'):
            	if (val.get('value')).isdigit():
                    lval = int(val['value'].lower())
             	   if lval == correctAnswerIndex and lval <= ANSWER_COUNT and lval > 0:
                        #print("user answered " + str(lval) + " correct answer number is: " + str(correctAnswerIndex))
                        return True
	return False
   	
  
def cancel_response(locale):
	""" """
	resource = getresource(locale)
	speechmessage = resource["CANCEL_MESSAGE"]
	return response("", response_plain_text(speechmessage, True))
 
def rebuild_response(request, locale, session, speech_message):
	""" """
 
	speech_output = session['attributes'][SPEECHOUTPUT_KEY]
	reprompt = session['attributes'][REPROMPT_KEY]
	game_questions = session['attributes'][GAME_QUESTIONS_KEY]
    correct_answer_index = session['attributes'][CORRECTANSWERINDEX]
	current_score = session['attributes'][SCORE]
    current_question_index = session['attributes'][CURRENTQUESTION_KEY]
    correct_answer_text = session['attributes'][ANSWERTEXT_KEY]
    set_game_state(GAME_STATE_TRIVIA)
 
	attributes = { SPEECHOUTPUT_KEY: reprompt,
                  REPROMPT_KEY: reprompt,
                  CURRENTQUESTION_KEY: current_question_index,
                  CORRECTANSWERINDEX: correct_answer_index,
                  GAME_QUESTIONS_KEY: game_questions,
              	SCORE: current_score,
                  ANSWERTEXT_KEY: correct_answer_text,
                  STATE_KEY: get_game_state(),
                  LOCALE: locale
             	}
 
	return response(attributes, response_plain_text_promt(speech_message, speech_message, False))
 
def dohelp(request, newgame, locale):
	""" display help for selected locale """
	
	resource = getresource(locale)
	askmessage =  resource["REPEAT_QUESTION_MESSAGE"] +" " +resource["ASK_MESSAGE_START"]
	speech_message = resource["HELP_MESSAGE"].format(resource["GAME_NAME"]) + askmessage
 
    set_game_state(GAME_STATE_HELP)
	attributes = {
                 STATE_KEY: get_game_state()              	
             	}
	return response(attributes, response_plain_text_promt(speech_message, speech_message, False))
 
def help_handler(newgame, request, locale, session):
	""" help handler """
 
	intent_name = request['intent']['name']
	resource = getresource(locale)
	if newgame == True:
         askmessage = resource["ASK_MESSAGE_START"]
	else:
     	askmessage = resource["REPEAT_QUESTION_MESSAGE"] + resource["ASK_MESSAGE_START"]
 	
	if intent_name == "AMAZON.StartOverIntent":
        print("help state: startover intent")
 	   set_game_state(GAME_STATE_START)
    	return start_game(request, False, locale)
 
	elif intent_name == "AMAZON.RepeatIntent":
        print("help state: repeat intent")
    	if SPEECHOUTPUT_KEY in session['attributes']:
        	if not( session['attributes'][SPEECHOUTPUT_KEY] is None) and not(session['attributes'][REPROMPT_KEY] is None):
            	return dohelp(False, request, session, locale)
    	return dohelp(request, True, locale)
 
	elif intent_name == "AMAZON.CancelIntent":
    	return cancel_response(locale)
 
	elif intent_name == "AMAZON.StopIntent":
    	return cancel_response(locale)
 
	elif intent_name == "AMAZON.HelpIntent":
    	if SPEECHOUTPUT_KEY in session['attributes']:
     	   if not( session['attributes'][SPEECHOUTPUT_KEY] is None) and not(session['attributes'][REPROMPT_KEY] is None):
            	return dohelp(request, False, locale)
    	return dohelp(request, True, locale)	
 	
	speechmessage = resource["HELP_MESSAGE"].format(GAME_LENGTH) + askmessage
    set_game_state(GAME_STATE_HELP)   
	attributes = {
                  STATE_KEY: get_game_state()              	
             	}
	return response(attributes, response_plain_text(speechmessage, False))	
 	
def on_launch(request, session):
	""" start """
    #print("launch")
    set_game_state(GAME_STATE_TRIVIA)
	return start_game(request, True, getlocale(request, session))
 
def start_game(request, newgame, locale):
	""" start a new game """
	
	resource = getresource(locale)
 
	speechOutput = ""
	if newgame == True:
   	speechOutput = resource["NEW_GAME_MESSAGE"].format(resource["GAME_NAME"]) + resource["WELCOME_MESSAGE"].format(str(GAME_LENGTH))
        
    current_question_index = 0
	
	questions = get_question_list(locale)
    correct_answer_index = random.randrange(0, ANSWER_COUNT - 1, 1)
    	
	round_answers = populate_round_answers(questions[current_question_index],
    	current_question_index, correct_answer_index)
    correct_answer_text = round_answers[correct_answer_index]
	
	reprompt = get_answers_text(questions[current_question_index], round_answers, current_question_index, locale)
	speech_message = speechOutput + reprompt
	
    correct_answer_index += 1	
    set_game_state(GAME_STATE_TRIVIA)
	
	attributes = { SPEECHOUTPUT_KEY: speech_message,
                  REPROMPT_KEY: reprompt,
                  CURRENTQUESTION_KEY: str(current_question_index),
                  CORRECTANSWERINDEX: str(correct_answer_index),
                  GAME_QUESTIONS_KEY: questions,
                  SCORE: "0",
                  ANSWERTEXT_KEY: correct_answer_text,
                  STATE_KEY: get_game_state(),
      	        LOCALE: locale
             	}
 
	return response(attributes, speech_response_prompt_card(resource["GAME_NAME"],speech_message, reprompt, False)) 	
 
def populate_round_answers(question, correct_question_index, correct_answer_index):
	""" get answers for a given question, place correct answer at the spot marked by the/
        correctAnswerIndex.
	"""
	for theanswers in question.values():    	
    	tmp_answer = theanswers[0]    	
        theanswers.remove(tmp_answer)
  	  theanswers_randomised = random.sample(theanswers, len(theanswers) )
        theanswers_randomised.insert(correct_answer_index, tmp_answer)
        theanswers.insert(correct_question_index, tmp_answer)
    	return theanswers_randomised
 
def getstate(session):
	""" get and set the current state  """
 
	if STATE_KEY in session['attributes']:
        set_game_state(session['attributes'][STATE_KEY])
	else:
        set_game_state(GAME_STATE_START)
 
def get_answers_text(question, reorderedquestion, current_question_index, locale):
	""" get text for the answer """
	number = current_question_index + 1
	resource = getresource(locale)
	k = list(question.keys())
	questiontext = k[0]
	outtext = resource["TELL_QUESTION_MESSAGE"].format(str(number), questiontext) + " "
	
	index = 0
	for qtext in reorderedquestion:
    	outtext += str(index + 1) + ". " + qtext +". "
    	index += 1    	
    	if index == ANSWER_COUNT:
 	       break
 
	return outtext[:-1]  
 
def get_game_state():
	""" """
	global game_state
	return game_state
 
def set_game_state(state):
	""" """
	global game_state
	game_state = state
 
def getresource(locale):
	""" """
	return languageSupport[locale]["translation"]
 
def getlocale(request,session):
	""" """
	locale = request['locale']
	if locale == "":
   	attributes = session['attributes']
       attributes['locale']
 
	if locale == "":
    	locale = "en-US"
	
	return locale
 
def on_session_ended():
	""" called on session end  """
    #print(on_session_ended)
 
 
def get_question_list(locale):
	""" """
	global GAME_LENGTH
	questions  = []
	res = getresource(locale)
	ilen = len(res["QUESTIONS"])
	questionsample = random.sample(range(0, ilen), GAME_LENGTH)
	for index in questionsample:
        questions.append(res["QUESTIONS"][index])
	return questions
 
# --------------- speech response handlers -----------------
# build the json responses
 
def response_plain_text(output, endsession):
	""" create a simple json plain text response  """
	return {
        'outputSpeech': {
        	'type': 'PlainText',
        	'text': output
    	}, 	
    	'shouldEndSession': endsession
	}
 
def response_plain_text_promt(output, reprompt_text, endsession):
	""" create a simple json plain text response  """
	return {
        'outputSpeech': {
        	'type': 'PlainText',
        	'text': output
 	   },
    	'reprompt': {
            'outputSpeech': {
        	'type': 'PlainText',
        	'text': reprompt_text
        	}
    	},
        'shouldEndSession': endsession
	}
 
def response_ssml_text(output, endsession):
	""" create a simple json plain text response  """
	return {
        'outputSpeech': {
        	'type': 'SSML',
        	'ssml': "<speak>" +output +"</speak>"
    	},
        'shouldEndSession': endsession
	}
 
def response_ssml_text_card_image(title, output, endsession, cardtext, smallimage, largeimage):
	""" create a simple json plain text response  """
	return {
    	'card': {
        	'type': 'Standard',
        	'title': title,
        	'text': cardtext,
        	'image':{
                'smallimageurl':smallimage,
                'largeimageurl':largeimage
        	},
    	},
        'outputSpeech': {
        	'type': 'SSML',
        	'ssml': "<speak>" +output +"</speak>"
    	},
    	'shouldEndSession': endsession
	}
 
def response_ssml_text_card(title, output, endsession):
	""" create a simple json plain text response  """
	return {
    	'card': {
        	'type': 'Simple',
        	'title': title,
        	'content': output
    	},
        'outputSpeech': {
        	'type': 'SSML',
        	'ssml': "<speak>" +output +"</speak>"
    	},
        'shouldEndSession': endsession
	}
 
def speech_response_prompt_card(title, output, reprompt_text, endsession):
    """  create a simple json response with a card  """
	return {
        'outputSpeech': {
        	'type': 'PlainText',
        	'text': output
    	},
     	'card': {
        	'type': 'Simple',
        	'title': title,
        	'content': reprompt_text
    	},
    	'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
        	}
    	},
        'shouldEndSession': endsession
	}
 
 
def response_ssml_text_reprompt(title, output, endsession, repromt_text):
    """  create a simple json response with a card  """
	return {
        'outputSpeech': {
        	'type': 'SSML',
        	'ssml': "<speak>" +output +"</speak>"
    	},
    	'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>" +repromt_text +"</speak>"
        	}
    	},
        'shouldEndSession': endsession
	}
 
def dialog_response(attributes, endsession):
    """  create a simple json response with card """
	return {
    	'version': '1.0',
        'sessionAttributes': attributes,
    	'response':{
            'directives': [
            	{
                    'type': 'Dialog.Delegate'
            	}
        	],
            'shouldEndSession': endsession
    	}
	}
 
def response(attributes, speech_response):
	""" create a simple json response """
	return {
    	'version': '1.0',
        'sessionAttributes': attributes,
    	'response': speech_response
	}
