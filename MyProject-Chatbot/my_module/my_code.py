"""A collection of original functions that extend the functionality of the Chatbot from Assignment 3."""


    #Chose to use class to store information because each disorder is going to have the same 6 names of attributes with different content.    
class MentalDisorders():
    
    
    """a class used to represent the 6 mental disorders 
    
    Attributes
    ----------
     name : str
         the name of the disorder.
     definition : str
         the definition of the disorder.
     cause : str
         the biological, psychological, environmental factors that are likely to cause the disorder.
     prevalence : str
         number of people displaying a disorder in the total population at any given time .
     symptom : list of str
         physical or mental features that are regarded as indicating the condition of the disease. 
     treatment : str
         medical care options that can given to a patient suffering from the mental disorder.
   
    """
    
    
    def __init__(self, name, definition, cause, prevalence, symptom, treatment):
        
        
        """
        Parameters
        ----------
         name : str
             the name of the disorder.
         definition : str
             the definition of the disorder.
         cause : str
             the biological, psychological, environmental factors that are likely to cause the disorder.
         prevalence : str
             number of people displaying a disorder in the total population at any given time .
         symptom : list str
             physical or mental features that are regarded as indicating the condition of the disease. 
         treatment : str
             medical care options that can given to a patient suffering from the mental disorder.
    
        """
        
        
        self.name = name 
        self.definition = definition
        self.cause = cause
        self.prevalence = prevalence
        self.symptom = symptom
        self.treatment = treatment
        
        
    #Initialized objects with names of the disorders, passing in informations for all 6 attributes. 
depression = MentalDisorders("depression","A mental disorder characterized by social withdrawal, disorganized thinking, abnormal speech, and an inability to understand reality."
,"The causes include environmental and genetic factors. Possible environmental factors include being raised in a city, cannabis use during adolescence, certain infections, parental age and poor nutrition during pregnancy. Genetic factors include a variety of common and rare genetic variants."
,"1.2% of the U.S. adult.", ["Having false beliefs", "Hearing voices that others do not", "Reduced emotional expression", "Lack of motivation"],"The mainstay of treatment is antipsychotic medication, along with counselling, job training and social rehabilitation.")

bipolar = MentalDisorders("bipolar","A mental health condition that causes extreme mood swings that include emotional highs (mania or hypomania) and lows (depression).", "Bipolar disorder is more common in people who have a first-degree relative, such as a sibling or parent, with the condition. People with bipolar disorder also appear to have physical changes in their brains. ","4.4% of U.S. adults experience bipolar disorder at some time in their lives."
, ["Extremely low mood","Abnormally upbeat", "Jumpy or wired", "Exaggerated sense of well-being and self-confidence (euphoria)", "Racing thoughts"],"Bipolar disorder is treated with three main classes of medication: mood stabilizers, antipsychotics, and, while their safety and effectiveness for the condition are sometimes controversial,antidepressants.")

schizophrenia = MentalDisorders("schizophrenia","A mental disorder characterized by social withdrawal, disorganized thinking, abnormal speech, and an inability to understand reality.","The causes include environmental and genetic factors. Possible environmental factors include being raised in a city, cannabis use during adolescence, certain infections, parental age and poor nutrition during pregnancy. Genetic factors include a variety of common and rare genetic variants."
, "1.2% of the U.S. adult.",["Having false beliefs", "Hearing voices that others do not", "Reduced emotional expression", "Lack of motivation"],"The mainstay of treatment is antipsychotic medication, along with counselling, job training and social rehabilitation.")

delusional_disorder = MentalDisorders("delusional","A generally rare mental illness in which the patient presents delusions, but with no accompanying prominent hallucinations, thought disorder, mood disorder, or significant flattening of affect.","The causes include environmental and genetic factors. Possible environmental factors include being raised in a city, cannabis use during adolescence, certain infections, parental age and poor nutrition during pregnancy. Genetic factors include a variety of common and rare genetic variants.","About 24 to 30 cases per 100,000 people while 0.7 to 3.0 new cases per 100,000 people are reported every year.","The patient expresses an idea or belief with unusual persistence or force, even when evidence suggests the contradictory.That idea appears to have an undue influence on the patient's life, and the way of life is often altered to an inexplicable extent.","Treaments are difficult because most patients failed to regnoize it as a problem. Individual psychotherapy is recommended rather than group psychotherapy, as patients are often quite suspicious and sensitive. Antipsychotics are not well tested in delusional disorder, but they do not seem to work very well, and often have no effect on the core delusional belief.")

schizophreniform_disorder = MentalDisorders("schizophreniform","A mental disorder characterized by social withdrawal, disorganized thinking, abnormal speech, and an inability to understand reality.Different from Schizophrenia, but signs of disruption are not present for the full six months required for the diagnosis of schizophrenia.", "The causes include environmental and genetic factors. Possible environmental factors include being raised in a city, cannabis use during adolescence, certain infections, parental age and poor nutrition during pregnancy. Genetic factors include a variety of common and rare genetic variants.","1.2% of the U.S. adult.",["Having false beliefs", "Hearing voices that others do not", "Reduced emotional expression", "Lack of motivation"], "The mainstay of treatment is antipsychotic medication, along with counselling, job training and social rehabilitation.")

schizoaffective_disorder = MentalDisorders("schizoaffective","A mental disorder characterized by social withdrawal, disorganized thinking, abnormal speech, and an inability to understand reality.Different from Schizophrenia,the diagnosis is made when the person has features of both schizophrenia (usually psychosis) and a mood disorder—either bipolar disorder or depression—but doesn't meet the diagnostic criteria for schizophrenia or a mood disorder separately.", "The causes include environmental and genetic factors. Possible environmental factors include being raised in a city, cannabis use during adolescence, certain infections, parental age and poor nutrition during pregnancy. Genetic factors include a variety of common and rare genetic variants.", "1.2% of the U.S. adult.", ["Having false beliefs", "Hearing voices that others do not", "Reduced emotional expression", "Lack of motivation"]
,"The mainstay of treatment is antipsychotic medication, along with counselling, job training and social rehabilitation.")


    #List of mental disorders the chatbot is able to answer questions on. 
    #It will be later used in the function "disorder_filter()".
DISORDERS = ["depression","bipolar","schizophrenia","delusional","schizophreniform","schizoaffective"]

    #List of aspects of the disorders the chatbot is able to answer questions on. 
    #It will also be later used in the function "disorder_filter()".
CATEGORIES =["definition","cause","causes","prevelance","symptom","symptoms","treatment","treatments"]


def disorder_filter(msg, DISORDERS, CATEGORIES):
    
    
    """
    a function that takes in input message from the user and return the name of the disorder within the 6 disorders specificed in the list DISORDERS, and the aspect of the disorder within the 6 aspects specified in the list CATEGORIES if found. 


    Parameters
    ----------
    msg : list string
        takes the output of function "prepare_text()"(specific in the module existing_code) as an input
        example: ["what", "is", "the", "cause", "of", "depression"]
    

    Returns
    -------
    found : list
       a list of strings that include the name of the disorder, and the aspect of the disorder that the user is interested in. 
       
    """
    
    
    #initialize illness and aspect as None.
    illness = None
    aspect = None
   
    # Loop over msg
    for word in msg:
        
        # Checking for disorders
        if illness == None: 
            if word in DISORDERS:
                illness = word
                
        #Checking for aspect 
        if aspect == None:
            if word in CATEGORIES:
                aspect = word
             
        #When both found, the information is stored a list of strings in "found"
        if illness != None and aspect!= None:
            found = [illness, aspect]
            return found 
        
    #If not both found, returns None    
    return None 
   

    #Initialized a list of disorders that are going to be used in functions "find_disorder()" and "find_ouput()"    
disorders = [depression,bipolar,schizophrenia,delusional_disorder,schizophreniform_disorder,schizoaffective_disorder]


def find_disorder(disorders,name):
    
    
    """
    a function that takes in the name of the disorder to find the disorder object with its corresponding name. 
    
    Parameters
    ----------
    name : string
        the name of the disorder
 

    Returns
    -------
    disordr : object
       the object of a specific disorder
       
    """
    
    
    #Loop over all the disorders in the list disorders
    for disorder in disorders:
        
        #Check if the name passed in is the same as the attribute "name" for any disorders.
        if name == disorder.name:
            
            #the specific disorder object is returned
            return disorder
        
        
def find_output(disorders,found):
    
    
    """
    a function that takes in the name and the aspect of the disorder to return the corresponding information retrived from the object of the disorder. 

    Parameters
    ----------
    found: list
        a list of strings that include the name of the disorder, and the aspect of the disorder that the user is interested in. 
        

    Returns
    -------
    The corresponding attribute from the disorder object.
       
    """
    
    
    #Each if/else statement has the same following structure:
        #if the second string in the list "found", which is the aspect of the disorder is found as "definition"
    if found[1] == "definition":
        #the attribute "definition" of the specific disorder is returned.
        return find_disorder(disorders,found[0]).definition
    
    elif found[1] == "cause" or found[1] == "causes":
        return find_disorder(disorders,found[0]).cause
    
    elif found[1] == "prevalence":
        return find_disorder(disorders,found[0]).prevalence
    
    elif found[1] == "symptom" or found[1] =="symptoms":
        
        output = ""
        number = 1;
        space = "        ";
        
        #loop through the list of symtoms strings in for the specific disorder.
        for symptom in find_disorder(disorders,found[0]).symptom:
            
            #if it is the first symptom in the list.
            if number == 1:
                #the output would be the contatenation of the empty space, the number as a string, ". ", the specific symptom, and line change.
                output = output + str(number)+". "+symptom+ "\n"
            
            # if it is not the first symptom in the list.       
            else:
                #the output would be the same thing, except for the addition of more empty space (space) so the symptoms can line up when displayed.
                output = output + space + str(number)+". "+symptom+ "\n"
            #increment number by 1 for printing purposes    
            number = number + 1 
            
        return output
    
    else:
        return find_disorder(disorders,found[0]).treatment
        
        
        
        
        
        
        
        
        
        
        
