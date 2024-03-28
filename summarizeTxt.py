import requests

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": "Bearer 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"}

def query(txt, question):
	response = requests.post(API_URL, headers=headers, json={"inputs" : {
			"question" : f"{question}" , "context" : f"{txt}"
		} 
	})
	return response.json()

test = """ 
La Grande Muraille de Chine est l'une des structures les plus emblématiques au monde. Construite sur plusieurs dynasties, elle s'étend sur environ 21 000 kilomètres. Construite pour protéger la Chine des invasions, elle est aujourd'hui un site touristique majeur.
Situé à Agra, le Taj Mahal est un chef-d'œuvre de l'architecture moghole. Construit au XVIIe siècle par l'empereur Shah Jahan en mémoire de son épouse Mumtaz Mahal, il est renommé pour sa beauté et son élégance.
Un symbole emblématique de la liberté, la Statue de la Liberté se dresse sur l'île de la Liberté à New York. Offerte par la France en 1886, elle accueille les visiteurs du monde entier.
Situé à Rome, le Colisée est un amphithéâtre romain antique. Construit au Ier siècle, il était utilisé pour des spectacles publics, y compris les combats de gladiateurs.
Symbole emblématique de Paris, la Tour Eiffel a été construite pour l'Exposition universelle de 1889. Conçue par Gustave Eiffel, elle attire des millions de visiteurs chaque année.
Niché dans les montagnes des Andes, le Machu Picchu est une ancienne cité inca construite au XVe siècle. Son architecture spectaculaire et son emplacement pittoresque en font un site archéologique unique.
L'une des sept merveilles du monde antique, la Pyramide de Gizeh, est la plus grande des trois pyramides de Gizeh. Construite comme tombeau pour le pharaon Khéops, elle est un chef-d'œuvre de l'ingénierie ancienne.
Surplombant la ville de Rio de Janeiro, la statue du Christ Rédempteur s'élève majestueusement au sommet du mont Corcovado. Avec ses bras ouverts, elle symbolise l'accueil chaleureux du Brésil.
Le Kremlin de Moscou est une forteresse historique qui abrite plusieurs cathédrales, palais et musées. Il est le centre politique et spirituel de la Russie depuis des siècles.
Angkor abrite une vaste collection de temples et de monuments anciens construits par l'Empire khmer entre le IXe et le XVème siècle. Le temple d'Angkor Wat est le plus grand et le plus célèbre de ces édifices.
"""

print(query(test,"Quels sont tous les noms des monuments de ce texte?")["answer"])


