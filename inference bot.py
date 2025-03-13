class KnowledgeBase:
    def __init__(self):
        self.knowledge_base = []

    def add(self,statement):
        self.knowledge_base.append(statement)
    def remove(self, statement):
        if statement in self.knowledge_base:
            self.knowledge_base.remove(statement)
        else:
            raise Exception('There is no statement to be removed ! ')
    def show(self):
        return self.knowledge_base  

    def and_operation(self,statement1,statement2):
        return statement1 and statement2

    def or_operation(self,statement1,statement2):

        return statement1 or statement2

    def not_operation(self,statement):

        return not statement

# Parent class: KnowledgeBase
class KnowledgeBase:
    def __init__(self):
        self.knowledge_base = []

    def add(self, statement):
        self.knowledge_base.append(statement)

    def remove(self, statement):
        if statement in self.knowledge_base:
            self.knowledge_base.remove(statement)

class InferenceEngine(KnowledgeBase):
    def __init__(self):
        super().__init__()

    def and_operation(self, statement1, statement2):
        if statement1 in self.knowledge_base and statement2 in self.knowledge_base:
            return {statement1, statement2}
        else:
            return {statement1, statement2}

    def or_operation(self, statement1, statement2):
        if statement1 in self.knowledge_base or statement2 in self.knowledge_base:
            return {statement1, statement2}
        else:
            return {statement1, statement2}

inference = InferenceEngine()
inference.add("It is raining")
inference.add("The ground is wet")

result = inference.and_operation("It is raining", "The ground is wet")
print(result)
