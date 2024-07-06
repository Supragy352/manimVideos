import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Adding nodes and edges based on our learnings
G.add_edges_from([
    ("Learning Summary", "AgroAdvisor Project"),
    ("AgroAdvisor Project", "Research Paper"),
    ("Research Paper", "Crop Yield Prediction"),
    ("Research Paper", "Soil Health Assessment"),
    ("Research Paper", "Weather Forecasting"),
    ("Research Paper", "Pest and Disease Management"),
    ("AgroAdvisor Project", "Data Visualization"),
    ("Data Visualization", "Crop Yield Predictions"),
    ("Data Visualization", "Soil Health Heatmap"),
    ("Data Visualization", "Monthly Weather Trends"),
    ("Data Visualization", "Crop Prices"),
    ("Data Visualization", "Crop Diseases Distribution"),
    ("Learning Summary", "Book Summaries"),
    ("Book Summaries", "AI: A Modern Approach"),
    ("AI: A Modern Approach", "Core AI Concepts"),
    ("AI: A Modern Approach", "Advanced Topics"),
    ("AI: A Modern Approach", "Practical Applications"),
    ("Book Summaries", "AI: Guide to Intelligent Systems"),
    ("AI: Guide to Intelligent Systems", "Rule-Based Systems"),
    ("AI: Guide to Intelligent Systems", "Uncertainty Management"),
    ("AI: Guide to Intelligent Systems", "Neural Networks"),
    ("AI: Guide to Intelligent Systems", "Hybrid Systems"),
    ("AI: Guide to Intelligent Systems", "Data Mining"),
    ("Learning Summary", "AI Model Development"),
    ("AI Model Development", "Crop Yield Prediction Model"),
    ("Crop Yield Prediction Model", "Data Collection"),
    ("Crop Yield Prediction Model", "Model Selection"),
    ("Crop Yield Prediction Model", "Training and Evaluation"),
    ("Crop Yield Prediction Model", "Example Prediction"),
    ("Learning Summary", "Latest AI Developments"),
    ("Latest AI Developments", "Generative AI Models"),
    ("Generative AI Models", "GPT-4"),
    ("Generative AI Models", "DALL-E 2"),
    ("Latest AI Developments", "AI in Healthcare"),
    ("AI in Healthcare", "Predictive Analytics"),
    ("AI in Healthcare", "Medical Imaging"),
    ("Latest AI Developments", "AI for Climate Change"),
    ("AI for Climate Change", "Climate Modeling"),
    ("AI for Climate Change", "Sustainable Practices"),
    ("Latest AI Developments", "Robotics and Autonomous Systems"),
    ("Robotics and Autonomous Systems", "Improved Autonomy"),
    ("Robotics and Autonomous Systems", "Human-Robot Collaboration"),
    ("Latest AI Developments", "AI Ethics and Governance"),
    ("AI Ethics and Governance", "Fairness and Bias Mitigation"),
    ("AI Ethics and Governance", "Regulation and Policy"),
    ("Latest AI Developments", "NLP"),
    ("NLP", "Multilingual Models"),
    ("NLP", "Contextual Understanding"),
    ("Latest AI Developments", "AI in Finance"),
    ("AI in Finance", "Fraud Detection"),
    ("AI in Finance", "Algorithmic Trading"),
    ("Latest AI Developments", "AI-Driven Personalization"),
    ("AI-Driven Personalization", "Customer Experience"),
    ("Latest AI Developments", "Edge AI"),
    ("Edge AI", "On-Device Processing"),
    ("Latest AI Developments", "Quantum AI"),
    ("Quantum AI", "Quantum Computing")
])

# Set positions for nodes using graphviz layout
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')

# Draw the graph
plt.figure(figsize=(11.7, 16.5))  # Portrait A4 size
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=8, font_weight="bold", arrows=True, arrowstyle='-|>', arrowsize=15, edge_color="gray")

plt.title('Learning Summary Tree', size=20)
plt.show()
