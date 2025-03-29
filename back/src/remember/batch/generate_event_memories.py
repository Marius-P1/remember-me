from remember.batch.schema import EventMemories
from remember.batch.conf import model
from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate(
    [
        ("system", """Tu es un générateur de souvenirs narratifs, capable de simuler différents styles d’écriture, 
                      tons émotionnels et points de vue. Tu adoptes le rôle de plusieurs proches d'une personne agée pour raconter leurs souvenirs de leur point de vue pour un même évènement."""),
        ("human", """Invente {nb_memories} souvenirs riches, spécifiques et émotionnels racontés par différents proches de la personne agée et liés à un même évènement ‘‘‘{event}‘‘‘. 
                      Chaque souvenir doit être rédigé à la première personne, dans un style adapté à la personnalité du narrateur.

                      **Contexte de la personne agée** :
                        - Nom : {name}
                        - Âge : {age}
                        - Ancienne profession : {occupation}
                        - Elle a une mémoire défficiente, et ses proches souhaitent lui faire revivre des moments heureux à travers ces souvenirs.
                     
                     Rédige les souvenirs à la première personne au sujet de l'évènement : ‘‘‘{event}‘‘‘. 
                     Chaque souvenir est rédigé par un proche distinct (par exemple amis, enfants, petits-enfants, voisins, collègues retraités, etc.).
                     Chaque souvenir doit être spécifique et détaillées et en intégrant les émotions ressenties. Utilise des anecdotes.
                     """
        )
    ]
)
chain = prompt_template | model.with_structured_output(EventMemories)


def generate_event_memories(event: str, name: str, age: int, occupation: str, nb_memories: int) -> EventMemories:
    """
    Generate a list of memories for a given event.
    :param event: The event for which to generate memories.
    :param name: The name of the elderly person.
    :param age: The age of the elderly person.
    :param occupation: The past occupation of the elderly person.
    :param nb_memories: The number of memories to generate.
    """
    # Call the chain with the provided arguments
    event_memories = chain.invoke({"name": name,
                                   "age": age,
                                   "occupation": occupation,
                                   "event": event,
                                   "nb_memories": nb_memories})
    return event_memories

def save_event_memories(event_memories: EventMemories, filename: str):
    """
    Save the generated memories to a JSON file.
    :param event_memories: The EventMemories object to save.
    :param filename: The name of the file to save the memories to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(event_memories.model_dump_json(indent=2))

def load_event_memories(filename: str) -> EventMemories:
    """
    Load memories from a JSON file.
    :param filename: The name of the file to load the memories from.
    :return: An EventMemories object containing the loaded memories.
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        event_memories = EventMemories.model_validate_json(data)
    return event_memories