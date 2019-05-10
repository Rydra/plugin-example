from plugin_exercise.interfaces import PolicyAnalyzer


class SuperPolicyAnalyzer(PolicyAnalyzer):
    def analyze(self):
        print('Ima super policy analyzer')


class MegaPolicyAnalyzer(PolicyAnalyzer):
    def analyze(self):
        print('Ima mega policy analyzer')
