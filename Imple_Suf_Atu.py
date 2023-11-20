class State:
    def __init__(self, length):
        self.length = length  # Length of the longest string of this state
        self.edges = {}       # Dictionary for edges (transitions), character: state_index
        self.link = -1        # Suffix link, -1 means undefined

class SuffixAutomaton:
    def __init__(self, s):
        self.states = [State(0)]  # Initialize with the initial state
        self.last = 0              # Index of the last added state

        for character in s:
            self.add_character(character)  # Add characters of the string to the automaton

    def add_character(self, c):
        cur = len(self.states)
        self.states.append(State(self.states[self.last].length + 1))  # Create a new state

        p = self.last
        # Propagate the transitions from the previous states, if they don't have transition for 'c'
        while p >= 0 and c not in self.states[p].edges:
            self.states[p].edges[c] = cur
            p = self.states[p].link

        if p != -1:
            q = self.states[p].edges[c]
            if self.states[p].length + 1 == self.states[q].length:
                # Directly set the suffix link if the condition is met
                self.states[cur].link = q
            else:
                # Need to create a clone state in case of extending an existing state
                clone = len(self.states)
                self.states.append(State(self.states[p].length + 1))
                self.states[clone].edges = self.states[q].edges.copy()
                self.states[clone].link = self.states[q].link

                # Redirect transitions
                while p >= 0 and self.states[p].edges[c] == q:
                    self.states[p].edges[c] = clone
                    p = self.states[p].link

                self.states[q].link = self.states[cur].link = clone
        else:
            # If no previous state has transitions for 'c', set the suffix link of the new state to the initial state
            self.states[cur].link = 0

        self.last = cur  # Update the last added state
