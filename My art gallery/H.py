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
        found = [
            item for item in self.artworks
            if artwork.lower() in item.lower()
        ]

        if found:
            print("\nArtwork search results:")
            for item in found:
                print(f"- {item}")
        else: