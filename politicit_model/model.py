from huggingface_hub import snapshot_download
from transformers import TFBertModel, TFAutoModel, AutoTokenizer
from tensorflow import keras
from .preprocessing import preprocess_text


class PoliticITModel:
    def __init__(self, repo_id="leeeov4/PIDIT"):
        local_dir = snapshot_download(repo_id=repo_id)

        self.model = keras.models.load_model(local_dir, custom_objects={
            "TFBertModel": TFBertModel,
            "TFAutoModel": TFAutoModel
        })

        self.bert_tokenizer = AutoTokenizer.from_pretrained(local_dir + "/bert_tokenizer")
        self.alberto_tokenizer = AutoTokenizer.from_pretrained(local_dir + "/alberto_tokenizer")

    def predict(self, text):
        inputs = preprocess_text(text, self.bert_tokenizer, self.alberto_tokenizer)
        outputs = self.model.predict(inputs)

        return outputs