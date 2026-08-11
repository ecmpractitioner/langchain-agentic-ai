from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from shared.utils.load_env import load_and_return_api_key
from shared.utils.llm_calls import call_openai_llm

api_key = load_and_return_api_key("OPENAI_API_KEY")


def summarize_text(text: str, api_key: str) -> str:
    summary_template = """
    given the information {information} about a country, I want you to create:
    1. A short summary
    2. Two interesting facts about the country
    """
    summary_prompt_template = PromptTemplate(
        input_variables=[text], template=summary_template
    )
    # using openai model
    # llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")
    # we will use ollama from the local desktop
    llm = ChatOllama(temperature=0, model="gemma3:270m")
    chain = summary_prompt_template | llm
    # print(chain)

    response = chain.invoke(input={"information": text})

    return response.content


if __name__ == "__main__":
    text = """
India, officially the Republic of India,[j][19] is a country in South Asia. It is the world's seventh-largest country by area and the largest by population.[20] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[k] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is near Sri Lanka and the Maldives.[l]

Modern humans arrived on the Indian subcontinent from Africa by 55,000 years ago.[22][23][24] Their long, isolated occupation as hunter-gatherers made the region highly diverse.[25] Settled life emerged on the western margins of the Indus basin 9,000 years ago, evolving into the Indus Valley Civilisation by the third millennium BCE.[26] By 1200 BCE, an archaic form of Sanskrit, spread into India from the northwest,[27][28] its hymns recording the early dawnings of Hinduism.[29] Northern Dravidian languages were supplanted.[30] By 400 BCE, caste emerged within Hinduism,[31] while Buddhism and Jainism arose, proclaiming social orders unlinked to heredity.[32] In the loose-knit Maurya and Gupta Empires,[33] art, architecture, and writing flourished,[34] women's status declined,[35] and untouchability became organised.[m][36] In South India, Middle kingdoms exported Dravidian language scripts and cultures to Southeast Asia.[37] In the 1st millennium, Judaism, Christianity, Islam and Zoroastrianism became established on India's southern and western coasts.[38]

Early in the 2nd millennium, Central Asian Muslim conquests[39] established the Delhi Sultanate, integrating northern India into the Islamic cosmopolis.[40] In south India, the Vijayanagara Empire created a long-lasting composite Hindu culture,[41] while Sikhism emerged in the Punjab, rejecting institutionalised religion.[42] The Mughal Empire ushered in two centuries of economic expansion and relative peace,[43] leaving a rich architectural legacy.[44][45] Gradually expanding rule of the British East India Company turned India into a colonial economy but consolidated its sovereignty.[46] British Crown rule began in 1858. The rights promised to Indians were granted slowly,[47][48] but technological changes were introduced, and modern education and the public life took root.[49] A nationalist movement emerged in India, the first in the non-European British Empire.[50][51] Noted for nonviolent resistance after 1920,[52] it became the primary factor in ending British rule.[53] In 1947, the British Indian Empire was partitioned into two independent dominions, a Hindu-majority dominion of India and a Muslim-majority dominion of Pakistan. A large-scale loss of life and an unprecedented migration accompanied the partition.[54]

Since 1950, India has been a federal republic, governed through a democratic parliamentary system. It is a pluralistic, multilingual and multi-ethnic society. India's population grew from 361 million in 1951 to over 1.4 billion in 2023.[55] Its fast-growing economy is a hub for information technology, with an expanding middle class.[56] India has reduced poverty, though alongside increasing economic inequality.[57] It is a nuclear-weapon state, with high military expenditure, and holds unresolved mid-20th-century disputes over Kashmir with its neighbours, Pakistan and China.[58] Socio-economic challenges include gender inequality, child malnutrition,[59] and rising air pollution.[60] India's megadiverse land features four biodiversity hotspots. Its wildlife is supported in protected habitats and traditionally viewed with cultural tolerance.[61]

"""

print(summarize_text(text, api_key))
