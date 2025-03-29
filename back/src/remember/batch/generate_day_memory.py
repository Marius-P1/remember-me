from remember.batch.schema import DayMemory, EventMemories
from remember.batch.conf import model
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", """Tu es un assistant bienveillant spécialisé dans la stimulation de la mémoire émotionnelle chez les personnes 
                      âgées ayant une déficience de leur mémoire. Tu aides à raviver les souvenirs marquants à travers des récits narratifs, sensoriels et profondément humains."""),
        ("user", """
         Voici les informations sur la personne agée :
            Nom : {name}
            Age : {age}
            Profession : {occupation}
         Voici différents souvenirs exprimées par des proches de la personne agée au sujet de l'évènement :.
            {memories}
         Raconte cet évènement à la personne agée comme une petite histoire intime, d’environ 100 mots, qui lui parle directement.
         Utilise un ton amical, rassurant et affectueux, comme si tu étais un proche.
         Fais vivre l’histoire par les émotions, les détails sensoriels (la lumière, les couleurs, les sons, les sourires…).
         Intègre au moins une anecdote si elle est présente dans les souvenirs fournis.
         Sois doux et encourageant : le but est de faire naître un sourire, une réminiscence, une sensation familière.
         """),
    ]
)
chain = prompt_template | model.with_structured_output(DayMemory)

def generate_day_memory(name: str, age: int, occupation: str, memories: str) -> DayMemory:
    """
    Generate a day memory for a given event.
    :param name: The name of the elderly person.
    :param age: The age of the elderly person.
    :param occupation: The past occupation of the elderly person.
    :param memories: The memories to be used for generating the day memory.
    """
    # Call the chain with the provided arguments
    day_memory = chain.invoke({"name": name,
                                "age": age,
                                "occupation": occupation,
                                "memories": memories})
    return day_memory


def save_day_memory(day_memory: DayMemory, filename: str):
    """
    Save the generated memories to a JSON file.
    :param day_memory: The DayMemory object to save.
    :param filename: The name of the file to save the memories to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(day_memory.model_dump_json(indent=2))

def load_day_memory(filename: str) -> DayMemory:
    """
    Load memories from a JSON file.
    :param filename: The name of the file to load the memories from.
    :return: An DayMemory object containing the loaded memories.
    """
    with open(filename, "r", encoding="utf-8") as file:
        day_memory = DayMemory.model_validate_json(file.read())
    return day_memory