from dataclasses import dataclass

@dataclass
class Album:
    AlbumId: int
    Title: str
    durata: float


    def __hash__(self):
        return hash(self.AlbumId)

    def __str__(self):
        return f"{self.AlbumId} - {self.Title}"

    def __eq__(self, other):
        return self.AlbumId == other.AlbumId