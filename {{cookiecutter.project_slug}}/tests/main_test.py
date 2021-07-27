from {{cookiecutter.project_name}}.main import main


def test_main(capsys):
    main()

    out, err = capsys.readouterr()

    assert out.strip() == "Hello, world!"
    assert err.strip() == ""
