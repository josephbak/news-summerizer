import openai
import os
from dotenv import load_dotenv

load_dotenv("./.env")
openai.api_key = os.getenv('OPENAI_KEY')


prompt = """
The infrastructure behind Hive, one of the most prolific ransomware operations, has been seized by law enforcement agencies in the United States and Europe.

Hive saw its dark web portal seized as part of a coordinated law enforcement action carried out by the U.S. Department of Justice, the FBI, Secret Service and several European government agencies, just months after the federal government’s cybersecurity unit CISA sounded the alarm about Hive’s ongoing extortion efforts.

“This hidden site has been seized. The Federal Bureau of Investigation seized this site as part of a coordinated law enforcement action taken against Hive Ransomware,” a seizure notice displayed on Hive’s dark web leak site reads. “This action has been taken in coordination with the United States Attorney’s Office for the Middle District of Florida and the Computer Crime and Intellectual Property Section of the Department of Justice with substantial assistance from Europol.”

The FBI confirmed Thursday that it had access to Hive’s computer network since July 2022, allowing federal agents to capture and offer Hive’s decryption keys to victims worldwide. Since its takeover, the FBI has helped at least 336 victims of the Hive ransomware, according to the affidavit, preventing more than $130 million in ransom payments, said U.S. Attorney General Merrick Garland during a press conference on Thursday,

According to the government, the FBI also successfully disrupted a Hive ransomware attack on a Louisiana Hospital, saving the victim from a $3 million ransom payment, and another attack targeting a school based in Texas.

Hive, which operates a ransomware-as-a-service model, previously targeted a wide range of industries and critical infrastructure, with a particular focus on healthcare and public health entities. The gang claimed Illinois-based Memorial Health System as its first healthcare victim in August 2021, followed by Costa Rica’s public health service and New York-based emergency response and ambulance service provider Empress EMS. Hive also targeted Tata Power, a top power-generation company in India, in October.

Garland added that the FBI has also begun dismantling Hive’s front- and back-end infrastructure in the U.S. and abroad, which included the seizure of two of Hive’s back-end servers located in Los Angeles. The FBI did not say how it identified the Hive servers, and no arrests or indictments were announced during the press conference.
"""
  
def summarize(prompt):
    augmented_prompt = f"summarize this text: {prompt}"
    summarized_text = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]
    return summarized_text


# print(summarize(prompt))