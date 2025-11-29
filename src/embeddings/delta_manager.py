import json
import os
from src.utils.file_hash import compute_file_hash

class DeltaManager:
    """
    Avoid recomputing embeddings for unchanged files.
    Stores file hash and chunk count in delta.json
    """

    STORE = "vector_store/delta.json"

    @staticmethod
    def load_state():
        if not os.path.exists(DeltaManager.STORE):
            return {}
        return json.load(open(DeltaManager.STORE))

    @staticmethod
    def save_state(state):
        with open(DeltaManager.STORE, "w") as f:
            json.dump(state, f, indent=2)

    @staticmethod
    def needs_update(file_path, chunks):
        state = DeltaManager.load_state()
        file_hash = compute_file_hash(file_path)

        if file_path not in state:
            return True

        old_state = state[file_path]
        return old_state["hash"] != file_hash or old_state["count"] != len(chunks)

    @staticmethod
    def update_state(file_path, chunks):
        state = DeltaManager.load_state()
        state[file_path] = {
            "hash": compute_file_hash(file_path),
            "count": len(chunks)
        }
        DeltaManager.save_state(state)
