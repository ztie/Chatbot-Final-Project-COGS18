"""Test for my functions."""

from chatbot_functions import *

def test_disorder_filter():

    assert isinstance(disorder_filter(["what","is","the","cause","for", "depression"],DISORDERS, CATEGORIES),list)
    assert disorder_filter(["what","is","the","cause","for", "depression"], DISORDERS, CATEGORIES) == ["depression", "cause"]
                                      
        
def test_find_disorder():

    assert isinstance(find_disorder(disorders,"bipolar"),object)
    assert find_disorder(disorders, "bipolar") == bipolar
    
    
def test_find_output():
    
    assert isinstance(find_output(disorders,["schizophrenia","symptom"]),str)
    assert find_output(disorders,["schizophrenia","symptom"]) ==  '1. Having false beliefs\n        2. Hearing voices that others do not\n        3. Reduced emotional expression\n        4. Lack of motivation\n'