from png2svg.cli import build_parser


def test_parser_accepts_input_output_and_radius():
    parser = build_parser()

    args = parser.parse_args(
        [
            "input.png",
            "output.svg",
            "--radius",
            "10",
        ]
    )

    assert args.input == "input.png"
    assert args.output == "output.svg"
    assert args.radius == 10
