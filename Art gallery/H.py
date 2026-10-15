class ArtGallery:
    def __init__(self, gallery_name, location):
        self.gallery_name = gallery_name
        self.location = location
        self.artworks = []

        print(f"\nWelcome to {self.gallery_name}!")
        print(f"Location: {self.location}")
        print("Art gallery collection is ready.")

    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' has been added to the gallery.")

    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' has been removed.")
        else:
            print(f"'{artwork}' was not found in the gallery.")

    def display_artworks(self):
        print(f"\n--- {self.gallery_name} Art Collection ---")

        if self.artworks:
            for number, artwork in enumerate(self.artworks, 1):
                print(f"{number}. {artwork}")
        else:
            print("No artworks have been added yet.")

    def search_artwork(self, artwork):
        if artwork in self.artworks:
            print(f"'{artwork}' was found in the gallery.")
        else:
            print(f"'{artwork}' was not found in the gallery.")

gallery = ArtGallery("Creative World", "Lahore")

gallery.add_artwork("Starry Night")
gallery.add_artwork("Mona Lisa")
gallery.add_artwork("The Scream")

gallery.display_artworks()

gallery.search_artwork("Mona Lisa")

gallery.remove_artwork("The Scream")

gallery.display_artworks()
