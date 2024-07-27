import random
import matplotlib.pyplot as plt
import networkx as nx
text_data = """
Once upon a time in a land far, far away, there was a small village nestled among the hills.
The village was known for its beautiful scenery and friendly inhabitants.
In this village, there was a young girl named Lily who loved to explore the forests and meadows.
"""
text_data = text_data.lower()
text_data = text_data.replace('\n', ' ')
words = text_data.split()
markov_chain = {}
for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    if word not in markov_chain:
        markov_chain[word] = {}
    if next_word not in markov_chain[word]:
        markov_chain[word][next_word] = 0
    markov_chain[word][next_word] += 1
def generate_text(chain, start_word, num_words):
    word = start_word
    output = [word]
    for _ in range(num_words - 1):
        word = random.choices(list(chain[word].keys()), weights=list(chain[word].values()))[0]
        output.append(word)
    return ' '.join(output)
start_word = random.choice(words)
generated_text = generate_text(markov_chain, start_word, 50)
print(generated_text)
G = nx.DiGraph()
for word, transitions in markov_chain.items():
    for next_word, weight in transitions.items():
        G.add_edge(word, next_word, weight=weight)
pos = nx.spring_layout(G, k=0.5, iterations=50)
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=5000, node_color="lightblue", font_size=10, font_weight="bold", edge_color="gray")
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Markov Chain of Text Data")
plt.show()
