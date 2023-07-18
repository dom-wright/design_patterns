'''
Proxy

A sort of wrapper class that controls access to the wrapped object. The proxy object acts as an intermediary, which can add functionality, restrict / control access, implement lazy initialisation, or provide a layer of abstraction for the underlying object (hide and protect its underlying details).

Facade vs Proxy:
- Proxies generally control access to one other object and are intended to provide additional behaviours / restrictions when accessing the target. It's purpose is not to hide complexity, even if it might.
- Facade provides a simplified interface to a complex subsystem, which can involve many classes and functions. It's purpose is only to abstract away complexity.

Example:
- Example 1 implements authentication and authorisation for sensitive patient data.
- Example 2 allows for lazy implementation, allowing for the image object to be prepared first, but only loading in the actual image when it is needed.
'''

# Example 1


class PatientFileManager:
    def __init__(self):
        self.__patients = {}

    def _add_patient(self, patient_id, data):
        self.__patients[patient_id] = data

    def _get_patient(self, patient_id):
        return self.__patients[patient_id]


class AccessManager(PatientFileManager):
    def __init__(self, fm):
        self.fm = fm

    def add_patient(self, patient_id, data, password):
        if password == 'sudo':
            self.fm._add_patient(patient_id, data)
        else:
            print("Wrong password.")

    def get_patient(self, patient_id, password):
        if password == 'totallytheirdoctor' or password == 'sudo':
            return self.fm._get_patient(patient_id)
        else:
            print("Only their doctor can access this patients data.")


pfm = PatientFileManager()
am = AccessManager(pfm)
am.add_patient('Jessica', ['pneumonia 2020-23-03', 'shortsighted'], 'sudo')

print(am.get_patient('Jessica', 'totallytheirdoctor'))


# Example 2

class Image:
    def display(self):
        pass


class RealImage(Image):
    def __init__(self, filename):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")


class ImageProxy(Image):
    def __init__(self, filename):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()


image_proxy = ImageProxy("image.jpg")
# The real image is not loaded yet

image_proxy.display()
# The real image is loaded and displayed

image_proxy.display()
# The real image is already loaded, so it is displayed again
