from steps.preprocess import clean_input, tag_keywords
from steps.inference import run_inference
from steps.postprocess import summarize_response
from monitor import log_result

def process_pipeline(raw_input: str):
    try:
        log_result("preprocessing", "started", raw_input)
        cleaned = clean_input(raw_input)
        tagged = tag_keywords(cleaned)
        log_result("preprocessing", "success", raw_input, tagged)

        log_result("inference", "started", tagged)
        response = run_inference(tagged)
        log_result("inference", "success", tagged, response)

        summary = summarize_response(response)
        log_result("postprocessing", "success", response, summary)

        return summary

    except Exception as e:
        log_result("pipeline", "error", raw_input, error=str(e))
        return f"Pipeline failed: {e}"