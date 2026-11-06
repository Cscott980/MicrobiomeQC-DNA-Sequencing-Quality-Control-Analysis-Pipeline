from Bio import SeqIO
from pathlib import Path
import gzip


def open_fastq(file_path):
    """Open plain-text or compressed FASTQ files."""

    file_path = Path(file_path)

    if file_path.suffix == ".gz":
        return gzip.open(file_path, "rt")

    return open(file_path, "r")


def process_fastq(file_path):
    """Extract sequencing information from FASTQ."""

    results = []

    with open_fastq(file_path) as handle:

       for record in SeqIO.parse(handle, "fastq"):

            sequence = str(record.seq)

            quality_scores = record.letter_annotations[
                "phred_quality"
            ]

            results.append({
                "read_id": record.id,
                "sequence": sequence,
                "length": len(sequence),
                "average_quality": (
                    sum(quality_scores) / len(quality_scores)
                    if quality_scores else 0.0
                )
            })

    return results


if __name__ == "__main__":

    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent
    
    file_path = project_root / "data" / "sample_data" / "demo.fastq"

    reads = process_fastq(file_path)

    print(f"Total reads: {len(reads)}")

    for read in reads:
        print(read)

"""
Result Sample: 
    Total reads: 4
{'read_id': 'SAMPLE_001', 'sequence': 'ATCGATCGATCG', 'length': 12, 'average_quality': 40.0}
{'read_id': 'SAMPLE_002', 'sequence': 'GCTAGCTAGCTA', 'length': 12, 'average_quality': 39.0}
{'read_id': 'SAMPLE_003', 'sequence': 'TTGCAATTGCAA', 'length': 12, 'average_quality': 40.0}
{'read_id': 'SAMPLE_004', 'sequence': 'CGATCGATCGAT', 'length': 12, 'average_quality': 39.0}

"""