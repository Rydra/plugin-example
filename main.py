from straight.plugin import load

from plugin_exercise.interfaces import PolicyAnalyzer

plugins = load("plugin_exercise.plugins", subclasses=PolicyAnalyzer)
instances = plugins.produce()

for instance in instances:
    instance.analyze()
