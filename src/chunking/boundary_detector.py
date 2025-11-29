class BoundaryDetector:
    """
    Detect segment boundaries from layout + metadata.
    Rules:
    - Table → break
    - Heading-like lines → break
    - Density jumps → break
    """

    @staticmethod
    def is_heading(text):
        # Simple heuristic for headings
        return text.isupper() or text.endswith(":") or len(text.split()) <= 3

    @staticmethod
    def find_boundaries(items):
        boundaries = []
        start = 0

        for idx in range(1, len(items)):
            prev = items[idx - 1]
            curr = items[idx]

            # Break on table rows
            if curr["type"] == "table_row":
                boundaries.append((start, idx))
                start = idx
                continue

            # Break on headings
            if BoundaryDetector.is_heading(curr["text"]):
                boundaries.append((start, idx))
                start = idx
                continue

            # Break on density spike
            if abs(prev["density"] - curr["density"]) > 0.10:
                boundaries.append((start, idx))
                start = idx

        # Final segment
        boundaries.append((start, len(items)))

        return boundaries
