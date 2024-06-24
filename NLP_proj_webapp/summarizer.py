from transformers import pipeline

def summary_text(text, summary_length = "short"):
    summarizer = pipeline("summarization", model="./Models/mt5_base_finetuned_model", tokenizer="./Models/mt5_base_finetuned_token")

    if summary_length == "short":
        return summarizer(text, max_length=75, min_length=30, length_penalty=2.0, num_beams=4)
    
    if summary_length == "long":
        return summarizer(text, max_length=120, min_length=50, length_penalty=2.0, num_beams=4)



