def preprocess_text(text, bert_tokenizer, alberto_tokenizer):
    bert_tokens = bert_tokenizer(text, max_length=250, padding='max_length', truncation=True, return_tensors='tf')
    alberto_tokens = alberto_tokenizer(text, max_length=250, padding='max_length', truncation=True, return_tensors='tf')

    input_dict = {
        'bert_input_ids': bert_tokens['input_ids'],
        'bert_token_type_ids': bert_tokens['token_type_ids'],
        'bert_attention_mask': bert_tokens['attention_mask'],
        'alberto_input_ids': alberto_tokens['input_ids'],
        'alberto_token_type_ids': alberto_tokens['token_type_ids'],
        'alberto_attention_mask': alberto_tokens['attention_mask']
    }
    return input_dict
