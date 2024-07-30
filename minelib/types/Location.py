from dataclasses import dataclass

@dataclass
class Location():
    X: float
    Y: float
    Z: float
    relative: bool = False

    def to_string(self):
        if self.relative:
            return f"~{self.X if self.X != 0 else ''} ~{self.Y if self.Y != 0 else ''} ~{self.Z if self.Z != 0 else ''}"
        else:
            return f"{self.X} {self.Y} {self.Z}"