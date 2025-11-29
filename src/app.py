from orchestrator.review_orchestrator import ReviewOrchestrator

def run_review(file_path: str):
    orchestrator = ReviewOrchestrator()
    return orchestrator.run(file_path)

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1]
    print(run_review(file_path))
