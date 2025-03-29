from langchain.chat_models import init_chat_model

model = init_chat_model("mistral-large-latest", model_provider="mistralai", temperature=0.2)