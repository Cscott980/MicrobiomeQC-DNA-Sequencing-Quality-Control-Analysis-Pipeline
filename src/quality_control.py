import ingestion
import statistics

total_counted_samples: int = 0

def total_counted(data) -> int:
    """Return the total sample amounts."""
    if not data: return 0
    print(f"Total Samples: {int(len(data))}")
    return int(len(data))

def sample_avg_length(data) -> float:
    """Return the average samples length."""
    if not data: return 0.0
    # Extract the 'length' value from each dictionary
    result: int = statistics.mean(sample['length'] for sample in data)
    print(f"Avarage length: {result}")
    return result
                                                 
def overall_quality(data) -> float:
    result: float = 0.0
    total: float = 0.0
    dividen: int = 0
    if not data: return 0.0

    for samples in data:
        total = samples["length"] + samples["average_quality"]
        dividen += samples["length"]

    result = total / dividen
    print(f"Overall Quailty: {result}")
    return result
    
    

