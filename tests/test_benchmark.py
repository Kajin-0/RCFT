from rcft.benchmark import BenchmarkSource
from rcft.io import read_jsonl


def test_benchmark_source_round_trip():
    source = BenchmarkSource.from_dict(
        {
            "key": "hampapura_mukhi_2015_two_characters",
            "title": "On 2d Conformal Field Theories with Two Characters",
            "url": "https://arxiv.org/abs/1510.04478",
            "category": "two_character_mlde",
            "rank_regime": "n=2",
            "benchmark_role": "admissible two-character MLDE reproduction baseline",
        }
    )

    as_dict = source.to_dict()

    assert as_dict["key"] == "hampapura_mukhi_2015_two_characters"
    assert as_dict["extraction_status"] == "not_started"
    assert as_dict["metadata"] == {}


def test_source_manifest_records_are_parseable():
    records = list(read_jsonl("data/benchmarks/source_manifest.jsonl"))
    sources = [BenchmarkSource.from_dict(record) for record in records]

    assert len(sources) >= 6
    assert {source.rank_regime for source in sources} >= {"n=2", "n=3"}
    assert all(source.key for source in sources)
    assert all(source.url.startswith("https://") for source in sources)
