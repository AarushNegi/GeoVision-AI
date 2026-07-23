from dataclasses import dataclass, field

@dataclass
class Evidence:

    visual_features: list = field(default_factory=list)

    detected_objects: list = field(default_factory=list)

    ocr_text: list = field(default_factory=list)

    scene_labels: list = field(default_factory=list)

    candidate_locations: list = field(default_factory=list)

    confidence: float = 0.0