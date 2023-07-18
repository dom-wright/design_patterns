'''
Adapter

Allows objects with incompatible interfaces to work together, just like any adapter in the real world. It is a sort of wrapper object, that offers the required interface for the task, while internally calling the correct methods on the object it wraps.

Example:
In the example, a legacy component and new component both do similar things, but have a different interface / method names. This is no good for the user, as it must consistently call the same method name (the new method name: "perform_operation"), no matter which object it is fed. The solution is to create an adapter for the legacy object, which will define "perform_operation" and within its code, and call the correct operation on the legacy object.
'''


class LegacyComponent:
    def specific_operation(self):
        print("Legacy component's operation")


class NewInterface:
    def perform_operation(self):
        print("New operation!")


class Adapter(NewInterface):
    def __init__(self, legacy_component):
        self.legacy_component = legacy_component

    def perform_operation(self):
        self.legacy_component.specific_operation()


new_component = NewInterface()
legacy_component = LegacyComponent()
adapted_legacy_component = Adapter(legacy_component)

for component in (new_component, adapted_legacy_component):
    component.perform_operation()
