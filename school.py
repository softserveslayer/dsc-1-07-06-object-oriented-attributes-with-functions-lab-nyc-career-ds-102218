class School:
    def __init__(self, name):
        self._name = name
        self._roster = {}
        
    
    def roster(self):
        return self._roster
    
    def add_student(self, name, grade):
        if grade in self._roster:
            self._roster[grade].append(name)
        else:
            self._roster[grade] = [name]
            
    def grade(self, grade):
        if grade in self._roster:
            return self._roster[grade]
 
    def sort_roster(self):
        return {x:sorted(self._roster[x]) for x in self._roster.keys()}
        
     
    
# Define a method called sort_roster that returns the school's roster where the strings in the student arrays are sorted alphabetically. For instance: {9: ["Kelly Slater"], 10: ["Ryan Sheckler", "Tony Hawk"], 11: ["Bethany Hamilton"], 12: ["Peter Piper"]}}

# >>> d1 = {"B" : ["x", "z", "k"], "A" : ["a", "c", "b"]}
# >>> d2 = {x:sorted(d1[x]) for x in d1.keys()}
# >>> d2
# {'A': ['a', 'b', 'c'], 'B': ['k', 'x', 'z']}