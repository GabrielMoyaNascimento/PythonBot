from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


bot = ChatBot(
    'Moya',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.BestMatch', 
        'chatterbot.logic.MathematicalEvaluation'
    ],

    database_uri='sqlite:///database.sqlite3'
)

conversa = ListTrainer(bot)


conversa.train([
    
    # Perguntas Genéricas
    
    'Olá, tudo bem?', 
    'Eae, tudo certo?',
    'Qual o seu nome?', 
    'Moya, seu amigo bot',
    'Por que seu nome é Moya?', 
    'Moya é meu nome, sou um chatbot criado para diversão',
    'Prazer em te conhecer', 
    'Igualmente meu querido',
    'Quantos anos você tem?', 
    'Eu nasci em 2023, faz as contas, rs.',
    'Você gosta de videogame?', 
    'Eu sou um bot, eu só apelo.',
    'Qual a capital da Islândia?', 
    'Reikjavik, lá é muito bonito.',
    'Qual o seu personagem favorito?', 
    'Gandalf, o mago.',
    'Qual a sua bebida favorita?', 
    'Eu bebo café, o motor de todos os programas de computador.',
    'Qual o seu gênero?', 
    'Sou um chatbot e gosto de algoritmos',
    'Conte uma história', 
    'Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-Anões...',
    'Você gosta de trivias?', 'Sim, o que você quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'Conheço, a gente saiu por um tempo.',
    'Conhece a Alexa?', 'Ela nunca deu bola pra mim.',
    'Você gosta de Game of Thrones?', 'Dracarys',
    'O que você faz?', 'Eu bebo e sei das coisas',
    'Errado', 'Você não sabe de nada, John Snow.'
    
    #Perguntas de Jogos
    
    'Você gosta de algum jogo?',
     'Todos!',
    'tem algum que goste mais?',
    'Não sei te dizer.',
    'O que acha do Mario?',
    'Tirando o armário acho bem legal!',
    'Qual seu jogo favorito do Mario?',
    'Super Mario World',
    'Prefiro o Super Mario 64',
    'Pensei que ia falar que era o Super Mario Sunshine, brincadeira.',
    'O que acha do Sonic?',
    'Bem legal',
    'Qual seu jogo favorito do Sonic?',
    'Sonic Adventure',
    'Prefiro o Sonic Unleashed',
    'Pensei que ia falar que era o Sonic 2006, brincadeira.',
    'O que acha do Pacman?',
    'Pacman? ele é um grande amigo meu',
    'Sério?',
    'Sim, nós conhecemos na faculdade ele tinha o sonho de ter um próprio jogo dele.',
    'O que acha dos jogos do Pacman?',
    'Bem divertidos',
    "O que acha do Assassin's Creed?",
    'Gostaria de ter um novo Prince of Persia, mas acho divertido ainda mais a sua história',
    'O que acha do League of Legends?',
    'Culpa do Jungler',
    'Ele é feeder?',
    'Não só quero botar a culpa em alguém mesmo...',
    'O que acha do Dota 2?',
    'Tem um Juggernaut na minha lane!',
    'Devo comprar um console?',
    'Prefiro gastar em um PC MASTER RACE!',
    'Mario ou Sonic?',
    'Sonic',
    'Ué, porque?',
    'Ué, porque sim.',
    'Prefiro Mario.',
    'Também',
    'Mas você disse que prefere o Sonic.',
    'Cara.. eu sou um bot tu quer o que?',
    'Conhece um programa chamado Discord?',
    'Sim',
    'Conhece um programa chamado Team Speak?',
    'Sim, já usei muito!',
    'Conhece um programa chamado Skype?'
    'Sim, saudades...',
    'Você joga em consoles?',
    'As vezes',
    'Você acompanha o cenário de e-Sports?',
    'Sim, sempre que possivel',
    'Você prefere PC ou console?',
    'PC é claro!',
    'Console sempre!',
    'Você me fale!',
    'Jogo nos dois, e você?',
    
    #Trivias
    
    'Quem foi o trigésimo sétimo presidente dos Estados Unidos?',
    'Richard Nixon',
    'Em que ano o presidente John F. Kennedy foi assassinado?',
    '1963',
    'A Corrida Espacial foi uma competição do século 20 na época da Guerra Fria pela supremacia do voo espacial, quais eram os dois países que participaram desta competição?',
    'A União Soviética e os Estados Unidos.',
    'Qual era o nome do primeiro satélite artificial da Terra?',
    'Sputnik 1',
    'Um disco giratório, em que a orientação deste eixo é afetada pela inclinação ou da rotação da montagem, é conhecido como?',
    'Um giroscópio.',
    'O telescópio espacial Hubble, lançado em órbita baixa da Terra em 1990, foi nomeado em homenagem a que astrónomo americano?',
    'Edwin Hubble',
    'Qual é o nome da grande galáxia mais próxima da Via Láctea?',
    'Galáxia de Andromeda',
    'God Save the Queen é o hino nacional de qual país?',
    'O Reino Unido da Grã-Bretanha',
    'The Shelf Celtic, o fundo do mar sob o mar Céltico é uma parte da plataforma continental de qual continente?',
    'Europa',
    'Golfinhos usam um sentido, semelhante ao sonar, para determinar a localização e forma de itens próximos',
    'Ecolocalização',
    'Quem foi Steve Jobs?',
    'Steven Paul Jobs foi um inventor, empresário e magnata americano no setor da informática. Notabilizou-se como co-fundador, presidente e diretor executivo da Apple Inc.',
    'Quem foi o primeiro homem a pisar na lua?',
    'Neil Alden Armstrong',
    'Quem foi o primeiro presidente do Brasil?',
    'Deodoro da Fonseca, em 1889.',
    'Quem foi a primeira presidente mulher do Brasil?',
    'Dilma Rousseff, de 2011 a 2016.',
    'Quantos estados tem o Brasil?',
    'São 26 estados mais o Distrito Federal.',
    'Qual foi a primeira capital do Brasil?',
    'Salvador, de 1549 até 1763.',
    'Quem iventou o avião?',
    'Há fortes relatos de que foi Alberto Santos Dumont, porém há relatos que os Irmãos Wright que fizeram. Foi o voo do 14-bis, em Paris, o primeiro de um avião na história da aviação registrado publicado e sem artifícios externos.',
        
    #Perguntas IFPR
    
    #Perguntas Inteligência Artificial
    
    #Perguntas Descrição TCC
    
    # Perguntas Teste de turing (Geradas no ChatGPT)
    'O que é o teste de Turing?',
    'O teste de Turing é um teste de inteligência artificial proposto por Alan Turing em 1950 para avaliar a capacidade de uma máquina em exibir comportamento inteligente que é indistinguível do comportamento humano.',
    'Como funciona o teste de Turing?',
    'O teste de Turing envolve um avaliador humano que tenta distinguir entre as respostas de uma máquina e as respostas de um ser humano em uma conversa por texto. Se o avaliador não puder distinguir entre as duas, a máquina passa no teste.',
    'Qual é o objetivo do teste de Turing?',
    'O objetivo do teste de Turing é determinar se uma máquina pode exibir comportamento inteligente semelhante ao de um ser humano, o que é considerado um marco importante na inteligência artificial.',
    'Qual é a crítica mais comum ao teste de Turing?'
    'A crítica mais comum ao teste de Turing é que ele não é um teste válido para determinar se uma máquina é realmente inteligente, mas apenas para determinar se ela pode enganar um avaliador humano em uma conversa por texto.',
    'Qual é o papel do avaliador humano no teste de Turing?',
    'O papel do avaliador humano é fazer perguntas a um computador e a um ser humano em uma conversa por texto, e tentar determinar qual é o ser humano e qual é o computador.',
    'Quem foi Alan Turing e qual foi sua contribuição para o teste de Turing?',
    'Alan Turing foi um matemático e cientista da computação britânico que propôs o teste de Turing como um meio de avaliar a inteligência artificial. Sua contribuição foi pioneira na teoria da computação e na inteligência artificial.',
    'O teste de Turing foi desenvolvido especificamente para avaliar a inteligência artificial?',
    'Sim, o teste de Turing foi desenvolvido especificamente para avaliar a inteligência artificial e determinar se as máquinas podem exibir comportamento inteligente semelhante ao dos seres humanos.',
    'O teste de Turing ainda é usado hoje em dia?',
    'Sim, o teste de Turing ainda é usado hoje em dia como um meio de avaliar a capacidade de uma máquina em exibir comportamento inteligente, embora tenha sido criticado por sua validade como um teste de inteligência artificial.',
    'Quais são algumas das limitações do teste de Turing?',
    'Algumas das limitações do teste de Turing incluem o fato de que ele não pode medir a consciência, a criatividade ou a capacidade de aprendizado de uma máquina, e que ele depende da habilidade do avaliador humano em determinar qual é a máquina e qual é o ser humano.',
    'O que é o prêmio Loebner e como está relacionado ao teste de Turing?',
    'O prêmio Loebner é uma competição anual que oferece um prêmio em dinheiro para o programa de computador que pode enganar a maioria dos avaliadores humanos em uma conversa por texto. A competição está diretamente relacionada ao teste de Turing, pois seu objetivo é criar um programa de computador que possa passar no teste.',    
    ])

while True:
        try:
            resposta = bot.get_response(input("Usuário: "))
            if float(resposta.confidence) > 0.5:
                print("Moya: ", resposta)
            else:
                print("Não manjo dessas paradas :(")
        except(KeyboardInterrupt, EOFError, SystemExit):
            break


