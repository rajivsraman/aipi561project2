import os
from pipeline import process_pipeline
from steps.preprocess import clean_input, tag_keywords
from steps.postprocess import summarize_response
from retry_utils import retry

# Test preprocessing logic
def test_clean_input():
    text = "  This is a test. \n\n"
    assert clean_input(text) == "This is a test."

def test_tag_keywords():
    text = "AI models use data to train."
    tagged = tag_keywords(text)
    assert "[AI]" in tagged and "[data]" in tagged

# Test postprocessing
def test_summarize_response():
    response = "This is a long answer. With multiple sentences."
    assert summarize_response(response) == "This is a long answer."

# Test retry mechanism
def test_retry_success():
    counter = {"calls": 0}

    @retry(max_retries=2)
    def flaky_function():
        counter["calls"] += 1
        if counter["calls"] < 2:
            raise Exception("Temporary error")
        return "success"

    assert flaky_function() == "success"
    assert counter["calls"] == 2

# Test pipeline integration
def test_pipeline_integration(monkeypatch):
    def fake_inference(prompt):
        return "This is a mocked Titan response. It ends here."

    # Patch the function as used inside pipeline.py
    monkeypatch.setattr("pipeline.run_inference", fake_inference)

    result = process_pipeline("How is AI used in finance?")
    assert "This is a mocked" in result
