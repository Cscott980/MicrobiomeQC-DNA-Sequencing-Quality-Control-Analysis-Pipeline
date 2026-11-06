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

        while True:
            header = handle.readline()

            if not header:
                break

            sequence = handle.readline().strip()
            separator = handle.readline().strip()
            quality = handle.readline().strip()

            if not header.startswith("@"):
                raise ValueError("Invalid FASTQ header")

            if not separator.startswith("+"):
                raise ValueError("Invalid FASTQ separator")

            quality_scores = [ord(char) - 33 for char in quality]

            results.append({
                "read_id": header.strip()[1:],
                "sequence": sequence,
                "length": len(sequence),
                "average_quality": (
                    sum(quality_scores) / len(quality_scores)
                    if quality_scores else 0.0
                )
            })

    return results


if __name__ == "__main__":

    file_path = "data/sample_data/demo.fastq"

    reads = process_fastq(file_path)

    print(f"Total reads: {len(reads)}")

    for read in reads:
        print(read)
