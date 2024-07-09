**Overview**

The present work was conducted within the scope of the Data Structures and Algorithms course, with the main objective of implementing a Graph ADT with query, insertion, removal, and search methods, based on previously available databases related to users of the GitHub and Facebook social networks. It is important to start by noting that social network analysis is a field of study aimed at investigating the structure of relationships that connect individuals (or other social units, such as organizations) and how these relationships influence behaviors and attitudes. Generally, social network analysis studies are represented by Graphs, which are nothing more than graphical representations of individuals and their social relationships. A social network consists of a set of nodes (individuals) and connections (links) between them. The nodes represent people, entities, organizations, systems, computational elements, etc., which can be analyzed individually or collectively, observing the relationship between them. One of the objectives of these analyses is to understand the social impact of the nodes through their connections, in the formation of the network structure through their relationships. Social networks can be formalized and analyzed through Graph theory, using mathematical formulations to understand the elements and their relationships within the network. In this sense, Graph theory can be considered a branch of applied mathematics that seeks to solve problems within a network of relationships. As mentioned, a good way to identify a network is as a Graph, composed of a set of points also called vertices connected by lines called edges. Graphs are structures that can represent various types of data. This representation is generally quite efficient for representing relationships between individuals, which naturally led to its adoption by scientists in these areas as a means to study and represent social networks. In this sense, Graph theory has been increasingly used in social network analyses due to its representation capacity and high simplicity.

Using Graph network theories and algorithms, it is possible to analyze a social network and extract various metrics from this network. For example, the number of communities or groups existing in these networks and which vertices (nodes) are the most important in the network. From this knowledge, it is possible to direct efforts to the most important points in the network, optimizing resources and time. For example, observing the example of the Graph below, it is easy to see which vertex is the most central in the network. Likewise, the number of connections of a vertex reflects its size, so we can also observe that the most central vertex is also the most connected. Thus, information delivered to this network through this vertex is more likely to reach the other vertices in the network faster than by choosing another vertex at random.

In this sense, the present work aims to analyze, based on data from the GitHub and Facebook social networks, the connections between their members, evaluating dimensions such as influence, centrality, and proximity. For this purpose, an algorithm (Dijkstra) was implemented to determine the centrality and the shortest path between connections within those social networks. The implemented solution can be useful for analyzing any other type of social network, as well as other types of real-life applications, such as navigation in transport applications, data traffic management in computer networks, or even financial exchanges (such as currency).

In the present work and based on the defined concepts, code was developed to implement methods to determine the shortest paths in the created Graph for the social networks used: (a) without using weights on the edges; (b) using weights on the edges. Measures of degree centrality and closeness centrality were also implemented. Following the implementation of the centrality measures, results were presented related to: the top 10 most interconnected vertices in the network; the top 10 vertices that are closest to the others; and the top 10 least interconnected vertices in the network. Application tests were presented on the provided databases (GitHub and Facebook), with the objective of testing the developed methods and obtaining results of centrality, proximity, and shortest path calculation. As an extra element and with the aim of visualizing the Graph, the 'networkx' and 'matplotlib' libraries were used, and connection graphs of the GitHub and Facebook social network users were presented.


**Full Report**

The full Report, with detailed explanations and results, is present in the *'Grupo_A13.pdf'* file.
