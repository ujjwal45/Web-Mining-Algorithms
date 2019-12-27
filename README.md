# Web-Mining-Algorithms
### HITS Algorithm

Hyperlink-Induced Topic Search (HITS) (also known as Hubs and authorities) is a link analysis algorithm that rates Web pages, developed by Jon Kleinberg. It determines two values for a page: its authority, which estimates the value of the content of the page, and its hub value, which estimates the value of its links to other pages.
Steps involved in HITS algorithm:
1.	Starting from the user supplied query, HITS assembles initial set S of pages:
The initial set of pages is called root set. These pages are then expanded to a larger root set T by adding any pages that are linked to or from any page in the initial set S.
2.	HITS then associate with each page p a hub weight h(p) and an authority weight a(p), all initialized to 1.
3.	HITS then iteratively update the hubs and authority weights of each page. Let p → q denotes “page p has a hyperlink to page q”. HITS update the hubs and authority as follows:

       a(p)=∑p→qh(q)

       h(p)=∑q→pa(q)

### Naive Bayes

Bayes Theorem helps us to find the probability of a hypothesis given our prior knowledge.

As per wikipedia,In probability theory and statistics, Bayes’ theorem (alternatively Bayes’ law or Bayes’ rule, also written as Bayes’s theorem) describes the probability of an event, based on prior knowledge of conditions that might be related to the event.

