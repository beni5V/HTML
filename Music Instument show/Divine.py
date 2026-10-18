from abc import ABC, abstractmethod
class Instrument(ABC):
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def display_info(self):
        print(f"🎵 Instrument Name: {self.name}")
        print(f"📂 Category: {self.category}")
    @abstractmethod
    def play_sound(self):
        pass

class Guitar(Instrument):
    def __init__(self, name, category, strings):
        super().__init__(name, category)
        self.strings = strings

    def play_sound(self):
        print(f"🎸 Sound: Strum Strum! ({self.strings} strings)")
class Drum(Instrument):

    def __init__(self, name, category, drum_type):
        super().__init__(name, category)
        self.drum_type = drum_type

    def play_sound(self):
        print(f"🥁 Sound: Boom Boom! ({self.drum_type})")
class Flute(Instrument):

    def __init__(self, name, category, material):
        super().__init__(name, category)
        self.material = material

    def play_sound(self):
        print(f"🪈 Sound: Toot Toot! (Made of {self.material})")

class Piano(Instrument):

    def __init__(self, name, category, keys):
        super().__init__(name, category)
        self.keys = keys

    def play_sound(self):
        print(f"🎹 Sound: Plink Plonk! ({self.keys} keys)")

instruments = [
    Guitar("Acoustic Guitar", "String Instrument", 6),
    Drum("Bass Drum", "Percussion Instrument", "Large Drum"),
    Flute("Bamboo Flute", "Wind Instrument", "Bamboo"),
    Piano("Grand Piano", "Keyboard Instrument", 88) ]

print("=" * 40)
print("🎶 MUSIC INSTRUMENT SOUND SHOW 🎶")
print("=" * 40)

for instrument in instruments:
    print()
    instrument.display_info()
    instrument.play_sound()
    print("-" * 40)

print("🎉 Thanks for visiting the Sound Show!")
