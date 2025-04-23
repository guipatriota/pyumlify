import subprocess

def test_cli_runs(tmp_path):
    """Test basic CLI execution and output generation."""
    out_dir = tmp_path / "uml_out"
    result = subprocess.run(
        ["python", "-m", "pyumlify.cli", "--root", "tests/fixtures", "--output", str(out_dir)],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0, result.stderr
    assert out_dir.exists()
    assert any(f.suffix == ".puml" for f in out_dir.iterdir())
