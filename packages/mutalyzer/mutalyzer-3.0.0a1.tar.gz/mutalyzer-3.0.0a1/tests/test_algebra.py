import pytest

from mutalyzer.algebra import _get_hgvs_and_variant, _get_id, compare
from mutalyzer.reference import retrieve_reference

from .commons import code_in, patch_retriever


@pytest.mark.parametrize(
    "reference_id",
    ["NM_012459.2", "LRG_24"],
)
def test_get_id(reference_id):
    assert _get_id(reference_id) == {
        "input": reference_id,
        "type": "id",
        "reference": {"id": reference_id},
        "sequence": retrieve_reference(reference_id)["sequence"]["seq"],
    }


@pytest.mark.parametrize(
    "reference_id",
    ["NO_REF"],
)
def test_get_id_no_ref(reference_id):
    assert _get_id(reference_id) == {
        "input": reference_id,
        "type": "id",
        "reference": {"id": reference_id},
        "errors": [
            {
                "code": "ERETR",
                "details": "Reference NO_REF could not be retrieved.",
                "paths": [[]],
            }
        ],
    }


@pytest.mark.parametrize(
    "description, expected",
    [
        (
            "NM_012459.2:c.1del",
            {
                "input": "NM_012459.2:c.1del",
                "type": "hgvs",
                "reference": {"id": "NM_012459.2"},
                "sequence": "AAGTCGAGAGGCGGTGCACACCCGTCGCGCTGCGCAAACACAGCTGTCGG"
                "AAGGTGGCGAGCCTGAGGCGAACAATGGCGGAGCTGGGCGAAGCCGATGAAGCGGAGTTGCA"
                "GCGCCTGGTGGCCGCCGAGCAGCAGAAGGCGCAGTTTACTGCACAGGTGCATCACTTCATGG"
                "AGTTATGTTGGGATAAATGTGTGGAGAAGCCAGGGAATCGCCTAGACTCTCGCACTGAAAAT"
                "TGTCTCTCCAGCTGTGTAGACCGCTTCATTGACACCACTCTTGCCATCACCAGTCGGTTTGC"
                "CCAGATTGTACAGAAAGGAGGGCAGTAGGCCATCCCCCAGGAGAATGACAGAAGCAAAGGAC"
                "TTGTTACTAAGCAGATTTAAGGGTCAGTGGGGGAAGGCTATCAACCCATTGTCAGATCAGCA"
                "TCAGGCTGTTATCAAGTCTGTTGGTGCTAAAAAGTAAAAGATGAAATGTTCAAAGAGTGAAA"
                "TTTATTTATTTGGAATTCAGAAATTCCAGGTTGTATGACATCAGTTACTCAATAAGTGTGAA"
                "TTCTCCAACTCTTCTTTTAATCCCATTTTAGAATTTAATATAGAGATCTCTGATTGGCAGGA"
                "ACACTAGAAATAAATGTTCCATGGCCAGTAGTGCAAATGGGGGATTGTAGGTTTTGAAAAAC"
                "CACCCTAAGCCATATTAAGGGGGTTGGAAGAACCATCGAAGCCTAAGGCATAGAAGAAAATT"
                "TGGGGTTAAGAAAGATGAAGAACAAAAAACAGCTTTATTGCTTATACATGACCAAGAAAAGG"
                "AAAACATGGCAAAAAAAAAAAAAAAAAA",
                "reference_sequence": "AAGTCGAGAGGCGGTGCACACCCGTCGCGCATGCGCAAAC"
                "ACAGCTGTCGGAAGGTGGCGAGCCTGAGGCGAACAATGGCGGAGCTGGGCGAAGCCGATGA"
                "AGCGGAGTTGCAGCGCCTGGTGGCCGCCGAGCAGCAGAAGGCGCAGTTTACTGCACAGGTG"
                "CATCACTTCATGGAGTTATGTTGGGATAAATGTGTGGAGAAGCCAGGGAATCGCCTAGACT"
                "CTCGCACTGAAAATTGTCTCTCCAGCTGTGTAGACCGCTTCATTGACACCACTCTTGCCAT"
                "CACCAGTCGGTTTGCCCAGATTGTACAGAAAGGAGGGCAGTAGGCCATCCCCCAGGAGAAT"
                "GACAGAAGCAAAGGACTTGTTACTAAGCAGATTTAAGGGTCAGTGGGGGAAGGCTATCAAC"
                "CCATTGTCAGATCAGCATCAGGCTGTTATCAAGTCTGTTGGTGCTAAAAAGTAAAAGATGA"
                "AATGTTCAAAGAGTGAAATTTATTTATTTGGAATTCAGAAATTCCAGGTTGTATGACATCA"
                "GTTACTCAATAAGTGTGAATTCTCCAACTCTTCTTTTAATCCCATTTTAGAATTTAATATA"
                "GAGATCTCTGATTGGCAGGAACACTAGAAATAAATGTTCCATGGCCAGTAGTGCAAATGGG"
                "GGATTGTAGGTTTTGAAAAACCACCCTAAGCCATATTAAGGGGGTTGGAAGAACCATCGAA"
                "GCCTAAGGCATAGAAGAAAATTTGGGGTTAAGAAAGATGAAGAACAAAAAACAGCTTTATT"
                "GCTTATACATGACCAAGAAAAGGAAAACATGGCAAAAAAAAAAAAAAAAAA",
                "view": {
                    "views": [
                        {
                            "start": 0,
                            "end": 30,
                            "type": "outside",
                            "left": "AAGTCGAGAG",
                            "right": "CCCGTCGCGC",
                        },
                        {
                            "description": "1del",
                            "start": 30,
                            "end": 31,
                            "type": "variant",
                            "deleted": {"sequence": "A"},
                        },
                        {
                            "start": 31,
                            "end": 823,
                            "type": "outside",
                            "left": "TGCGCAAACA",
                            "right": "AAAAAAAAAA",
                        },
                    ],
                    "seq_length": 823,
                },
            },
        )
    ],
)
def test_get_hgvs(description, expected):
    assert _get_hgvs_and_variant(description) == expected


@pytest.mark.parametrize(
    "params, expected",
    [
        (
            ("AAAAA", "sequence", "ATAAAAA", "sequence", "2_3insT", "variant"),
            {
                "relation": "disjoint",
                "influence_lhs": {"min_pos": 0, "max_pos": 5},
                "influence_rhs": {"min_pos": 2, "max_pos": 2},
                "view_rhs": {
                    "views": [
                        {"start": 0, "end": 2, "type": "outside", "sequence": "AA"},
                        {
                            "description": "2_3insT",
                            "start": 2,
                            "end": 2,
                            "type": "variant",
                            "inserted": {"sequence": "T", "length": 1},
                        },
                        {"start": 2, "end": 5, "type": "outside", "sequence": "AAA"},
                    ],
                    "seq_length": 5,
                },
            },
        ),
        (
            (
                None,
                None,
                "LRG_24:g.5525_5532del",
                "hgvs",
                "LRG_24:g.5525_5533del",
                "hgvs",
            ),
            {
                "relation": "is_contained",
                "influence_lhs": {"min_pos": 5522, "max_pos": 5534},
                "influence_rhs": {"min_pos": 5522, "max_pos": 5534},
                "view_lhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5532del",
                            "start": 5524,
                            "end": 5532,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCAC"},
                        },
                        {
                            "start": 5532,
                            "end": 11486,
                            "type": "outside",
                            "left": "CAGGGAAGGA",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
                "view_rhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5533del",
                            "start": 5524,
                            "end": 5533,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCACC"},
                        },
                        {
                            "start": 5533,
                            "end": 11486,
                            "type": "outside",
                            "left": "AGGGAAGGAT",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
            },
        ),
        (
            (
                None,
                None,
                "LRG_24:g.5525_5532del",
                "hgvs",
                "LRG_24:g.5525_5533del",
                "hgvs",
            ),
            {
                "relation": "is_contained",
                "influence_lhs": {"min_pos": 5522, "max_pos": 5534},
                "influence_rhs": {"min_pos": 5522, "max_pos": 5534},
                "view_lhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5532del",
                            "start": 5524,
                            "end": 5532,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCAC"},
                        },
                        {
                            "start": 5532,
                            "end": 11486,
                            "type": "outside",
                            "left": "CAGGGAAGGA",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
                "view_rhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5533del",
                            "start": 5524,
                            "end": 5533,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCACC"},
                        },
                        {
                            "start": 5533,
                            "end": 11486,
                            "type": "outside",
                            "left": "AGGGAAGGAT",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
            },
        ),
        (
            (
                "LRG_24",
                "id",
                "LRG_24:g.5525_5532del",
                "hgvs",
                "LRG_24:g.5525_5533del",
                "hgvs",
            ),
            {
                "relation": "is_contained",
                "influence_lhs": {"min_pos": 5522, "max_pos": 5534},
                "influence_rhs": {"min_pos": 5522, "max_pos": 5534},
                "view_lhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5532del",
                            "start": 5524,
                            "end": 5532,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCAC"},
                        },
                        {
                            "start": 5532,
                            "end": 11486,
                            "type": "outside",
                            "left": "CAGGGAAGGA",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
                "view_rhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5533del",
                            "start": 5524,
                            "end": 5533,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCACC"},
                        },
                        {
                            "start": 5533,
                            "end": 11486,
                            "type": "outside",
                            "left": "AGGGAAGGAT",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
            },
        ),
        (
            (
                "LRG_24",
                "id",
                "LRG_24:g.5525_5532del",
                "hgvs",
                "LRG_24:g.5525_5533del",
                "hgvs",
            ),
            {
                "relation": "is_contained",
                "influence_lhs": {"min_pos": 5522, "max_pos": 5534},
                "influence_rhs": {"min_pos": 5522, "max_pos": 5534},
                "view_lhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5532del",
                            "start": 5524,
                            "end": 5532,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCAC"},
                        },
                        {
                            "start": 5532,
                            "end": 11486,
                            "type": "outside",
                            "left": "CAGGGAAGGA",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
                "view_rhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTTCACACTT",
                            "right": "CCGGCCTGCC",
                        },
                        {
                            "description": "5525_5533del",
                            "start": 5524,
                            "end": 5533,
                            "type": "variant",
                            "deleted": {"sequence": "CGGGGCACC"},
                        },
                        {
                            "start": 5533,
                            "end": 11486,
                            "type": "outside",
                            "left": "AGGGAAGGAT",
                            "right": "ATACACATAC",
                        },
                    ],
                    "seq_length": 11486,
                },
            },
        ),
        (
            (
                None,
                None,
                "NG_008376.4:g.5525_5532del",
                "hgvs",
                "LRG_303:g.5525_5532del",
                "hgvs",
            ),
            {
                "relation": "equivalent",
                "influence_lhs": {"min_pos": 5519, "max_pos": 5534},
                "influence_rhs": {"min_pos": 5519, "max_pos": 5534},
                "view_lhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTGTCTGCCA",
                            "right": "AGATGAGTTA",
                        },
                        {
                            "description": "5525_5532del",
                            "start": 5524,
                            "end": 5532,
                            "type": "variant",
                            "deleted": {"sequence": "GTCCTGAG"},
                        },
                        {
                            "start": 5532,
                            "end": 11312,
                            "type": "outside",
                            "left": "TGCCGTTTAA",
                            "right": "AAGAGGGATC",
                        },
                    ],
                    "seq_length": 11312,
                },
                "view_rhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 5524,
                            "type": "outside",
                            "left": "GTGTCTGCCA",
                            "right": "AGATGAGTTA",
                        },
                        {
                            "description": "5525_5532del",
                            "start": 5524,
                            "end": 5532,
                            "type": "variant",
                            "deleted": {"sequence": "GTCCTGAG"},
                        },
                        {
                            "start": 5532,
                            "end": 11312,
                            "type": "outside",
                            "left": "TGCCGTTTAA",
                            "right": "AAGAGGGATC",
                        },
                    ],
                    "seq_length": 11312,
                },
            },
        ),
        (
            (
                None,
                None,
                "NG_012337.3:g.274>A",
                "hgvs",
                "274del",
                "variant",
            ),
            {
                "relation": "contains",
                "influence_lhs": {"min_pos": 272, "max_pos": 275},
                "influence_rhs": {"min_pos": 274, "max_pos": 274},
                "view_lhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 273,
                            "type": "outside",
                            "left": "GGGCTTGGTT",
                            "right": "ACGAAGAATA",
                        },
                        {
                            "description": "274>A",
                            "start": 273,
                            "end": 274,
                            "type": "variant",
                            "deleted": {"sequence": "T"},
                            "inserted": {"sequence": "A", "length": 1},
                        },
                        {
                            "start": 274,
                            "end": 39784,
                            "type": "outside",
                            "left": "ACTTGCCATC",
                            "right": "ACTCAAGGAA",
                        },
                    ],
                    "seq_length": 39784,
                },
                "view_rhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 273,
                            "type": "outside",
                            "left": "GGGCTTGGTT",
                            "right": "ACGAAGAATA",
                        },
                        {
                            "description": "274del",
                            "start": 273,
                            "end": 274,
                            "type": "variant",
                            "deleted": {"sequence": "T"},
                        },
                        {
                            "start": 274,
                            "end": 39784,
                            "type": "outside",
                            "left": "ACTTGCCATC",
                            "right": "ACTCAAGGAA",
                        },
                    ],
                    "seq_length": 39784,
                },
            },
        ),
        (
            (
                None,
                None,
                "NG_012337.3:g.274>A",
                "hgvs",
                "274del",
                "variant",
            ),
            {
                "relation": "contains",
                "influence_lhs": {"min_pos": 272, "max_pos": 275},
                "influence_rhs": {"min_pos": 274, "max_pos": 274},
                "view_lhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 273,
                            "type": "outside",
                            "left": "GGGCTTGGTT",
                            "right": "ACGAAGAATA",
                        },
                        {
                            "description": "274>A",
                            "start": 273,
                            "end": 274,
                            "type": "variant",
                            "deleted": {"sequence": "T"},
                            "inserted": {"sequence": "A", "length": 1},
                        },
                        {
                            "start": 274,
                            "end": 39784,
                            "type": "outside",
                            "left": "ACTTGCCATC",
                            "right": "ACTCAAGGAA",
                        },
                    ],
                    "seq_length": 39784,
                },
                "view_rhs": {
                    "views": [
                        {
                            "start": 0,
                            "end": 273,
                            "type": "outside",
                            "left": "GGGCTTGGTT",
                            "right": "ACGAAGAATA",
                        },
                        {
                            "description": "274del",
                            "start": 273,
                            "end": 274,
                            "type": "variant",
                            "deleted": {"sequence": "T"},
                        },
                        {
                            "start": 274,
                            "end": 39784,
                            "type": "outside",
                            "left": "ACTTGCCATC",
                            "right": "ACTCAAGGAA",
                        },
                    ],
                    "seq_length": 39784,
                },
            },
        ),
    ],
)
def test_compare(params, expected):
    assert compare(*params) == expected


@pytest.mark.parametrize(
    "params, expected",
    [
        (
            (
                None,
                "hgvs",
                "NG_012337.3:g.274>A",
                "HGVS",
                "1delete",
                "varianT",
            ),
            {
                "errors": {
                    "reference_type": [
                        {
                            "code": "EINVALIDINPUT",
                            "details": "'hgvs' not valid.",
                            "options": ["sequence", "id"],
                        }
                    ],
                    "lhs_type": [
                        {
                            "code": "EINVALIDINPUT",
                            "details": "'HGVS' not valid.",
                            "options": ["sequence", "variant", "hgvs"],
                        }
                    ],
                    "rhs_type": [
                        {
                            "code": "EINVALIDINPUT",
                            "details": "'varianT' not valid.",
                            "options": ["sequence", "variant", "hgvs"],
                        }
                    ],
                }
            },
        ),
        (
            (
                None,
                None,
                "NG_012337.3:g.274>A",
                "hgvs",
                "1delete",
                "variant",
            ),
            {
                "errors": {
                    "rhs": [
                        {
                            "code": "ESYNTAXUEOF",
                            "details": "Unexpected end of input.",
                            "pos_in_stream": 7,
                            "unexpected_character": "e",
                            "description": "1delete",
                            "expecting": [
                                "'(' for an uncertainty start or before a selector ID",
                                "':' between the reference part and the coordinate system",
                                "a reference / selector ID",
                            ],
                        }
                    ]
                }
            },
        ),
    ],
)
def test_compare_errors(params, expected):
    assert compare(*params) == expected
